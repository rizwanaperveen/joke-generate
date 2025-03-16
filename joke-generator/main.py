import streamlit as st
import requests

def get_joke():
    """Get a random joke from the Joke API."""
    try:
        response = requests.get("https://official-joke-api.appspot.com/random_joke")
       
        if response.status_code == 200:
            joke_data = response.json()
            return f"{joke_data['setup']} \n\n {joke_data['punchline']}"
        else:
            return "Failed to fetch a joke."
    except:
        return "Why did the programmer quit his job? Because he didn't get arrays!"

def main():
    st.title("😁Random Joke Generator😁")
    st.write("😁🤣Click the button below to generate a random Joke😁🤣")

    if st.button("👉🏻Generate a Joke!"):
        joke = get_joke()
        st.success(joke)
        st.divider()

        st.markdown(
            """
        <div style='text-align: center; color: #FF69B4; font-size: 20px;'>
            <p>😁Joke from Official Joke API🤣</p>
            <p>Build with ❤️ by <a href="https://github.com/RizwanaPerveen">RIZWANA PERVEEN</a> using streamlit and python.
        </div>
""",
             unsafe_allow_html=True
        )
if __name__ == "__main__":
    main()