import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()  # Load variables from .env
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-2.0-flash')


def app():
    print("Welcome to Gemini chat bot type 'exit'\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Good bye")
            break
        try:
            response = model.generate_content(user_input)
            print("Gemini: ", response.text)
        except Exception as e:
            print("Error", e)
if __name__ == "__main__" :
                app()