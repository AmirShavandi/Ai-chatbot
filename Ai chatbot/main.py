from gpt4all import GPT4All


def start_chatbot():
    # 1. Load the model
    model_name = "Llama-3.2-1B-Instruct-Q4_0.gguf"
    print(f"[*] Initializing {model_name}...")

    try:
        model = GPT4All(model_name)
    except Exception as e:
        print(f"Error loading model: {e}")
        return

    print("\n" + "=" * 40)
    print(" AI CHATBOT SYSTEM ONLINE ")
    print(" (Type 'exit' or 'quit' to stop) ")
    print("=" * 40)

    # 2. Start a persistent chat session
    # This context manager handles the 'memory' of the conversation
    with model.chat_session():
        while True:
            user_input = input("\nYou: ")

            if user_input.lower() in ["exit", "quit", "bye"]:
                print("AI: Goodbye!")
                break

            # 3. Generate response
            # We don't manually add 'Context:' or 'Player:' here.
            # The chat_session handles the formatting for us.
            response = model.generate(
                user_input,
                max_tokens=200,
                temp=0.7,
                top_k=40
            )

            print(f"\nAI: {response}")


if __name__ == "__main__":
    start_chatbot()