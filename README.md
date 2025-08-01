# Wordle Helper for Russian / 5 Букв

A helper app for the popular word guessing game "Wordle" adapted for the Russian language.
It helps you track guesses, update constraints, and filter possible words based on the feedback you receive in the game.

---

## How to use

* Enter a guessed 5-letter Russian word.
* Enter the result string with letters indicating the color feedback:

  * `y` — yellow: letter is in the word and in the correct position.
  * `w` — white: letter is in the word but in a different position.
  * `g` — gray: letter is not in the word.
* The app will filter possible words and show you hints.

---

## Rules of the game

Source: [tbank.ru](https://www.tbank.ru/finance/blog/legendary-game/?ysclid=mdsthuggc6324954008/gb)

* The player has six attempts to guess a secret five-letter word.
* Each guess must be a valid five-letter word.
* After each guess, the game colors each letter:

  * **Green (yellow in our app)** means the letter is correct and in the right position.
  * **Yellow (white in our app)** means the letter is in the word but in the wrong position.
  * **Gray** means the letter is not in the word.
* The goal is to guess the word within six tries using the color feedback.

---

## Features

* Automatic filtering of possible words based on input feedback.
* Tracking of banned, required letters, and positional constraints.
* Displays remaining possible words and constraints for each letter position.
* Input validation for Russian letters and feedback symbols.
* Reset option to start a new game.

---

## Installation and running

1. Make sure you have Python 3.8+ installed.
2. Install dependencies:

   ```bash
   pip install streamlit
   ```
3. Place `russian.txt` word list in the project folder (encoded in CP1251).
4. Run the app:

   ```bash
   streamlit run app.py
   ```

---

# Помощник для игры "5 букв" (Wordle на русском)

Приложение помогает играть в популярную игру угадывания слов «5 букв» (аналог Wordle) на русском языке.
Вы вводите свои попытки и цветовые подсказки, а программа автоматически отсеивает неподходящие слова и подсказывает возможные варианты.

---

## Как пользоваться

* Введите предполагаемое 5-буквенное русское слово.
* Введите результат в виде строки из символов, означающих цвет подсказки:

  * `y` — жёлтый: буква на своём месте.
  * `w` — белый: буква есть в слове, но в другой позиции.
  * `g` — серый: буквы в слове нет.
* Программа отфильтрует возможные слова и покажет подсказки.

---

## Правила игры

Источник: [tbank.ru](https://www.tbank.ru/finance/blog/legendary-game/?ysclid=mdsthuggc6324954008/gb)

* Игроку даётся шесть попыток угадать секретное слово из 5 букв.
* Каждая попытка — это существующее 5-буквенное слово.
* После каждой попытки буквы подсвечиваются цветами:

  * **Жёлтый (зелёный в оригинальной игре)** — буква на своём месте.
  * **Белый (жёлтый в оригинальной игре)** — буква есть в слове, но на другой позиции.
  * **Серый** — буквы в слове нет.
* Задача — угадать слово за шесть попыток, используя подсказки по цветам.

---

## Особенности

* Автоматическая фильтрация возможных слов на основе введённой подсказки.
* Отслеживание запрещённых и обязательных букв, а также ограничений по позициям.
* Отображение оставшихся возможных слов и ограничений по каждой позиции.
* Проверка корректности ввода русских букв и символов результата.
* Кнопка сброса для начала новой игры.

---

## Установка и запуск

1. Убедитесь, что у вас установлен Python версии 3.8 и выше.
2. Установите зависимости:

   ```bash
   pip install streamlit
   ```
3. Поместите файл `russian.txt` со списком слов в папку проекта (кодировка CP1251).
4. Запустите приложение:

   ```bash
   streamlit run app.py
   ```

---