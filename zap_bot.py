from selenium import webdriver
import time

class whats_bot:
    def __init__(self):
        self.mensagem = "Mensagem de teste, funcionando"
        self.contatos = ["Teste"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

    def enviar_msg(self):
        # <span class="matched-text _3-8er">Teste</span>
        # <div tabindex="-1" class="_2A8P4">
        # <span data-testid="send" data-icon="send" class="">
        print("entrando...")
        self.driver.get('https://web.whatsapp.com/')
        time.sleep(8)
        for contato in self.contatos:
            contato = self.driver.find_element_by_xpath(f"//span[@title='{contato}']")
            time.sleep(2)
            contato.click()
            chat_entrar = self.driver.find_element_by_class_name('_2A8P4')
            time.sleep(2)
            chat_entrar.click()
            chat_entrar.send_keys(self.mensagem)
            botao_enviar = self.driver.find_element_by_xpath("//span[@data-testid='send']")
            time.sleep(2)
            botao_enviar.click()
            time.sleep(2)


bot = whats_bot()
bot.enviar_msg()