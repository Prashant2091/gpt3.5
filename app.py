import streamlit as st
import openai

# Initialize OpenAI API using the key
openai.api_key = st.secrets["open_api_key"]
# Title of the web app
st.title("GPT-3.5 Streamlit App")

# Text input for the user
user_input = st.text_area("Enter your prompt here:")

# Button to generate the response
if st.button("Generate Response"):
    if user_input:
        response = openai.Completion.create(
            engine="gpt-3.5-turbo",
            prompt=user_input,
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.7,
        )
        st.write(response.choices[0].text.strip())
    else:
        st.write("Please enter a prompt.")
