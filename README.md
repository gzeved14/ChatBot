# ChatBot


# 🤖 ChatBot com Backend Python e Frontend Web

## 🌟 Visão Geral do Projeto

Este projeto implementa um sistema de ChatBot utilizando Python no Backend (com lógica de Processamento de Linguagem Natural - PLN, OpenAI ou dados customizados) e uma interface Web simples no Frontend (HTML/JS). O objetivo principal é fornecer uma base funcional e escalável para aplicações conversacionais.

---

## ⚙️ Tecnologias Utilizadas

<<<<<<< HEAD
| Componente | Tecnologia | Detalhes |
| :---------------- | :----------------------------------- | :-------------------------------------------------------------------- |
| **Backend** | Python | Lógica principal, serviços, rotas e banco de dados. |
| **Framework Web** | FastAPI / Flask (a ser definido) | Serviço RESTful para comunicação. |
| **Database** | MongoDB (via URI de Atlas) | Armazenamento de dados do chatbot (ex: histórico de conversas, logs). |
| **Frontend** | HTML5, CSS3, JavaScript | Interface de chat embutida. |
| **PLN/IA** | OpenAI API / Dados em `intents.json` | Motor de inteligência do chatbot. |
=======
| Componente | Tecnologia | Detalhes |
| :--- | :--- | :--- |
| **Backend** | Python | Lógica principal, serviços, rotas e banco de dados. |
| **Framework Web** | FastAPI / Flask (a ser definido) | Serviço RESTful para comunicação. |
| **Database** | MongoDB (via URI de Atlas) | Armazenamento de dados do chatbot (ex: histórico de conversas, logs). |
| **Frontend** | HTML5, CSS3, JavaScript | Interface de chat embutida. |
| **PLN/IA** | OpenAI API / Dados em `intents.json` | Motor de inteligência do chatbot. |

> > > > > > > 1ffd495fda3952c4e9d0039429255b224da482cf

---

## 🚀 Como Rodar o Projeto Localmente

Siga os passos abaixo para configurar e executar o projeto em sua máquina.

### Pré-requisitos

Você precisa ter instalado em sua máquina:
<<<<<<< HEAD

- [Python 3.x](https://www.python.org/downloads/)
- # [Git](https://git-scm.com/downloads)

* [Python 3.x](https://www.python.org/downloads/)
* [Git](https://git-scm.com/downloads)
  > > > > > > > 1ffd495fda3952c4e9d0039429255b224da482cf

### 1. Clonar o Repositório

```bash
git clone [https://github.com/gzeved14/ChatBot.git](https://github.com/gzeved14/ChatBot.git)
cd ChatBot
<<<<<<< HEAD
```
````

### 2\. Configurar o Ambiente Virtual

É altamente recomendável usar um ambiente virtual para isolar as dependências do projeto.

```bash
# Cria o ambiente virtual (venv ou .venv)
python -m venv .venv

# Ativa o ambiente virtual (Windows - PowerShell/CMD)
# .venv\Scripts\Activate

# Ativa o ambiente virtual (Linux/macOS ou Git Bash)
source .venv/bin/activate
```

### 3\. Instalar as Dependências

Instale todas as bibliotecas Python necessárias (assumindo que você terá um arquivo `requirements.txt`).

```bash
pip install -r requirements.txt
```

### 4\. Configurar Variáveis de Ambiente

Crie o arquivo de configuração de ambiente na pasta `backend/` baseado no template.

1.  Copie o arquivo de exemplo:

    ```bash
    cp backend/.env.example backend/.env
    ```

2.  **Preencha o arquivo `backend/.env`** com suas chaves de API e credenciais reais (MongoDB URI, `OPENAI_API_KEY`, etc.).

    **_ATENÇÃO: Este arquivo (.env) é ignorado pelo Git e nunca deve ser commitado._**

### 5\. Executar o Backend

Inicie o servidor de Backend:

```bash
# Exemplo de comando de execução do arquivo principal
python backend/main.py
```

_A porta do servidor será exibida no console (ex: https://www.google.com/search?q=http://127.0.0.1:8000)._

### 6\. Acessar o Frontend

Abra o arquivo `frontend/index.html` em seu navegador para interagir com o ChatBot. O JavaScript (`frontend/chat.js`) se conectará automaticamente à API rodando no Backend.

---

## 📂 Estrutura do Projeto

A estrutura de diretórios principal é organizada da seguinte forma:

```
.
├── backend/
│   ├── .env.example       # Template para configurações de ambiente
│   ├── chatbot/           # Lógica do Chatbot
│   │   ├── intents.json   # Dados/Intenções do Chatbot
│   │   └── nlp.py         # Módulo de Processamento de Linguagem
│   ├── main.py            # Ponto de entrada do Backend
│   ├── routes.py          # Definições de API/Rotas
│   └── services.py        # Módulos de serviço (DB, API, etc.)
├── frontend/
│   ├── index.html         # Página principal do Chat
│   └── chat.js            # Lógica de comunicação com o Backend
├── .gitignore             # Arquivos e pastas ignorados
└── README.md              # Documentação do projeto (este arquivo)
```

---

## 🤝 Contribuição

Sinta-se à vontade para sugerir melhorias, reportar _bugs_ ou contribuir com código.

1.  Crie um Fork do projeto.
2.  Crie um novo _branch_ (`git checkout -b feature/sua-feature`).
3.  Faça suas alterações e _commits_.
4.  Envie suas alterações (`git push origin feature/sua-feature`).
5.  Abra um _Pull Request_.

---
