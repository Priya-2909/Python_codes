import google.generativeai as genai
import os

genai.configure(api_key="")
model = genai.GenerativeModel("gemini-3.1-flash-lite-preview")
chat = model.start_chat(history=[])

print("CHATBOT (TYPE 'exit' TO QUIT)")
print("Welcome! You can start your chat")
while True:
    user_input=input("You: ")
    if user_input.lower() in ["exit","quit","bye"]:
        break
    response = chat.send_message(user_input)
    print(f"Idealabs:{response.text}")
