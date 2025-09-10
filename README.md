

<p align="center">
<img alt="Feito com" src="https://img.shields.io/badge/Feito%20com-Python-blue?style=for-the-badge&logo=python">
<img alt="Tecnologias" src="https://img.shields.io/badge/Tecnologias-Selenium%20%7C%20WebDriver-green?style=for-the-badge">
<img alt="Licença" src="https://img.shields.io/badge/Licença-MIT-red?style=for-the-badge">
</p>


## 💻 Sobre o Projeto

Este é um projeto de estudos para a criação de um bot que automatiza o envio de mensagens no WhatsApp Web. A aplicação utiliza Selenium para controlar o navegador e interagir com a interface da plataforma de forma automatizada.

-----

## 🛠️ Tecnologias

As seguintes ferramentas e tecnologias foram utilizadas na construção do projeto:

  * **Python 3.10+**
  * **Selenium**
  * **WebDriver Manager**

-----

## 🚀 Como Executar o Projeto

Siga os passos abaixo para rodar a aplicação em sua máquina local.

#### **Pré-requisitos**

Antes de começar, você vai precisar ter instalado em sua máquina:

  * [Git](https://git-scm.com)
  * [Python 3.8+](https://www.python.org/downloads/)
  * Google Chrome

#### **1. Clone o repositório**

```bash
git clone https://github.com/aldhemir/bot_whatsapp.git
cd bot_whatsapp
```

#### **2. (Recomendado) Crie e ative um ambiente virtual**

```bash
# Para Windows
python -m venv venv
.\venv\Scripts\activate
```

#### **3. Instale as dependências**

```bash
pip install -r requirements.txt
```

#### **4. Configure a mensagem e os contatos**

Abra o arquivo `zapbot.py` e edite as variáveis no bloco de execução principal, **ao final do arquivo**:

```python
# --- Bloco de Execução Principal ---
if __name__ == '__main__':
    # --- ÁREA DE CONFIGURAÇÃO ---
    contatos_alvo = ["Nome Exato do Contato 1", "Nome do Grupo 2"]
    mensagem_para_enviar = "Sua mensagem aqui."
    # ---------------------------

    # Cria a instância do bot e chama o método para enviar a mensagem
    bot = WhatsappBot()
    bot.send_message(contatos=contatos_alvo, mensagem=mensagem_para_enviar)
```

**Importante:** Os nomes na lista `contatos_alvo` devem ser idênticos aos que aparecem no seu WhatsApp.

#### **5. Execute a aplicação**

```bash
python zapbot.py
```

Ao executar, uma janela do Chrome abrirá. Escaneie o QR Code com seu celular para fazer login no WhatsApp Web. Após o login, o bot iniciará os envios.

-----

## 📸 Demonstração

\<p align="center"\>
\<img src="URL\_DO\_SEU\_GIF\_DE\_DEMONSTRAÇÃO\_AQUI.gif" alt="Demonstração do Bot"\>
\</p\>

-----

## ⚠️ Aviso Importante

Este projeto foi desenvolvido exclusivamente para **fins educacionais**. A automação de contas de usuário pode violar os **Termos de Serviço do WhatsApp**.

O uso indevido desta ferramenta para envio de spam, mensagens em massa ou qualquer outra atividade maliciosa é de **inteira responsabilidade do usuário**. O autor não se responsabiliza por qualquer consequência, incluindo, **bloqueio de contas** ou quaisquer outras perdas e danos. **Use por sua conta e risco.**

-----

## 📝 Licença

Este projeto está sob a licença [MIT](https://www.google.com/search?q=LICENSE).

-----

<p align="center">
Feito com ❤️ por <strong>Aldhemir</strong>
</p>
<p align="center">
<a href="https://github.com/aldhemir">
<img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/>
</a>
</p>
