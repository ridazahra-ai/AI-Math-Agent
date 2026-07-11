from agent import chat

print("Type exit or quit for exiting from this...")
while True:
    user_input = input("\nYou: ")

    if user_input.lower() in ["exit", "quit"]:
        break

    response = chat(user_input)

    print(f"\nAI: {response}")
