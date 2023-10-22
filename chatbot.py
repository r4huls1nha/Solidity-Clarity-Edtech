# chatbot.py
import os
from dotenv import load_dotenv
import openai
from converter import convert_solidity_to_clarity, walk_through_changes  # Add this line

# Load .env file
load_dotenv()

# Get API key from .env file
API_KEY = os.getenv('API_KEY')

# Initialize OpenAI with API key
openai.api_key = API_KEY

# Initialize chat model
chat_model = "text-davinci-002"  # Change this to the model you want to use

def chat_with_gpt4(prompt):
    """
    Function to chat with GPT-4 model.
    """
    # Get the response from the model
    response = openai.ChatCompletion.create(
        model=chat_model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )

    # Extract the message from the response
    message = response['choices'][0]['message']['content']

    return message

def handle_conversion(solidity_code):
    """
    Function to handle the conversion from Solidity to Clarity and explain the changes.
    """
    # Convert Solidity code to Clarity code
    clarity_code = convert_solidity_to_clarity(solidity_code)

    # Walk through the changes
    explanation = walk_through_changes(solidity_code, clarity_code)

    return clarity_code, explanation