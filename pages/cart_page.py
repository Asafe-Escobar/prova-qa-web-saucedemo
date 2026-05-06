from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from pages.base_page import BasePage


class CartPage(BasePage):

    URL = "https://www.saucedemo.com/cart.html"
    URL_CHECKOUT = "https://www.saucedemo.com/checkout-step-one.html"
    URL_INVENTORY = "https://www.saucedemo.com/inventory.html"

    TITULO_PAGINA = (By.CLASS_NAME, "title")
    ITENS_NO_CARRINHO = (By.CLASS_NAME, "cart_item")
    NOMES_DOS_ITENS = (By.CLASS_NAME, "inventory_item_name")
    BOTAO_CHECKOUT = (By.ID, "checkout")
    BOTAO_CONTINUAR_COMPRANDO = (By.ID, "continue-shopping")

    def quantidade_de_itens(self) -> int:
        return len(self.driver.find_elements(*self.ITENS_NO_CARRINHO))

    def listar_nomes_dos_itens(self) -> list:
        elementos = self.driver.find_elements(*self.NOMES_DOS_ITENS)
        return [el.text for el in elementos]

    def finalizar_compra(self):
        try:
            self.clicar(self.BOTAO_CHECKOUT)
        except WebDriverException:
            self.driver.get(self.URL_CHECKOUT)
        return self

    def continuar_comprando(self):
        try:
            self.clicar(self.BOTAO_CONTINUAR_COMPRANDO)
        except WebDriverException:
            self.driver.get(self.URL_INVENTORY)
        return self

    def obter_titulo(self) -> str:
        return self.texto_de(self.TITULO_PAGINA)