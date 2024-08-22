import streamlit as st
import openai

# Initialize OpenAI API
openai.api_key = st.secrets["sk-E6pxB5UNVgyZpyn5HENtXO7VA3Ik15790fGKGCA8gGT3BlbkFJskFIg4VvK9tPZ0Q5e9xEx6JysBEAkkZd9wG6JZRksA"]

# Title of the web app
st.title("GPT-4 Streamlit App")

# Text input for the user
user_input = st.text_area("Enter your prompt here:")

# Button to generate the response
if st.button("Generate Response"):
    if user_input:
        # Call the OpenAI API to generate a response
        response = openai.Completion.create(
            engine="gpt-3.5",
            prompt=user_input,
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.7,
        )
        # Display the response
        st.write(response.choices[0].text.strip())
    else:
        st.write("Please enter a prompt.")

