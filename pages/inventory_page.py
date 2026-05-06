from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from pages.base_page import BasePage


class InventoryPage(BasePage):

    URL = "https://www.saucedemo.com/inventory.html"
    URL_CARRINHO = "https://www.saucedemo.com/cart.html"

    TITULO_PAGINA = (By.CLASS_NAME, "title")
    ICONE_CARRINHO = (By.CLASS_NAME, "shopping_cart_link")
    QUANTIDADE_CARRINHO = (By.CLASS_NAME, "shopping_cart_badge")

    def _botao_adicionar(self, nome_produto: str):
        produto_id = nome_produto.lower().replace(" ", "-")
        return (By.ID, f"add-to-cart-{produto_id}")

    def _botao_remover(self, nome_produto: str):
        produto_id = nome_produto.lower().replace(" ", "-")
        return (By.ID, f"remove-{produto_id}")

    def adicionar_ao_carrinho(self, nome_produto: str):
        try:
            self.clicar(self._botao_adicionar(nome_produto))
        except WebDriverException:
            self.driver.execute_script(
                f"document.getElementById('add-to-cart-{nome_produto.lower().replace(' ', '-')}').click();"
            )
        return self

    def remover_do_carrinho(self, nome_produto: str):
        try:
            self.clicar(self._botao_remover(nome_produto))
        except WebDriverException:
            self.driver.execute_script(
                f"document.getElementById('remove-{nome_produto.lower().replace(' ', '-')}').click();"
            )
        return self

    def quantidade_no_carrinho(self) -> int:
        if not self.esta_visivel(self.QUANTIDADE_CARRINHO):
            return 0
        return int(self.texto_de(self.QUANTIDADE_CARRINHO))

    def ir_para_carrinho(self):
        try:
            self.clicar(self.ICONE_CARRINHO)
        except WebDriverException:
            self.driver.get(self.URL_CARRINHO)
        return self

    def obter_titulo(self) -> str:
        return self.texto_de(self.TITULO_PAGINA)