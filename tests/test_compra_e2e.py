import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.confirmation_page import ConfirmationPage


USUARIO_VALIDO = "standard_user"
SENHA_VALIDA = "secret_sauce"


class TestComprasE2E:

    def test_login_com_credenciais_validas_redireciona_para_produtos(self, driver):
        LoginPage(driver).abrir_pagina().fazer_login(USUARIO_VALIDO, SENHA_VALIDA)

        inventory = InventoryPage(driver)
        assert "inventory" in driver.current_url
        assert inventory.obter_titulo() == "Products"

    def test_login_com_usuario_bloqueado_exibe_mensagem_de_erro(self, driver):
        login = LoginPage(driver).abrir_pagina()
        login.fazer_login("locked_out_user", SENHA_VALIDA)

        mensagem = login.obter_mensagem_de_erro()
        assert "locked out" in mensagem.lower()

    def test_adicionar_produto_ao_carrinho_atualiza_contador(self, driver):
        LoginPage(driver).abrir_pagina().fazer_login(USUARIO_VALIDO, SENHA_VALIDA)
        inventory = InventoryPage(driver)

        inventory.adicionar_ao_carrinho("Sauce Labs Backpack")

        assert inventory.quantidade_no_carrinho() == 1

    def test_remover_produto_do_carrinho_atualiza_contador(self, driver):
        LoginPage(driver).abrir_pagina().fazer_login(USUARIO_VALIDO, SENHA_VALIDA)
        inventory = InventoryPage(driver)

        inventory.adicionar_ao_carrinho("Sauce Labs Backpack")
        inventory.remover_do_carrinho("Sauce Labs Backpack")

        assert inventory.quantidade_no_carrinho() == 0

    def test_compra_completa_de_dois_produtos_finaliza_com_sucesso(self, driver):
        LoginPage(driver).abrir_pagina().fazer_login(USUARIO_VALIDO, SENHA_VALIDA)

        inventory = InventoryPage(driver)
        inventory.adicionar_ao_carrinho("Sauce Labs Backpack")
        inventory.adicionar_ao_carrinho("Sauce Labs Bike Light")
        assert inventory.quantidade_no_carrinho() == 2

        inventory.ir_para_carrinho()
        cart = CartPage(driver)
        assert cart.quantidade_de_itens() == 2
        assert "Sauce Labs Backpack" in cart.listar_nomes_dos_itens()

        cart.finalizar_compra()
        checkout = CheckoutPage(driver)
        checkout.preencher_dados("Joao", "Silva", "64000-000")
        checkout.continuar()

        assert "$" in checkout.obter_total()

        checkout.finalizar()
        confirmation = ConfirmationPage(driver)
        assert confirmation.compra_foi_finalizada()
        assert confirmation.obter_titulo_sucesso() == "Thank you for your order!"

    def test_checkout_sem_preencher_dados_exibe_erro(self, driver):
        LoginPage(driver).abrir_pagina().fazer_login(USUARIO_VALIDO, SENHA_VALIDA)
        InventoryPage(driver).adicionar_ao_carrinho("Sauce Labs Backpack").ir_para_carrinho()

        CartPage(driver).finalizar_compra()
        checkout = CheckoutPage(driver)
        checkout.continuar()

        mensagem = checkout.obter_mensagem_de_erro()
        assert "first name" in mensagem.lower() or "required" in mensagem.lower()