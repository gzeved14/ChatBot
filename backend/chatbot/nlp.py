# nlp.py
import json
import re
import random
import logging
import os
import openai

logging.basicConfig(level=logging.WARNING, format='[%(levelname)s] %(message)s')


class SimpleNLP:
    def __init__(self, intents_file: str = "intents.json"):
        """
        Inicializa o NLP carregando as intenções do arquivo JSON.
        """
        self.intents = []
        self.fallback_responses = [
            "Desculpe, não entendi.",
            "Pode reformular sua pergunta?",
            "Não tenho certeza do que quis dizer."
        ]

        dir_path = os.path.dirname(__file__)
        intents_path = os.path.join(dir_path, intents_file)

        try:
            with open(intents_path, "r", encoding="utf-8") as file:
                self.intents = json.load(file).get("intents", [])
            logging.info(f"Intents carregadas: {len(self.intents)}")
        except FileNotFoundError:
            logging.error(f"Arquivo '{intents_path}' não encontrado.")
        except json.JSONDecodeError:
            logging.error(f"Erro ao decodificar o JSON em '{intents_path}'.")

    def find_intent_and_response(self, user_message: str) -> str:
        """
        Encontra a intenção da mensagem do usuário e retorna uma resposta.
        Retorna uma resposta de fallback se nenhuma correspondência for encontrada.
        """
        message = user_message.strip()
        if not message:
            return random.choice(self.fallback_responses)

        for intent in self.intents:
            for pattern in intent.get("patterns", []):
                try:
                    if re.search(pattern, message, re.IGNORECASE):
                        responses = intent.get("responses", [])
                        if responses:
                            return random.choice(responses)
                except re.error as e:
                    logging.warning(f"Erro no regex '{pattern}': {e}")

        return random.choice(self.fallback_responses)


class AdvancedNLP(SimpleNLP):
    def __init__(self, intents_file: str = "intents.json"):
        super().__init__(intents_file)
        self.api_key = os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            logging.warning("Variável OPENAI_API_KEY não configurada. IA não funcionará.")
        openai.api_key = self.api_key

    def find_intent_and_response(self, user_message: str) -> str:
        """
        Primeiro tenta NLP tradicional (SimpleNLP).
        Se cair no fallback, envia para a API da OpenAI.
        """
        nlp_response = super().find_intent_and_response(user_message)

        # Se for resposta de fallback e tiver API Key, tenta IA
        if nlp_response in self.fallback_responses and self.api_key:
            try:
                ai_response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": user_message}]
                )
                return ai_response.choices[0].message.content
            except openai.OpenAIError as e:
                logging.error(f"Erro OpenAI: {e}")
                return "Desculpe, não consegui entender sua mensagem."

        return nlp_response


# Exemplo de uso via console
if __name__ == "__main__":
    nlp = AdvancedNLP()
    print("Chatbot iniciado! Digite 'sair' para encerrar.\n")

    while True:
        msg = input("Você: ")
        if msg.lower() in ["sair", "quit", "exit"]:
            print("Bot: Até mais! 👋")
            break
        response = nlp.find_intent_and_response(msg)
        print("Bot:", response)
