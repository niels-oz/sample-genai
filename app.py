from dotenv import load_dotenv
import streamlit as st
import json
from datetime import datetime
import os
import openai

# from defaults import MODEL, , EXAMPLE_CONTENT, EXAMPLE_TASK

from data import SAMPLE_DATA

# defaults
MODEL = 'gpt-3.5-turbo'
SYSTEM_ROLE = '''Use the provided content delimited by triple quotes to answer questions. If the answer cannot be \
found in the content, write "I could not find an answer."'''


def get_completion(user_prompt, user_content, role=SYSTEM_ROLE, model=MODEL, top_p=1.0, stop=None, temperature=0,
                   frequency_penalty=0, presence_penalty=0):
    prompt = f'{user_prompt} \n\n Content: """{user_content}"""'
    messages = [{'role': 'system', 'content': role}, {'role': 'user', 'content': prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
        top_p=top_p,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty,
        stop=stop,
    )
    print(response)
    return locals(), response.choices[0].message['content']


# sets env vars as defined in .env
_ = load_dotenv()
openai.api_key = os.environ['OPENAI_API_KEY']


st.set_page_config(layout='wide')
# st.markdown('<style>#MainMenu {visibility: hidden;} footer {visibility: hidden;}</style>', unsafe_allow_html=True)
st.markdown('<style>button {height: auto;padding-top: 10px !important;padding-bottom: 10px !important;}</style>',
            unsafe_allow_html=True,)

st.title('Sample GenAI infused CRM')
customer_number = st.sidebar.selectbox(label='Select customer:', options=SAMPLE_DATA.keys())
customer_name = SAMPLE_DATA.get(customer_number).get('name')

st.subheader(f'customer: {customer_number}, {customer_name}')

CALL_HISTORY = SAMPLE_DATA.get(customer_number).get('call')
CHAT_HISTORY = SAMPLE_DATA.get(customer_number).get('chat')
EMAIL_HISTORY = SAMPLE_DATA.get(customer_number).get('email')

# st.write(f'customer: {customer_number}')

col1, col2, col3 = st.columns(3)

with col1.expander('call history'):
    st.write(CALL_HISTORY)

with col2.expander('chat history'):
    st.write(CHAT_HISTORY)

with col3.expander('email history'):
    st.write(EMAIL_HISTORY)


