# Gen AI ft. CRM

This is a Python application to show generative AI used in a CRM.


## How it works

The application provides you with mock up CRM. The application uses Streamlit to create the GUI. It uses 
ChatGPT's complete webservice to query the LLM. API reference: https://platform.openai.com/docs/api-reference/chat/create


## Installation

To install the repository, please clone this repository, create a virtual environment and install the requirements:

```
git clone https://github.com/niels-oz/sample-genai.git
cd sample-genai
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

```
# activate venv (win)
.venv/Scripts/activate
```

To create an openAI API key goto https://platform.openai.com/account/api-keys. 

Create a `.env` file from the .env.example and insert your OpenAI API key.

## Usage (if you have Python installed)

To use the application, run the `app.py` file: 

```
streamlit run app.py
```

Alternative way (only requirement is Docker for Desktop)
```
docker-compose up
```

