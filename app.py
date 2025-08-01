import streamlit as st
from logic import WordleAssistant

st.set_page_config(page_title="Russian Wordle Helper", layout="centered")

st.title("5-Letter Word Game Assistant")
assistant = st.session_state.get("assistant")

if assistant is None:
    assistant = WordleAssistant()
    st.session_state.assistant = assistant

st.markdown("Enter a 5-letter word and slot colors: yellow (y), white (w), gray (g)")

with st.form("guess_form", clear_on_submit=True):  # clear form after submission
    guess = st.text_input("Word (5 letters)", max_chars=5).strip().lower()
    result = st.text_input("Result (e.g., `ywgww`)", max_chars=5).strip().lower()
    submitted = st.form_submit_button("Apply")

if submitted:
    error = assistant.process_input(guess, result)
    if error:
        st.error(error)
    else:
        st.success(f"Input accepted: {guess} [{result}]")

if assistant.iteration > 1:
    st.markdown("---")
    st.subheader(f"Iteration {assistant.iteration - 1}")
    st.markdown("### Position constraints:")
    for i in range(5):
        st.markdown(
            f"**Position {i+1}**: {' '.join(sorted(assistant.possible_letters[i]))}"
        )

    st.markdown(f"**Gray letters**: `{', '.join(sorted(assistant.banned_letters))}`")
    st.markdown(
        f"**Required letters**: `{', '.join(sorted(assistant.required_letters))}`"
    )
    st.markdown(f"**Possible words left**: {len(assistant.filtered_words)}")
    st.text_area("Possible words", ", ".join(assistant.filtered_words), height=200)

    if assistant.is_solved():
        st.success(f"Word solved: {assistant.get_final_word()}")

st.button("Reset", on_click=lambda: st.session_state.pop("assistant", None))
