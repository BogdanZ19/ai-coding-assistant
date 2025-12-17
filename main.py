import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import argparse
from config import SYSTEM_PROMPT
from functions import schema


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    if api_key is None:
        raise RuntimeError("API KEY NOT FOUND")

    # Get the prompt and arguments from the user
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    # Prepare to store conversations
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

    # Create the client and make a call with the provided prompt
    client = genai.Client(api_key=api_key)
    
    # Get response for the prompt
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=messages,
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_PROMPT,
            tools=[schema.available_functions],
            ),
    )

    # Get token counts
    prompt_tokens_count = 0
    response_tokens_count = 0
    
    if response.usage_metadata is not None:
        prompt_tokens_count = response.usage_metadata.prompt_token_count
        response_tokens_count = response.usage_metadata.candidates_token_count
    else:
        raise RuntimeError("Usage Metadata Not Available")

    # Console output:
    if args.verbose is True:
        print(f"\tUser prompt: {args.user_prompt}")
        print(f"\tPrompt tokens: {prompt_tokens_count}")
        print(f"\tResponse tokens: {response_tokens_count}\n")

    print("Response:")
    print(response.text)
    
    if response.function_calls is not None:
        for function_call in response.function_calls:
            print(f"Calling function: {function_call.name}({function_call.args})")
            


if __name__ == "__main__":
    main()
