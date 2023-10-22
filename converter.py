# converter.py
import os
from dotenv import load_dotenv
import openai  # Change this line

# Load .env file
load_dotenv()

# Get API key from .env file
API_KEY = os.getenv('API_KEY')

# Initialize OpenAI with API key
openai.api_key = API_KEY  # Change this line

# Initialize chat model
chat_model = "gpt-4"

# Rest of the code remains the same

def convert_solidity_to_clarity(solidity_code):
    """
    Function to convert Solidity code to Clarity code using OpenAI's GPT-4 model.
    """
    # Prepare the prompt
    prompt = f"Translate the following Solidity code to Clarity code:\n\n{solidity_code}\n"

    # Get the response from the model
    response = openai.ChatCompletion.create(
        model=chat_model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )

    # Extract the translated code from the response
    clarity_code = response['choices'][0]['message']['content']

    return clarity_code

def walk_through_changes(solidity_code, clarity_code):
    """
    Function to walk the developer through the changes made in the conversion from Solidity to Clarity.
    """
    # Prepare the prompt
    prompt = f"Explain the changes made in the conversion from the following Solidity code to Clarity code:\n\nSolidity:\n{solidity_code}\n\nClarity:\n{clarity_code}\n"

    # Get the response from the model
    response = openai.ChatCompletion.create(
        model=chat_model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )

    # Extract the explanation from the response
    explanation = response['choices'][0]['message']['content']

    return explanation
