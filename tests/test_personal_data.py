from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from settings import valid_email, valid_password



# TC_rostelecom_auth_0021
def test_change_name_and_surname_0021(selenium):
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
    selenium.find_element(By.ID, 'password').send_keys(valid_password)

    # Кликаем по кнопке Войти
    selenium.find_element(By.NAME, 'login').click()

    # Неявное ожидание
    selenium.implicitly_wait(10)

    # Ожидаем, что заголовок на странице содержит текст "Учетные данные"
    assert selenium.find_element(By.CLASS_NAME, 'card-title').text\
           == "Учетные данные"

    # Кликаем по иконке с карандашом рядом с именем и фамилией
    selenium.find_element(By.CSS_SELECTOR, '.rt-base-icon.rt-base-icon--fill-path.edit-btn__icon').click()
    # Ожидаем, что заголовок в открывшемся окне содержит текст "Введите ФИО"
    assert selenium.find_element(By.CLASS_NAME, 'card-modal__title').text == "Введите ФИО"

    first_name = 'Иван'
    last_name = 'Иванов'
    # Очищаем поле "Фамилия". Метод clear() не срабатывает, поэтому решаю проблему с помощью Keys
    selenium.find_element(By.ID, 'user_lastname').click()
    selenium.find_element(By.ID, 'user_lastname').send_keys(Keys.CONTROL + "a")
    selenium.find_element(By.ID, 'user_lastname').send_keys(Keys.DELETE)

    # Очищаем поле "Имя"
    selenium.find_element(By.ID, 'user_firstname').click()
    selenium.find_element(By.ID, 'user_firstname').send_keys(Keys.CONTROL + "a")
    selenium.find_element(By.ID, 'user_firstname').send_keys(Keys.DELETE)

    # Записываем в поле новую фамилию
    selenium.find_element(By.ID, 'user_lastname').send_keys(last_name)
    # Записываем в поле новое имя
    selenium.find_element(By.ID, 'user_firstname').send_keys(first_name)
    # Кликаем по кнопке "Сохранить"
    selenium.find_element(By.ID, 'user_contacts_editor_save').click()

    # Неявное ожидание
    selenium.implicitly_wait(10)

    # Ожидаем, что Имя и Фамилия соответствуют новым
    assert selenium.find_element(By.CLASS_NAME, 'user-name__last-name').text \
           == last_name
    assert selenium.find_element(By.CLASS_NAME, 'user-name__first-patronymic').text \
           == first_name



# TC_rostelecom_auth_0022
def test_change_to_uncorrect_surname_0022(selenium):
    # Переходим на страницу авторизации
    selenium.get(
        'https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=c05af488-19f8-4b74-8368-cffa877f1c97&theme&auth_type')

    # Неявное ожидание
    selenium.implicitly_wait(10)

    # Ожидаем, что заголовок на странице содержит тест "Авторизация"
    assert selenium.find_element(By.CSS_SELECTOR, ".card-container__title").text == "Авторизация"

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

    # Кликаем по иконке с карандашом рядом с именем и фамилией
    selenium.find_element(By.CSS_SELECTOR, '.rt-base-icon.rt-base-icon--fill-path.edit-btn__icon').click()
    # Ожидаем, что заголовок в открывшемся окне содержит текст "Введите ФИО"
    assert selenium.find_element(By.CLASS_NAME, 'card-modal__title').text == "Введите ФИО"

    last_name = 'Ivanov'
    # Очищаем поле "Фамилия". Метод clear() не срабатывает, поэтому решаю проблему с помощью Keys
    selenium.find_element(By.ID, 'user_lastname').click()
    selenium.find_element(By.ID, 'user_lastname').send_keys(Keys.CONTROL + "a")
    selenium.find_element(By.ID, 'user_lastname').send_keys(Keys.DELETE)

    # Записываем в поле новую фамилию
    selenium.find_element(By.ID, 'user_lastname').send_keys(last_name)
    # Кликаем по кнопке "Сохранить"
    selenium.find_element(By.ID, 'user_contacts_editor_save').click()

    # Неявное ожидание
    selenium.implicitly_wait(10)

    # Ожидаем, что появится сообщение о некорректности данных
    assert selenium.find_element(By.CSS_SELECTOR, '.rt-input-container__meta.rt-input-container__meta--error').text \
           == 'Необходимо заполнить поле кириллицей, используя не менее двух символов и не более двух слов'