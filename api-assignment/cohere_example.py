import os
from dotenv import load_dotenv
import cohere
# Load environment variables
load_dotenv()
# Initialize Cohere client
co = cohere.Client(os.getenv("COHERE_API_KEY"))
def get_cohere_response(prompt):
    try:
        response = co.chat(
            model="command-a-03-2025",
            message=prompt
        )
        return response.text
    except Exception as err:
        return f"Error occurred: {err}"
def main():
    print("\nCohere API Program")
    prompt = input("Enter your prompt: ")
    print("\nGenerating\n")
    result = get_cohere_response(prompt)
    print("AI Response:\n")
    print(result)
if __name__ == "__main__":
    main()
