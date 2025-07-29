from gpt4all import GPT4All

model = GPT4All("mistral-7b-instruct-v0.1.Q4_0.gguf") # Change name if needed

print("✅ AI is ready. Type a question. Type 'exit' to stop.")

while True:
    prompt = input("You: ")
    if prompt.lower() == "exit":
        break
    response = model.generate(prompt)
    print("AI:", response)

