from selenium.webdriver.common.by import By
from settings import valid_password, valid_email



# TC_rostelecom_auth_0016
def test_email_auth_btn_phone_0016(selenium):
    # Переходим на страницу авторизации
    selenium.get(
        'https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=c05af488-19f8-4b74-8368-cffa877f1c97&theme&auth_type')

    # Неявное ожидание
    selenium.implicitly_wait(10)

    # Ожидаем, что заголовок на странице содержит текст "Авторизация"
    assert selenium.find_element(By.CSS_SELECTOR, ".card-container__title").text == "Авторизация"

    # Кликаем по кнопке Телефон
    selenium.find_element(By.ID, 't-btn-tab-phone').click()
    # Ожидаем, что текст в поле ввода – "Мобильный телефон"
    assert selenium.find_element(By.XPATH,
                                 "//*[@id='page-right']/div/div/div/form/div[1]/div[2]/div/span[2]").text \
           == "Мобильный телефон"

    # Вводим Почту
    selenium.find_element(By.ID, 'username').send_keys(valid_email)
    # Вводим Пароль
    selenium.find_element(By.ID, 'password').send_keys(valid_password)

    # Кликаем по кнопке Войти
    selenium.find_element(By.NAME, 'login').click()

    # Неявное ожидание
    selenium.implicitly_wait(10)

    # Ожидаем, что заголовок на странице содержит текст "Учетные данные"
    assert selenium.find_element(By.CLASS_NAME, 'card-title').text\
           == "Учетные данные"



# TC_rostelecom_auth_0017
def test_uncorret_password_0017(selenium):
    # Переходим на страницу авторизации
    selenium.get(
        'https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=c05af488-19f8-4b74-8368-cffa877f1c97&theme&auth_type')

    # Неявное ожидание
    selenium.implicitly_wait(10)

    # Ожидаем, что заголовок на странице содержит текст "Авторизация"
    assert selenium.find_element(By.CSS_SELECTOR, ".card-container__title").text == "Авторизация"

    # Вводим Почту
    selenium.find_element(By.ID, 'username').send_keys(valid_email)
    # Вводим Пароль
    selenium.find_element(By.ID, 'password').send_keys('Fgfgfg1')

    # Кликаем по кнопке Войти
    selenium.find_element(By.NAME, 'login').click()

    # Неявное ожидание
    selenium.implicitly_wait(10)

    # Ожидаем, что появится сообщение о неверном пароле и "Забыл пароль" поменяет цвет
    assert selenium.find_element(By.ID, 'form-error-message').text == "Неверный логин или пароль"
    assert selenium.find_element(By.CSS_SELECTOR,
                                 '.rt-link.rt-link--orange.login-form__forgot-pwd.login-form__forgot-pwd--animated').text \
           == "Забыл пароль"



# TC_rostelecom_auth_0020
def test_email_auth_btn_login_0020(selenium):
    # Переходим на страницу авторизации
    selenium.get(
        'https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=c05af488-19f8-4b74-8368-cffa877f1c97&theme&auth_type')

    # Неявное ожидание
    selenium.implicitly_wait(10)

    # Ожидаем, что заголовок на странице содержит текст "Авторизация"
    assert selenium.find_element(By.CSS_SELECTOR, ".card-container__title").text == "Авторизация"

    # Кликаем по кнопке Логин
    selenium.find_element(By.ID, 't-btn-tab-login').click()
    # Ожидаем, что текст в поле ввода - "Логин"
    assert selenium.find_element(By.XPATH,
                                 "//*[@id='page-right']/div/div/div/form/div[1]/div[2]/div/span[2]").text \
           == "Логин"

    # Вводим Почту
    selenium.find_element(By.ID, 'username').send_keys(valid_email)
    # Вводим Пароль
    selenium.find_element(By.ID, 'password').send_keys(valid_password)

    # Кликаем по кнопке Войти
    selenium.find_element(By.NAME, 'login').click()

    # Неявное ожидание
    selenium.implicitly_wait(10)

    assert selenium.find_element(By.CLASS_NAME, 'card-title').text\
           == "Учетные данные"
