import os
from dotenv import load_dotenv
from google import genai
import argparse

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    model = "gemini-2.5-flash"
    
    if api_key is None:
        raise RuntimeError("API KEY NOT FOUND")
    
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    args = parser.parse_args()
    
    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(model=model, contents=args.user_prompt);
    
    if response.usage_metadata is not None:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}\nResponse tokens: {response.usage_metadata.candidates_token_count}\n")
    else:
        raise RuntimeError("Usage Metadata Not Available")
    
    print(response.text)


if __name__ == "__main__":
    main()
