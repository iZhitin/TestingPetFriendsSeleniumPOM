from pages.auth_page import AuthPage

# для визуального контроля
import time

# для запуска тестов через терминал:
# python -m pytest -v --driver Chrome --driver-path chromedriver.exe tests\test_auth_page.py


# тестирование авторизации
def test_auth_page(selenium):
    page = AuthPage(selenium)
    time.sleep(3)
    page.enter_email("p@p.p")
    page.enter_password("122333")
    page.click_btn()

    assert page.get_relative_link() == '/all_pets', 'Ошибка авторизации'
