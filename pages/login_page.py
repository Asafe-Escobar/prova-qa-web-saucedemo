from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):

    URL = "https://www.saucedemo.com/"

    CAMPO_USUARIO = (By.ID, "user-name")
    CAMPO_SENHA = (By.ID, "password")
    BOTAO_LOGIN = (By.ID, "login-button")
    MENSAGEM_ERRO = (By.CSS_SELECTOR, "[data-test='error']")

    def abrir_pagina(self):
        self.abrir(self.URL)
        return self

    def fazer_login(self, usuario: str, senha: str):
        self.digitar(self.CAMPO_USUARIO, usuario)
        self.digitar(self.CAMPO_SENHA, senha)
        self.clicar(self.BOTAO_LOGIN)
        return self

    def obter_mensagem_de_erro(self) -> str:
        return self.texto_de(self.MENSAGEM_ERRO)