from backend.services import process_message

print("Chatbot iniciado! Digite 'sair' para encerrar.\n")

while True:
    try:
        msg = input("Você: ")
        if msg.lower() == "sair":
            print("Bot: Até mais 👋")
            break
        response = process_message(msg)
        print("Bot:", response)
    except KeyboardInterrupt:
        print("\n[INFO] Encerrando chatbot...")
        break
