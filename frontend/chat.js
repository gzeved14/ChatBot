// chat.js
document.addEventListener('DOMContentLoaded', () => {
    // Referências para os elementos do DOM
    const messagesEl = document.getElementById('messages');
    const userInput = document.getElementById('userInput');
    const sendBtn = document.getElementById('sendBtn');

    // URL da API backend. Para este exemplo, estamos usando a porta padrão do FastAPI.
    const API_URL = "http://localhost:8000";

    // Função para adicionar uma mensagem ao chat
    function addMessage(message, isUser = false) {
        const messageWrapper = document.createElement('div');
        const messageContent = document.createElement('div');

        messageWrapper.classList.add('flex', isUser ? 'justify-end' : 'justify-start');
        messageContent.classList.add('p-3', 'rounded-lg', 'max-w-[80%]');
        messageContent.textContent = message;

        if (isUser) {
            messageContent.classList.add('bg-blue-500', 'text-white');
        } else {
            messageContent.classList.add('bg-gray-200', 'text-gray-800');
        }

        messageWrapper.appendChild(messageContent);
        messagesEl.appendChild(messageWrapper);

        // Rola para a última mensagem
        messagesEl.scrollTop = messagesEl.scrollHeight;
    }

    // Função para enviar a mensagem para a API
    async function sendMessage() {
        const message = userInput.value.trim();
        if (!message) return;

        // Adiciona a mensagem do usuário na tela
        addMessage(message, true);
        userInput.value = '';

        try {
            // Requisição POST para o backend
            const response = await fetch(`${API_URL}/chat`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ message: message })
            });

            if (!response.ok) {
                throw new Error(`Erro de rede: ${response.status}`);
            }

            const data = await response.json();
            // Adiciona a resposta do chatbot na tela
            addMessage(data.response, false);

        } catch (error) {
            console.error('Erro ao comunicar com a API:', error);
            addMessage('Ocorreu um erro ao tentar obter a resposta do chatbot.', false);
        }
    }

    // Event listeners para enviar a mensagem
    sendBtn.addEventListener('click', sendMessage);
    userInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            sendMessage();
        }
    });
});
