from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ConfirmationPage(BasePage):

    TITULO_SUCESSO = (By.CLASS_NAME, "complete-header")
    MENSAGEM_SUCESSO = (By.CLASS_NAME, "complete-text")
    BOTAO_VOLTAR_PRODUTOS = (By.ID, "back-to-products")

    def obter_titulo_sucesso(self) -> str:
        return self.texto_de(self.TITULO_SUCESSO)

    def obter_mensagem_sucesso(self) -> str:
        return self.texto_de(self.MENSAGEM_SUCESSO)

    def voltar_para_produtos(self):
        self.clicar(self.BOTAO_VOLTAR_PRODUTOS)
        return self

    def compra_foi_finalizada(self) -> bool:
        return self.esta_visivel(self.TITULO_SUCESSO)