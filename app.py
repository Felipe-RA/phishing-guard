from fastapi import FastAPI, HTTPException
import os
from joblib.memory import asyncio
from openai import OpenAI
import requests
from fastapi.middleware.cors import CORSMiddleware
import joblib
import pandas as pd
from pydantic import BaseModel
from data_preprocessing import preprocess_url_features
from dotenv import load_dotenv
# Define a data model for input data validation (we are just checking a str here)
load_dotenv()
class url_body(BaseModel):
    url: str
class url_body_openAi(BaseModel):
    percentage: float
    url: str
class message_body_openAi(BaseModel):
    message: str
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can specify a list of allowed origins here
    allow_credentials=True,
    allow_methods=["*"],  # You can specify allowed HTTP methods here
    allow_headers=["*"],  # You can specify allowed HTTP headers here
)
# Load the pre-trained model
model = joblib.load('phishing_probability_predictor_model.pkl')

def call_openai_api(content: str, api_key: str, assistant_id: str):
    
    try:
        # REMOVE REMOVE BEFORE PRODUCTION AND ADD TO ENVIRONMENT VARIABLES
        client = OpenAI(api_key=api_key )

        # Retrieve our existing assistant (This is public)
        assistant_id = assistant_id  #  assistant's ID

        # Step 1: Retrieve the Assistant by ID
        assistant = client.beta.assistants.retrieve(assistant_id)
        message = ""
        # Step 2: Create a Thread (we cant use assistants without a thread)
        # A THREAD is a bunch of messages that signalize a conversation
        thread = client.beta.threads.create()

        # Step 3: Add a Message to the Thread 
        # a message must have the thread id, the role (user or assistant) and the content (the message itself)
        message = client.beta.threads.messages.create(
            thread_id=thread.id,
            role="user",
            content=content
        )

        # Step 4: Create and poll a Run to generate a response from the assistant
        run = client.beta.threads.runs.create_and_poll(
            thread_id=thread.id,
            assistant_id=assistant.id
            )
        message = ''
        # Step 5: Once the Run completes, retrieve the assistant's messages
        if run.status == 'completed':
            messages = client.beta.threads.messages.list(thread_id=thread.id)
            for message in messages.data:
                if message.role == 'assistant':  # Look for messages from the assistant
                    test_structure = message.content
                    # Access the first TextContentBlock in the list
                    content_block = test_structure[0]

                    text_object = content_block.text

                    # Access the 'value' property from the Text object
                    message = text_object.value
                    print(message)
                    break
            asyncio.create_task(delete_thread(thread.id))

            return message

        else:
            print(f"Run status: {run.status}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/predict/")
async def predict_phishing(data: url_body):
    # Preprocess the URL to extract features
    try:
        features = preprocess_url_features(data.url)
        features_df = pd.DataFrame([features])
        predictions = model.predict_proba(features_df)[:, 1] 
        phishing_probability = predictions[0] * 100.
        is_phishing = "phishing" if phishing_probability >= 70.0 else "not phishing"
        return {"probability": f"{phishing_probability:.1f}%", "classification": is_phishing}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/url-assistant/")
async def openai_url(openAi_url_body: url_body_openAi ):
    try:
        content_call = f"[URL]{openAi_url_body.url}\n[PERCENTAGE]{openAi_url_body.percentage}"
        response_message = call_openai_api(content_call, os.getenv("FELIPE_API_KEY", ""), os.getenv("FELIPE_ASSISTANT_ID", ""))
        return { "data": response_message }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/message-assistant/")
async def openai_message(openAi_message_body: message_body_openAi):
    try:
        content_call =  f"[BODY_MESSAGE]{openAi_message_body.message}"
        api_key = os.getenv("SERGIO_API_KEY", "")
        print(api_key)
        response_message = call_openai_api(content_call, os.getenv("SERGIO_API_KEY", ""), os.getenv("SERGIO_ASSISTANT_ID", ""))
        return { "data": response_message }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
async def delete_thread(thread_id):
    try:
        headers = {
            'Authorization': f'Bearer {os.getenv("FELIPE_API_KEY", "")}',
            'Content-Type': 'application/json',
            'OpenAI-Beta': 'assistants=v2'
        }

        response = requests.delete(f'https://api.openai.com/v1/threads/{thread_id}', headers=headers)
        if response.status_code == 200:
            print("Thread deleted successfully:", response.json())
        else:
            print("Failed to delete thread:", response.json())
    except Exception as e:
        print("Error deleting thread:", str(e))


