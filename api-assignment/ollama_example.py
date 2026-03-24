import requests


# Ollama runs locally - no API key needed!
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3.2"  # Make sure you ran: ollama pull llama3.2


def get_ollama_response(prompt):
    """Query local Ollama model with a prompt."""
    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL,
                "prompt": prompt,
                "stream": False  # Get full response at once
            },
            timeout=120  # Local models can be slow on first run
        )

        if response.status_code == 404:
            return f"Error: Model '{MODEL}' not found. Run: ollama pull {MODEL}"

        if response.status_code != 200:
            return f"API Error {response.status_code}: {response.text}"

        data = response.json()
        return data.get("response", "No response returned.")

    except requests.exceptions.ConnectionError:
        return (
            "Error: Cannot connect to Ollama.\n"
            "Make sure Ollama is running by executing: ollama serve"
        )
    except requests.exceptions.Timeout:
        return "Error: Request timed out. Your model may still be loading, try again."
    except Exception as err:
        return f"Unexpected error: {err}"


def main():
    print("Ollama Local AI Program")


    prompt = input("\nEnter your prompt: ").strip()

    if not prompt:
        print("No prompt entered. Exiting.")
        return

    print("\nQuerying\n")

    result = get_ollama_response(prompt)

    print("AI Response:")
    print(result)


if __name__ == "__main__":
    main()