import streamlit as st
import random

st.title("Bano Qabil 2.0")

# List of scrambled sentences
sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is a high-level programming language.",
    "Streamlit is an open-source app framework for Machine Learning and Data Science.",
    "Artificial Intelligence is shaping the future of technology.",
    "Data visualization is an important skill for data scientists."
]

# Function to scramble the words in a sentence
def scramble_sentence(sentence):
    words = sentence.split()
    random.shuffle(words)
    return " ".join(words)

# Function to check if the user's answer is correct
def check_answer(original_sentence, user_answer):
    return original_sentence == user_answer

def main():
    st.sidebar.title("Navigation")
    tab = st.sidebar.radio("", ["Home", "About us", "Contact us"])

    if tab == "Home":
        st.image("https://images.app.goo.gl/s7FbDervZkpWYfSM7", use_column_width=True)
    elif tab == "About us":
        st.title("About Us")
        st.markdown("Team Name: Pythonic Innovators\n\nTeam Members:\n\nTeam Leader: Syed Muhammad Shujaat Ali\nMember: Abdul Rahman\nMember: Anus Khan\n\nProject Description:\nThe final project submit in Bano Qabil 2.0\nBy Python coding robust puzzle game using Python.")
    elif tab == "Contact us":
        st.title("Contact Us")
        st.write("Email: shujju.sjt6969@gmail.com")       

    st.title("Puzzle Game")

    # Select a random sentence from the list
    sentence = random.choice(sentences)
    scrambled_sentence = scramble_sentence(sentence)

    st.write("Unscramble the sentence:")
    st.write(scrambled_sentence)

    user_answer = st.text_input("Your Answer")

    if st.button("Check Answer"):
        if check_answer(sentence, user_answer):
            st.success("Congratulations! Your answer is correct.")
        else:
            st.error("Sorry, your answer is incorrect. Please try again.")

if __name__ == "__main__":
    main()
