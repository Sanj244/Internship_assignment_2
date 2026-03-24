import os
from dotenv import load_dotenv
from google import genai
# Load environment variables from .env file
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")
# Initialize Gemini client
client = genai.Client(api_key=API_KEY)
MODEL = "gemini-2.0-flash"
def get_gemini_response(prompt):
    try:
        response = client.models.generate_content(
            model=MODEL,
            contents=prompt
        )
        return response.text

    except Exception as err:
        error_msg = str(err)
        if "API_KEY_INVALID" in error_msg or "401" in error_msg:
            return "Error: Invalid API key. Check your GOOGLE_API_KEY in .env"
        return f"Error: {error_msg}"
def main():
    print("     Google Gemini API Program")
    if not API_KEY:
        print("\nERROR: GOOGLE_API_KEY not found.")
        print("Add this to your .env file:")
        print("  GOOGLE_API_KEY=AIzaxxxxxxxxxxxxxxxx\n")
        return
    prompt = input("\nEnter your prompt: ").strip()
    if not prompt:
        print("No prompt entered. Exiting.")
        return
    print("\nQuerying Gemini API\n")
    result = get_gemini_response(prompt)
    print("AI Response:")
    print(result)



if __name__ == "__main__":
    main()
