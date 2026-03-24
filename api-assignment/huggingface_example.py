import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()

API_KEY = os.getenv("HUGGINGFACE_API_KEY")
MODEL = "deepseek-ai/DeepSeek-V3-0324"


def get_huggingface_response(prompt):
    """Query Hugging Face Inference API using InferenceClient."""
    try:
        client = InferenceClient(
            api_key=API_KEY,
            provider="auto",
        )

        completion = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=500,
        )

        return completion.choices[0].message.content

    except Exception as err:
        error_msg = str(err)

        # Try fallback model if first one fails
        if "not found" in error_msg.lower() or "404" in error_msg:
            return try_fallback(prompt)

        return f"Error: {error_msg}"


def try_fallback(prompt):
    """Try a fallback model if primary model fails."""
    fallback_model = "meta-llama/Llama-3.2-3B-Instruct"
    print(f"Primary model unavailable. Trying fallback: {fallback_model}")
    try:
        client = InferenceClient(api_key=API_KEY)
        completion = client.chat.completions.create(
            model=fallback_model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500,
        )
        return completion.choices[0].message.content
    except Exception as err2:
        return f"Both models failed.\nError: {err2}"


def main():
    print("     Hugging Face API Program")


    if not API_KEY:
        print("\nERROR: HUGGINGFACE_API_KEY not found.")
        print("Add this to your .env file:")
        print("  HUGGINGFACE_API_KEY=hf_xxxxxxxxxxxx\n")
        return

    prompt = input("\nEnter your prompt: ").strip()

    if not prompt:
        print("No prompt entered. Exiting.")
        return

    print("\nQuerying Hugging Face API\n")

    result = get_huggingface_response(prompt)

    print("AI Response:")
    print(result)



if __name__ == "__main__":
    main()