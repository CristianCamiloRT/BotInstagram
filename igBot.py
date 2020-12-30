from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import time
import random 


class InstagramBot:
    def __init__ (self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox(executable_path="geckodriver.exe")
    
    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com")
        time.sleep(3)
        campo_usuario = driver.find_element_by_xpath("//input[@name='username']")
        campo_usuario.click()
        campo_usuario.clear()
        campo_usuario.send_keys(self.username)

        campo_senha = driver.find_element_by_xpath("//input[@name='password']")
        campo_senha.click()
        campo_senha.clear()
        campo_senha.send_keys(self.password)
        campo_senha.send_keys(Keys.RETURN)
        time.sleep(5)
        self.comente_nas_fotos_com_a_hastag('badbunnypr')

    @staticmethod
    def digite_como_uma_pessoa(frase, onde_digitar):
        for letra in frase:
            onde_digitar.send_keys(letra)
            time.sleep(random.randint(1,2)/30)

    def comente_nas_fotos_com_a_hastag(self, hastag):
        driver = self.driver
        driver.get("https://www.instagram.com/"+hastag+"/")
        time.sleep(3)

        driver.get("https://www.instagram.com/p/CHi3xTmhtUG/")
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        time.sleep(2)

        for i in range (9999999999999999999999999999999999999999):
            try: 
                comentario = "#DAKITI"
                driver.find_element_by_class_name('Ypffh').click()
                campo_comentario = driver.find_element_by_class_name('Ypffh')
                time.sleep(2)
                self.digite_como_uma_pessoa(comentario,campo_comentario)
                time.sleep(1)
                driver.find_element_by_xpath("//button[contains(text(),'Publicar')]").click()
                time.sleep(random.randint(5,10))
                print(i)
            except Exception as e:
                print(e)
                driver.get("https://www.instagram.com")
                for j in range (3):
                    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
                    time.sleep(5)
                driver.get("https://www.instagram.com/p/CHi3xTmhtUG/")
                time.sleep(105)
                print(i)

CristianBot = InstagramBot('telefono-username','contraseña')
CristianBot.login()

