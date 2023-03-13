# Install dependencies

# Import dependencies
import openai
import streamlit as st

# Set the OpenAI secret key
openai.api_key = st.secrets['pass']

st.header('AI Analysis Report Generator')
st.subheader('current version : beta 0.1')

# Set the if, else loop including prompt
article_text = st.text_area('Please enter the text material or URL you would like to generate a report from')
if len(article_text) > 5:
    temp = st.slider("temperature", 0.2, 0.5, 0.8)
    if st.button ('Generate Report'):
        response = openai.Completion.create(
            engine = "text-davinci-003",
            prompt = "Create a summary analysis. The summary should be written in a formal tone, capture major points and all key details and should not repeat any information between or within sections. It should provide accurate information, with short concise descriptions for all data points and their implications. The target use for the summary will be to compile with other summary data for a report. Use only the text information located here: " + article_text,
            max_tokens = 3000,
            presence_penalty=0.8,
            frequency_penalty=0.6,
            temperature = temp
        )
        res = response["choices"][0]["text"]
        st.info(res)

        st.download_button("Download result", res)
else: st.warning("The supplied information is not large enough")
