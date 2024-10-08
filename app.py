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
        # Using the updated method for GPT-3.5-turbo
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_input}],
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.7,
        )
        # Display the response
        st.write(response['choices'][0]['message']['content'].strip())
    else:
        st.write("Please enter a prompt.")
