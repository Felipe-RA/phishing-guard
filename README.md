# Phishing Guard

![PhishingGuard_Uploaded_128x128_nobg](https://github.com/Felipe-RA/phishing-guard/assets/49454068/718f41b5-23a2-41d8-8848-d953885d68a9)

A browser extension to predict if a URL is phishing or not using an XGBoost model and the OpenAI API.

We trained with over 240K samples available in this paper. https://www.frontiersin.org/articles/10.3389/fcomp.2024.1308634/full

## How to use

[Screenshots of the app here guys]


# What can you find in this repo

## FastAPI Backend

You can find a simple FASTAPI Backend that will allow you to run predictions against our serialized model.

### Running the backend

## **How to use:**

1. Install

    ```bash
    sudo apt install uvicorn
    ```

    ```bash
    pip install requirements.txt
    ```

2. Run to launch the app

    ```bash
    uvicorn app:app --reload
    ```
3. To install the extension go to releases and follow the steps there.
## Endpoints
All  endpoints just allow POST requests
Send a POST request to /predict/: (We are using curl here, but if you guys have Postman that's also valid)

    ```bash
    curl -X 'POST' \
    'http://127.0.0.1:8000/predict/' \
    -H 'accept: application/json' \
    -H 'Content-Type: application/json' \
    -d '{
    "url": "https://example.com"
    }'
    ```
    You should get a response like:

    ```JSON
    {"probability":"24.971%","classification":"not phishing"}
    ```
Send a POST request to /url-assistant/. Here the percentage has to be the one  you get from  /predict/ and should be type float: 

    ```bash
    curl -X 'POST' \
    'http://127.0.0.1:8000/url-assistant/' \
    -H 'accept: application/json' \
    -H 'Content-Type: application/json' \
    -d '{
    "url": "https://example.com",
    "percentage": 35.4
    }'
    ```
Send a POST request to /url-message/: 

    ```bash
    curl -X 'POST' \
    'http://127.0.0.1:8000/url-message/' \
    -H 'accept: application/json' \
    -H 'Content-Type: application/json' \
    -d '{
    "message": "Hi, How It is going?"
    }'
    ```
## A notebook showing how are we structuring our OPENAI Usage

- Available at [openai_gpt_4_API.ipynb](/openai_gpt_4_API.ipynb)

## A bunch of Notebooks showcasing how we trained our model and preprocessed each input before predicting

- Available at [openai_gpt_4_API.ipynb](/openai_gpt_4_API.ipynb)
- Available at [00_model_training.ipynb](/00_model_training.ipynb)
- Available at [01_input_url_preprocessing.ipynb](/01_input_url_preprocessing.ipynb)
- Available at [02_serving_model_through_api.ipynb](/02_serving_model_through_api.ipynb)
