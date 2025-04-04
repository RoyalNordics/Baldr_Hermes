import openai
import os
import logging

def call_openai_api(prompt: str):
    """
    Calls the OpenAI API with the given prompt and returns the response.
    Reads the API key from the environment variable OPENAI_API_KEY.
    """
    logger = logging.getLogger(__name__)
    openai.api_key = os.environ.get("OPENAI_API_KEY")

    if not openai.api_key:
        logger.error("OPENAI_API_KEY not found in environment variables.")
        return "API key not found. Please set the OPENAI_API_KEY environment variable."

    try:
        response = openai.Completion.create(
            engine="davinci",  # You can change the engine as needed
            prompt=prompt,
            max_tokens=150
        )
        return response.choices[0].text.strip()
    except Exception as e:
        logger.error(f"Error calling OpenAI API: {e}")
        return f"Error calling OpenAI API: {e}"