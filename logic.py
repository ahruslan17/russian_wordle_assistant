RUSSIAN_ALPHABET = set("абвгдеёжзийклмнопрстуфхцчшщъыьэюя")
LIMIT = 100000


class WordleAssistant:
    def __init__(self):
        # Load dictionary words, filtering out unwanted characters and enforcing length 5
        with open("russian.txt", encoding="cp1251") as f:
            self.words = [
                w.strip().lower()
                for w in f
                if len(w.strip()) == 5
                and "." not in w
                and "-" not in w
                and set(w.strip().lower()).issubset(RUSSIAN_ALPHABET)
            ]
        # For each position, keep a set of possible letters (initially all)
        self.possible_letters = {pos: set(RUSSIAN_ALPHABET) for pos in range(5)}
        self.banned_letters = set()  # Letters excluded entirely (gray)
        self.yellow_positions = dict()  # Letters confirmed in exact positions (yellow)
        self.required_letters = set()  # Letters that must be present (yellow or white)
        self.iteration = 1
        self.filtered_words = self.words

    def process_input(self, guess, result):
        # Validate input lengths and allowed characters
        if len(guess) != 5 or any(ch not in RUSSIAN_ALPHABET for ch in guess):
            return "Error: word must contain 5 Russian letters."
        if len(result) != 5 or any(ch not in "ywg" for ch in result):
            return "Error: result must be 5 characters consisting of y, w, g."

        self._update_constraints(guess, result)
        self.filtered_words = self._filter_words()
        self.iteration += 1
        return None

    def _update_constraints(self, guess, result):
        # Process yellow letters: fix position, add to required letters, remove from banned
        for i, (ch, res) in enumerate(zip(guess, result)):
            if res == "y":
                self.possible_letters[i] = {ch}
                self.yellow_positions[ch] = i
                self.required_letters.add(ch)
                self.banned_letters.discard(ch)

        # Process white and gray letters
        for i, (ch, res) in enumerate(zip(guess, result)):
            if res == "w":
                # Letter cannot be at this position, but must be present somewhere
                self.possible_letters[i].discard(ch)
                self.required_letters.add(ch)
            elif res == "g":
                # If letter is not yellow or required, ban it from all positions
                if ch not in self.yellow_positions and ch not in self.required_letters:
                    self.banned_letters.add(ch)
                    for pos in self.possible_letters:
                        self.possible_letters[pos].discard(ch)

        # If only one letter remains in a position, ensure it's not banned
        for pos in self.possible_letters:
            if len(self.possible_letters[pos]) == 1:
                letter = next(iter(self.possible_letters[pos]))
                self.banned_letters.discard(letter)

    def _filter_words(self):
        filtered = []
        for w in self.words:
            if (
                all(w[i] in self.possible_letters[i] for i in range(5))
                and not self.banned_letters.intersection(w)
                and all(letter in w for letter in self.required_letters)
            ):
                filtered.append(w)
        return filtered

    def is_solved(self):
        return all(len(letters) == 1 for letters in self.possible_letters.values())

    def get_final_word(self):
        return "".join(next(iter(self.possible_letters[i])) for i in range(5))
