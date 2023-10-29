from dotenv import load_dotenv
import streamlit as st
import os
import openai

from defaults import MODEL, SYSTEM_ROLE, SAMPLE_DATA, SAMPLE_TASK


def get_completion(task, content, role=SYSTEM_ROLE, model=MODEL, top_p=1.0, stop=None, temperature=0,
                   frequency_penalty=0, presence_penalty=0):
    prompt = f'{task} \n\n Content: """{content}"""'
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
    return response.choices[0].message['content']


# sets env vars as defined in .env
_ = load_dotenv()
openai.api_key = os.environ['OPENAI_API_KEY']

# Initializing session state variables
if 'response' not in st.session_state:
    st.session_state['response'] = {}

st.set_page_config(layout='wide')
st.markdown(
    '<style>.block-container {padding-top: 3rem;padding-bottom: 0rem;padding-left: 5rem;padding-right: 5rem;}</style>',
    unsafe_allow_html=True)

st.title('Sample GenAI infused CRM')
customer_number = st.sidebar.selectbox(label='Select customer:', options=SAMPLE_DATA.keys())
customer_name = SAMPLE_DATA.get(customer_number).get('name')

st.subheader(f'customer: {customer_number}, {customer_name}')

CALL_HISTORY = SAMPLE_DATA.get(customer_number).get('call')
CHAT_HISTORY = SAMPLE_DATA.get(customer_number).get('chat')
EMAIL_HISTORY = SAMPLE_DATA.get(customer_number).get('email')

task = st.text_area('Task:', value=SAMPLE_TASK, height=160)

if st.button('Process'):
    response = get_completion(task=task,
                              content=f'calls: {CALL_HISTORY} \n\n chats: {CHAT_HISTORY} \n\n emails: {EMAIL_HISTORY}',
                              role=SYSTEM_ROLE, model=MODEL)
    st.session_state['response'][customer_number] = response

st.write(st.session_state['response'].get(customer_number))

col1, col2, col3 = st.columns(3)

with col1.expander('call history'):
    st.write(CALL_HISTORY)

with col2.expander('chat history'):
    st.write(CHAT_HISTORY)

with col3.expander('email history'):
    st.write(EMAIL_HISTORY)
