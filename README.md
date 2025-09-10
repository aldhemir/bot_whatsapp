

<p align="center">
<img alt="Feito com" src="https://img.shields.io/badge/Feito%20com-Python-blue?style=for-the-badge&logo=python">
<img alt="Tecnologias" src="https://img.shields.io/badge/Tecnologias-Selenium%20%7C%20WebDriver-green?style=for-the-badge">
<img alt="Licença" src="https://img.shields.io/badge/Licença-MIT-red?style=for-the-badge">
</p>

💻 Sobre o Projeto

Este é um projeto de estudos para a criação de um bot que automatiza o envio de mensagens no WhatsApp Web. A aplicação utiliza Selenium para controlar o navegador e interagir com a interface da plataforma de forma automatizada.

🛠️ Tecnologias

As seguintes ferramentas e tecnologias foram utilizadas na construção do projeto:

Python 3.10+

Selenium

WebDriver Manager

🚀 Como Executar o Projeto

Siga os passos abaixo para rodar a aplicação em sua máquina local.

Pré-requisitos

Antes de começar, você vai precisar ter instalado em sua máquina:

Git

Python 3.8+

Google Chrome


1. Clone o repositório
Bash

git clone https://github.com/aldhemir/bot_whatsapp.git
cd bot_whatsapp

2. (Opcional) Crie e ative um ambiente virtual
Bash

# Para Windows
python -m venv venv
.\venv\Scripts\activate


3. Instale as dependências
Bash

pip install -r requirements.txt


4. Configure a mensagem e os contatos
Abra o arquivo bot/bot.py. Dentro da classe WhatsappBot, no método __init__, altere as variáveis self.message e self.contact.

Python

class WhatsappBot:
    def __init__(self):
        # --- ÁREA DE CONFIGURAÇÃO ---
        self.message = "Sua mensagem aqui"
        self.contact = ["Nome Exato do Contato 1", "Nome do Grupo 2"]
        # ---------------------------
        
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('lang=pt-br')
        servico = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=servico, options=self.options)
Importante: Os nomes na lista self.contact devem ser idênticos aos que aparecem no seu WhatsApp.

5. Execute a aplicação
Bash

python bot/bot.py
Ao executar, uma janela do Chrome abrirá. Escaneie o QR Code com seu celular para fazer login no WhatsApp Web. Após o login, o bot iniciará os envios.

📸 Demonstração
<p align="center">
<img src="URL_DO_SEU_GIF_DE_DEMONSTRAÇÃO_AQUI.gif" alt="Demonstração do Bot">
</p>

⚠️ Aviso Importante
Este projeto foi desenvolvido para fins educacionais. A automação de contas de usuário pode violar os Termos de Serviço do WhatsApp, podendo resultar no bloqueio da sua conta. Use por sua conta e risco.

📝 Licença
Este projeto está sob a licença MIT.

<p align="center">
Feito com ❤️ por <strong>Aldhemir</strong>
</p>
<p align="center">
<a href="https://github.com/aldhemir">
<img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/>
</a>
</p>
