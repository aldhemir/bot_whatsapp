import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class WhatsappBot:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('lang=pt-br')
        servico = Service(ChromeDriverManager().install())
        
        self.driver = webdriver.Chrome(service=servico, options=chrome_options)

    def send_message(self, contatos, mensagem):
        """
        Abre o WhatsApp Web, busca os contatos e envia a mensagem.
        """
        self.driver.get('https://web.whatsapp.com/')
        
        try:
            wait = WebDriverWait(self.driver, 60)
            wait.until(
                EC.presence_of_element_located((By.XPATH, '//div[@data-testid="chat-list-search"]'))
            )
            print("Login realizado com sucesso.")
        except:
            print("Erro: O login não foi realizado no tempo esperado (60 segundos).")
            self.driver.quit()
            return
            
        for contato in contatos:
            try:
                print(f"Buscando o contato: {contato}")
                search_box = self.driver.find_element(By.XPATH, '//div[@data-testid="chat-list-search"]')
                search_box.click()
                search_box.clear()
                search_box.send_keys(contato)
                
                time.sleep(2)

                user = self.driver.find_element(By.XPATH, f'//span[@title="{contato}"]')
                user.click()
                time.sleep(2)

                message_box = self.driver.find_element(By.XPATH, '//div[@data-testid="conversation-compose-box-input"]')
                message_box.click()
                message_box.send_keys(mensagem)
                message_box.send_keys(Keys.ENTER)
                print(f"Mensagem enviada para: {contato}")
                time.sleep(3)
            
            except Exception as e:
                print(f"Não foi possível encontrar ou enviar mensagem para o contato: {contato}. Erro: {e}")
                continue

        print("Processo finalizado.")
        time.sleep(10) 
        self.driver.quit()


if __name__ == '__main__':
    # --- ÁREA DE CONFIGURAÇÃO ---
    contatos_alvo = ["Nome Exato do Contato 1", "Nome do Grupo 2"]
    mensagem_para_enviar = "Olá! Esta é uma mensagem de teste enviada pelo meu bot Python."
    # ---------------------------

    bot = WhatsappBot()
    bot.send_message(contatos=contatos_alvo, mensagem=mensagem_para_enviar)
