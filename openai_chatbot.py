from openai import OpenAI

client = OpenAI(api_key ="")

def start_chatbot() :
    messages = [{"role":"system","content ":"you are a helper and assistent "}]
    print("CHATBOT TYPE TO 'QUIT' to exit")

    while True:
        print("Hellooo how can i help you ?")
        user_input=input("You: ")
        if user_input.lower() in ["quit","exit","bye"]:
            break
        messages.append({"role":"user","content":user_input})
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            temperature=0.7
        )
        assistant_reply=response.choices[0].message.content
        print(f"Idealabs:{assistant_reply}")

        message.append({"role":"assiatant","content":assistant_reply})
if __name__ == "__main__":
    start_chatbot()
    
