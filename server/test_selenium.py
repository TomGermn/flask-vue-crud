# import threading
# import time
# import pytest

# from selenium import webdriver
# from selenium.webdriver.firefox.options import Options
# from selenium.webdriver.common.by import By
# from app import app, BOOKS

# @pytest.fixture(scope="module")
# def test_app():
#     thread = threading.Thread(target=app.run, kwargs={'port': 5001})
#     thread.daemon = True
#     thread.start()
#     time.sleep(1)
#     yield

# @pytest.fixture
# def browser():
#     options = Options()
#     options.add_argument('--headless')  # Supprime ça si tu veux voir le navigateur
#     driver = webdriver.Firefox(options=options)
#     yield driver
#     driver.quit()

# def test_books_are_displayed(test_app, browser):
#     BOOKS.clear()
#     BOOKS.extend([
#         {'id': 'x1', 'title': 'Test Book', 'author': 'Tester', 'read': True},
#         {'id': 'x2', 'title': 'Second Book', 'author': 'Author 2', 'read': False}
#     ])

#     browser.get('http://localhost:5001')
#     button = browser.find_element(By.ID, 'load-books')
#     button.click()

#     time.sleep(1)  # Laisse le temps au JS de charger les données

#     items = browser.find_elements(By.TAG_NAME, 'li')
#     assert len(items) == 2
#     assert 'Test Book by Tester' in [i.text for i in items]
#     assert 'Second Book by Author 2' in [i.text for i in items]
