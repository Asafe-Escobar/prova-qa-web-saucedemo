import os
import pytest
from utils.driver_factory import criar_driver


@pytest.fixture
def driver():
    headless = os.getenv("HEADLESS", "false").lower() == "true"
    driver = criar_driver(headless=headless)
    yield driver
    driver.quit()