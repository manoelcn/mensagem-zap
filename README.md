# 📲 Bot de Mensagens no WhatsApp com Call Me Bot

Este projeto é um simples bot em Python que utiliza a [API Call Me Bot](https://www.callmebot.com/blog/free-api-whatsapp-messages/) para enviar mensagens automáticas para um número pré-configurado no WhatsApp. 
O objetivo do projeto foi testar o funcionamento da [API Call Me Bot](https://www.callmebot.com/blog/free-api-whatsapp-messages/).

## 📌 Funcionalidades
- Enviar mensagens automáticas para um número previamente configurado.

## 🛠 Tecnologias Utilizadas
- Python
- Biblioteca `requests`
- Biblioteca `dotenv` para variáveis de ambiente
- API Call Me Bot

## 🚀 Como Rodar o Projeto
1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/mensagem-zap.git
   ```
2. Acesse o diretório do projeto:
   ```bash
   cd mensagem-zap
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
4. Crie um arquivo `.env` na raiz do projeto e adicione as seguintes variáveis:
   ```env
   PHONE=seu-numero
   API_KEY=sua-chave-da-api
   ```
5. Execute o script principal:
   ```bash
   python main.py
   ```

## ⚠️ Observação
- O projeto utiliza variáveis de ambiente para armazenar o número de telefone e a chave de API.
- É necessário obter a chave de [API do Call Me Bot](https://www.callmebot.com/blog/free-api-whatsapp-messages/) seguindo as instruções do site oficial.

---


