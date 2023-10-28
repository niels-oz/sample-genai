ARG BASE_IMAGE=python:3.10
FROM $BASE_IMAGE AS base

RUN apt-get update -y && apt-get upgrade -y

WORKDIR /app

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY app.py .
COPY defaults.py .

# CMD streamlit run app/app.py --server.enableCORS=false --server.headless true --server.enableXsrfProtection false --browser.gatherUsageStats false
CMD streamlit run app.py --server.headless true --browser.gatherUsageStats false

EXPOSE 8501