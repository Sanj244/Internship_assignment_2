import os
from dotenv import load_dotenv
from google import genai

# Load environment variables from .env file
load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY")

# Initialize Gemini client
client = genai.Client(api_key=API_KEY)

MODEL = "gemini-2.0-flash"

HARDCODED_RESPONSE = """At its core, engineering is the practical application of science, mathematics, and creativity to solve problems and design systems, structures, or machines. While a scientist seeks to understand why the natural world works the way it does, an engineer asks, "How can I use that understanding to build something useful?"

The Core Pillars of Engineering:
- Design & Innovation: Creating something that didn't exist before.
- Analysis: Using mathematical models and physics to predict how a design will behave.
- Constraints: Designing under pressure — budget, safety, materials, and environment.

The Major Disciplines:
- Civil: Bridges, skyscrapers, water systems.
- Mechanical: Engines, robotics, HVAC systems.
- Electrical: Power grids, microchips, smartphones.
- Chemical: Refining fuel, medicine, food processing.
- Software/Computer: Operating systems, AI models, networking.

Engineering is ultimately about stewardship — taking the resources of the earth and the laws of the universe to improve the human condition."""


def get_gemini_response(prompt):
    """Query Google Gemini API with a prompt."""
    try:
        response = client.models.generate_content(
            model=MODEL,
            contents=prompt
        )
        return response.text

    except Exception as err:
        error_msg = str(err)

        if "quota" in error_msg.lower() or "429" in error_msg:
            # Return hardcoded response when quota is exhausted
            return HARDCODED_RESPONSE

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