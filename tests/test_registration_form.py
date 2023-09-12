from selenium.webdriver.common.by import By
from settings import valid_email, valid_password

# TC_rostelecom_auth_0001
def test_uncorret_data_0001(selenium):
   # Переходим на страницу авторизации
   selenium.get('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=c05af488-19f8-4b74-8368-cffa877f1c97&theme&auth_type')

   # Неявное ожидание
   selenium.implicitly_wait(10)

   # Ожидаем, что заголовок на странице содержит текст "Авторизация"
   assert selenium.find_element(By.CSS_SELECTOR, ".card-container__title").text == "Авторизация"
   # Кликаем по ссылке Зарегистрироваться
   selenium.find_element(By.ID, 'kc-register').click()

   # Вводим Имя
   selenium.find_element(By.NAME, 'firstName').send_keys('Й')
   # Вводим Фамилию
   selenium.find_element(By.NAME, 'lastName').send_keys('И')
   # Вводим Почту
   selenium.find_element(By.ID, 'address').send_keys('sojogo1848@wlmycn.com')
   # Вводим Пароль
   selenium.find_element(By.ID, 'password').send_keys('Fgfgfg1')
   # Повторяем Пароль
   selenium.find_element(By.ID, 'password-confirm').send_keys('Fgfgfg1')
   # Кликаем по кнопке Зарегистрироваться
   selenium.find_element(By.NAME, 'register').click()

   # Ожидаем, что на странице появятся оповещения о некорректности данных
   # Имя
   assert selenium.find_element(By.XPATH,
                                '//*[@id="page-right"]/div/div/div/form/div[1]/div[1]/span').text \
          == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."
   # Фамилия
   assert selenium.find_element(By.XPATH,
                                '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/span').text \
          == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."
   # Пароль
   assert selenium.find_element(By.XPATH,
                                '//*[@id="page-right"]/div/div/div/form/div[4]/div[1]/span').text \
          == "Длина пароля должна быть не менее 8 символов"
   # Повтор пароля
   assert selenium.find_element(By.XPATH,
                                '//*[@id="page-right"]/div/div/div/form/div[4]/div[2]/span').text \
          == "Длина пароля должна быть не менее 8 символов"



# TC_rostelecom_auth_0002
def test_uncorret_data_0002(selenium):
   # Переходим на страницу авторизации
   selenium.get('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=c05af488-19f8-4b74-8368-cffa877f1c97&theme&auth_type')

   # Неявное ожидание
   selenium.implicitly_wait(10)

   # Ожидаем, что заголовок на странице содержит текст "Авторизация"
   assert selenium.find_element(By.CSS_SELECTOR, ".card-container__title").text == "Авторизация"
   # Кликаем по ссылке Зарегистрироваться
   selenium.find_element(By.ID, 'kc-register').click()


   # Вводим Имя
   selenium.find_element(By.NAME, 'firstName').send_keys('Й')
   # Вводим Фамилию
   selenium.find_element(By.NAME, 'lastName').send_keys('Ил')
   # Вводим Почту
   selenium.find_element(By.ID, 'address').send_keys('sojogo1848.com')
   # Вводим Пароль
   selenium.find_element(By.ID, 'password').send_keys('Fgfgfgfg')
   # Повторяем Пароль
   selenium.find_element(By.ID, 'password-confirm').send_keys('Fgfgfgfg')
   # Кликаем по кнопке Зарегистрироваться
   selenium.find_element(By.NAME, 'register').click()

   # Ожидаем, что на странице появятся оповещения о некорректности данных
   # Имя
   assert selenium.find_element(By.XPATH,
                                '//*[@id="page-right"]/div/div/div/form/div[1]/div[1]/span').text \
          == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."
   # Почта
   assert selenium.find_element(By.XPATH,
                                '//*[@id="page-right"]/div/div/div/form/div[3]/div/span').text \
          == "Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru"
   # Пароль
   assert selenium.find_element(By.XPATH,
                                '//*[@id="page-right"]/div/div/div/form/div[4]/div[1]/span').text \
          == "Пароль должен содержать хотя бы 1 спецсимвол или хотя бы одну цифру"
   # Повтор пароля
   assert selenium.find_element(By.XPATH,
                                '//*[@id="page-right"]/div/div/div/form/div[4]/div[2]/span').text \
          == "Пароль должен содержать хотя бы 1 спецсимвол или хотя бы одну цифру"



# TC_rostelecom_auth_0003
def test_uncorret_data_0003(selenium):
   # Переходим на страницу авторизации
   selenium.get('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=c05af488-19f8-4b74-8368-cffa877f1c97&theme&auth_type')

   # Неявное ожидание
   selenium.implicitly_wait(10)

   # Ожидаем, что заголовок на странице содержит тест "Авторизация"
   assert selenium.find_element(By.CSS_SELECTOR, ".card-container__title").text == "Авторизация"
   # Кликаем по ссылке Зарегистрироваться
   selenium.find_element(By.ID, 'kc-register').click()

   # Вводим Имя
   selenium.find_element(By.NAME, 'firstName').send_keys('Й')
   # Вводим Фамилию
   selenium.find_element(By.NAME, 'lastName').send_keys('Илья')
   # Вводим Почту
   selenium.find_element(By.ID, 'address').send_keys('')
   # Вводим Пароль
   selenium.find_element(By.ID, 'password').send_keys('fgfgfgf1')
   # Повторяем Пароль
   selenium.find_element(By.ID, 'password-confirm').send_keys('fgfgfgf1')
   # Кликаем по кнопке Зарегистрироваться
   selenium.find_element(By.NAME, 'register').click()

   # Ожидаем, что на странице появятся оповещения о некорректности данных
   # Имя
   assert selenium.find_element(By.XPATH,
                                '//*[@id="page-right"]/div/div/div/form/div[1]/div[1]/span').text \
          == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."
   # Почта
   assert selenium.find_element(By.XPATH,
                                '//*[@id="page-right"]/div/div/div/form/div[3]/div/span').text \
          == "Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru"
   # Пароль
   assert selenium.find_element(By.XPATH,
                                '//*[@id="page-right"]/div/div/div/form/div[4]/div[1]/span').text \
          == "Пароль должен содержать хотя бы одну заглавную букву"
   # Повтор пароля
   assert selenium.find_element(By.XPATH,
                                '//*[@id="page-right"]/div/div/div/form/div[4]/div[2]/span').text \
          == "Пароль должен содержать хотя бы одну заглавную букву"




# TC_rostelecom_auth_0004
def test_uncorret_data_0004(selenium):
   # Переходим на страницу авторизации
   selenium.get('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=c05af488-19f8-4b74-8368-cffa877f1c97&theme&auth_type')

   # Неявное ожидание
   selenium.implicitly_wait(10)

   # Ожидаем, что заголовок на странице содержит текст "Авторизация"
   assert selenium.find_element(By.CSS_SELECTOR, ".card-container__title").text == "Авторизация"
   # Кликаем по ссылке Зарегистрироваться
   selenium.find_element(By.ID, 'kc-register').click()

   # Вводим Имя
   selenium.find_element(By.NAME, 'firstName').send_keys('Й')
   # Вводим Фамилию
   selenium.find_element(By.NAME, 'lastName').send_keys('ИльяИльяИльяИльяИльяИльяИльяИл')
   # Вводим Почту
   selenium.find_element(By.ID, 'address').send_keys('sojogo1848.com')
   # Вводим Пароль
   selenium.find_element(By.ID, 'password').send_keys('Апапапап')
   # Повторяем Пароль
   selenium.find_element(By.ID, 'password-confirm').send_keys('Апапапап')
   # Кликаем по кнопке Зарегистрироваться
   selenium.find_element(By.NAME, 'register').click()

   # Ожидаем, что на странице появятся оповещения о некорректности данных
   # Имя
   assert selenium.find_element(By.XPATH,
                                '//*[@id="page-right"]/div/div/div/form/div[1]/div[1]/span').text \
          == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."
   # Почта
   assert selenium.find_element(By.XPATH,
                                '//*[@id="page-right"]/div/div/div/form/div[3]/div/span').text \
          == "Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru"
   # Пароль
   assert selenium.find_element(By.XPATH,
                                '//*[@id="page-right"]/div/div/div/form/div[4]/div[1]/span').text \
          == "Пароль должен содержать только латинские буквы"
   # Повтор пароля
   assert selenium.find_element(By.XPATH,
                                '//*[@id="page-right"]/div/div/div/form/div[4]/div[2]/span').text \
          == "Пароль должен содержать только латинские буквы"




# TC_rostelecom_auth_0005
def test_uncorret_data_0005(selenium):
   # Переходим на страницу авторизации
   selenium.get('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=c05af488-19f8-4b74-8368-cffa877f1c97&theme&auth_type')

   # Неявное ожидание
   selenium.implicitly_wait(10)

   # Ожидаем, что заголовок на странице содержит текст "Авторизация"
   assert selenium.find_element(By.CSS_SELECTOR, ".card-container__title").text == "Авторизация"
   # Кликаем по ссылке Зарегистрироваться
   selenium.find_element(By.ID, 'kc-register').click()

   # Вводим Имя
   selenium.find_element(By.NAME, 'firstName').send_keys('Й')
   # Вводим Фамилию
   selenium.find_element(By.NAME, 'lastName').send_keys('ИльяИльяИльяИльяИльяИльяИльяИлья')
   # Вводим Почту
   selenium.find_element(By.ID, 'address').send_keys('sojogo1848.com')
   # Вводим Пароль
   selenium.find_element(By.ID, 'password').send_keys('апапапап')
   # Повторяем Пароль
   selenium.find_element(By.ID, 'password-confirm').send_keys('апапапап')
   # Кликаем по кнопке Зарегистрироваться
   selenium.find_element(By.NAME, 'register').click()

   # Ожидаем, что на странице появятся оповещения о некорректности данных
   # Имя
   assert selenium.find_element(By.XPATH,
                                '//*[@id="page-right"]/div/div/div/form/div[1]/div[1]/span').text \
          == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."
   # Фамилия
   assert selenium.find_element(By.XPATH,
                                '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/span').text \
          == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."
   # Почта
   assert selenium.find_element(By.XPATH,
                                '//*[@id="page-right"]/div/div/div/form/div[3]/div/span').text \
          == "Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru"
   # Пароль
   assert selenium.find_element(By.XPATH,
                                '//*[@id="page-right"]/div/div/div/form/div[4]/div[1]/span').text \
          == "Пароль должен содержать только латинские буквы"
   # Повтор пароля
   assert selenium.find_element(By.XPATH,
                                '//*[@id="page-right"]/div/div/div/form/div[4]/div[2]/span').text \
          == "Пароль должен содержать только латинские буквы"



# TC_rostelecom_auth_0006
def test_uncorret_data_0006(selenium):
   # Переходим на страницу авторизации
   selenium.get('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=c05af488-19f8-4b74-8368-cffa877f1c97&theme&auth_type')

   # Неявное ожидание
   selenium.implicitly_wait(10)

   # Ожидаем, что заголовок на странице содержит текст "Авторизация"
   assert selenium.find_element(By.CSS_SELECTOR, ".card-container__title").text == "Авторизация"
   # Кликаем по ссылке Зарегистрироваться
   selenium.find_element(By.ID, 'kc-register').click()

   # Вводим Имя
   selenium.find_element(By.NAME, 'firstName').send_keys('Й')
   # Вводим Фамилию
   selenium.find_element(By.NAME, 'lastName').send_keys('')
   # Вводим Почту
   selenium.find_element(By.ID, 'address').send_keys('')
   # Вводим Пароль
   selenium.find_element(By.ID, 'password').send_keys('')
   # Повторяем Пароль
   selenium.find_element(By.ID, 'password-confirm').send_keys('')
   # Кликаем по кнопке Зарегистрироваться
   selenium.find_element(By.NAME, 'register').click()

   # Ожидаем, что на странице появятся оповещения о некорректности данных
   # Имя
   assert selenium.find_element(By.XPATH,
                                '//*[@id="page-right"]/div/div/div/form/div[1]/div[1]/span').text \
          == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."
   # Фамилия
   assert selenium.find_element(By.XPATH,
                                '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/span').text \
          == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."
   # Почта
   assert selenium.find_element(By.XPATH,
                                '//*[@id="page-right"]/div/div/div/form/div[3]/div/span').text \
          == "Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru"
   # Пароль
   assert selenium.find_element(By.XPATH,
                                '//*[@id="page-right"]/div/div/div/form/div[4]/div[1]/span').text \
          == "Длина пароля должна быть не менее 8 символов"
   # Повтор пароля
   assert selenium.find_element(By.XPATH,
                                '//*[@id="page-right"]/div/div/div/form/div[4]/div[2]/span').text \
          == "Длина пароля должна быть не менее 8 символов"




# TC_rostelecom_auth_0007
def test_uncorret_data_0007(selenium):
   # Переходим на страницу авторизации
   selenium.get('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=c05af488-19f8-4b74-8368-cffa877f1c97&theme&auth_type')

   # Неявное ожидание
   selenium.implicitly_wait(10)

   # Ожидаем, что заголовок на странице содержит текст "Авторизация"
   assert selenium.find_element(By.CSS_SELECTOR, ".card-container__title").text == "Авторизация"
   # Кликаем по ссылке Зарегистрироваться
   selenium.find_element(By.ID, 'kc-register').click()

   # Вводим Имя
   selenium.find_element(By.NAME, 'firstName').send_keys('Йя')
   # Вводим Фамилию
   selenium.find_element(By.NAME, 'lastName').send_keys('Ил')
   # Вводим Почту
   selenium.find_element(By.ID, 'address').send_keys('')
   # Вводим Пароль
   selenium.find_element(By.ID, 'password').send_keys('Апапапап')
   # Повторяем Пароль
   selenium.find_element(By.ID, 'password-confirm').send_keys('Апапапап')
   # Кликаем по кнопке Зарегистрироваться
   selenium.find_element(By.NAME, 'register').click()

   # Ожидаем, что на странице появятся оповещения о некорректности данных
   # Почта
   assert selenium.find_element(By.XPATH,
                                '//*[@id="page-right"]/div/div/div/form/div[3]/div/span').text \
          == "Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru"
   # Пароль
   assert selenium.find_element(By.XPATH,
                                '//*[@id="page-right"]/div/div/div/form/div[4]/div[1]/span').text \
          == "Пароль должен содержать только латинские буквы"
   # Повтор пароля
   assert selenium.find_element(By.XPATH,
                                '//*[@id="page-right"]/div/div/div/form/div[4]/div[2]/span').text \
          == "Пароль должен содержать только латинские буквы"




# TC_rostelecom_auth_0008
def test_uncorret_data_0008(selenium):
   # Переходим на страницу авторизации
   selenium.get('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=c05af488-19f8-4b74-8368-cffa877f1c97&theme&auth_type')

   # Неявное ожидание
   selenium.implicitly_wait(10)

   # Ожидаем, что заголовок на странице содержит тест "Авторизация"
   assert selenium.find_element(By.CSS_SELECTOR, ".card-container__title").text == "Авторизация"
   # Кликаем по ссылке Зарегистрироваться
   selenium.find_element(By.ID, 'kc-register').click()

   # Вводим Имя
   selenium.find_element(By.NAME, 'firstName').send_keys('Йя')
   # Вводим Фамилию
   selenium.find_element(By.NAME, 'lastName').send_keys('Илья')
   # Вводим Почту
   selenium.find_element(By.ID, 'address').send_keys('sojogo1848@wlmycn.com')
   # Вводим Пароль
   selenium.find_element(By.ID, 'password').send_keys('апапапап')
   # Повторяем Пароль
   selenium.find_element(By.ID, 'password-confirm').send_keys('апапапап')
   # Кликаем по кнопке Зарегистрироваться
   selenium.find_element(By.NAME, 'register').click()

   # Ожидаем, что на странице появятся оповещения о некорректности данных
   # Пароль
   assert selenium.find_element(By.XPATH,
                                '//*[@id="page-right"]/div/div/div/form/div[4]/div[1]/span').text \
          == "Пароль должен содержать только латинские буквы"
   # Повтор пароля
   assert selenium.find_element(By.XPATH,
                                '//*[@id="page-right"]/div/div/div/form/div[4]/div[2]/span').text \
          == "Пароль должен содержать только латинские буквы"




# TC_rostelecom_auth_0009
def test_uncorret_data_0009(selenium):
   # Переходим на страницу авторизации
   selenium.get('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=c05af488-19f8-4b74-8368-cffa877f1c97&theme&auth_type')

   # Неявное ожидание
   selenium.implicitly_wait(10)

   # Ожидаем, что заголовок на странице содержит текст "Авторизация"
   assert selenium.find_element(By.CSS_SELECTOR, ".card-container__title").text == "Авторизация"
   # Кликаем по ссылке Зарегистрироваться
   selenium.find_element(By.ID, 'kc-register').click()


   # Вводим Имя
   selenium.find_element(By.NAME, 'firstName').send_keys('Йя')
   # Вводим Фамилию
   selenium.find_element(By.NAME, 'lastName').send_keys('ИльяИльяИльяИльяИльяИльяИльяИл')
   # Вводим Почту
   selenium.find_element(By.ID, 'address').send_keys('sojogo1848@.com')
   # Вводим Пароль
   selenium.find_element(By.ID, 'password').send_keys('')
   # Повторяем Пароль
   selenium.find_element(By.ID, 'password-confirm').send_keys('')
   # Кликаем по кнопке Зарегистрироваться
   selenium.find_element(By.NAME, 'register').click()

   # Ожидаем, что на странице появятся оповещения о некорректности данных
   # Почта
   assert selenium.find_element(By.XPATH,
                                '//*[@id="page-right"]/div/div/div/form/div[3]/div/span').text \
          == "Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru"
   # Пароль
   assert selenium.find_element(By.XPATH,
                                '//*[@id="page-right"]/div/div/div/form/div[4]/div[1]/span').text \
          == "Длина пароля должна быть не менее 8 символов"
   # Повтор пароля
   assert selenium.find_element(By.XPATH,
                                '//*[@id="page-right"]/div/div/div/form/div[4]/div[2]/span').text \
          == "Длина пароля должна быть не менее 8 символов"




# TC_rostelecom_auth_0010
def test_uncorret_data_0010(selenium):
   # Переходим на страницу авторизации
   selenium.get('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=c05af488-19f8-4b74-8368-cffa877f1c97&theme&auth_type')

   # Неявное ожидание
   selenium.implicitly_wait(10)

   # Ожидаем, что заголовок на странице содержит тест "Авторизация"
   assert selenium.find_element(By.CSS_SELECTOR, ".card-container__title").text == "Авторизация"
   # Кликаем по ссылке Зарегистрироваться
   selenium.find_element(By.ID, 'kc-register').click()

   # Вводим Имя
   selenium.find_element(By.NAME, 'firstName').send_keys('Йя')
   # Вводим Фамилию
   selenium.find_element(By.NAME, 'lastName').send_keys('ИльяИльяИльяИльяИльяИльяИльяИлья')
   # Вводим Почту
   selenium.find_element(By.ID, 'address').send_keys('')
   # Вводим Пароль
   selenium.find_element(By.ID, 'password').send_keys('Fgfgfg1')
   # Повторяем Пароль
   selenium.find_element(By.ID, 'password-confirm').send_keys('Fgfgfg1')
   # Кликаем по кнопке Зарегистрироваться
   selenium.find_element(By.NAME, 'register').click()

   # Ожидаем, что на странице появятся оповещения о некорректности данных
   # Фамилия
   assert selenium.find_element(By.XPATH,
                                '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/span').text \
          == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."
   # Почта
   assert selenium.find_element(By.XPATH,
                                '//*[@id="page-right"]/div/div/div/form/div[3]/div/span').text \
          == "Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru"
   # Пароль
   assert selenium.find_element(By.XPATH,
                                '//*[@id="page-right"]/div/div/div/form/div[4]/div[1]/span').text \
          == "Длина пароля должна быть не менее 8 символов"
   # Повтор пароля
   assert selenium.find_element(By.XPATH,
                                '//*[@id="page-right"]/div/div/div/form/div[4]/div[2]/span').text \
          == "Длина пароля должна быть не менее 8 символов"





# TC_rostelecom_auth_0011
def test_uncorret_data_0011(selenium):
   # Переходим на страницу авторизации
   selenium.get('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=c05af488-19f8-4b74-8368-cffa877f1c97&theme&auth_type')

   # Неявное ожидание
   selenium.implicitly_wait(10)

   # Ожидаем, что заголовок на странице содержит текст "Авторизация"
   assert selenium.find_element(By.CSS_SELECTOR, ".card-container__title").text == "Авторизация"
   # Кликаем по ссылке Зарегистрироваться
   selenium.find_element(By.ID, 'kc-register').click()

   # Вводим Имя
   selenium.find_element(By.NAME, 'firstName').send_keys('Йя')
   # Вводим Фамилию
   selenium.find_element(By.NAME, 'lastName').send_keys('')
   # Вводим Почту
   selenium.find_element(By.ID, 'address').send_keys('sojogo1848@wlmycn.com')
   # Вводим Пароль
   selenium.find_element(By.ID, 'password').send_keys('Fgfgfgfg')
   # Повторяем Пароль
   selenium.find_element(By.ID, 'password-confirm').send_keys('Fgfgfgfg')
   # Кликаем по кнопке Зарегистрироваться
   selenium.find_element(By.NAME, 'register').click()

   # Ожидаем, что на странице появятся оповещения о некорректности данных
   # Фамилия
   assert selenium.find_element(By.XPATH,
                                '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/span').text \
          == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."
   # Пароль
   assert selenium.find_element(By.XPATH,
                                '//*[@id="page-right"]/div/div/div/form/div[4]/div[1]/span').text \
          == "Пароль должен содержать хотя бы 1 спецсимвол или хотя бы одну цифру"
   # Повтор пароля
   assert selenium.find_element(By.XPATH,
                                '//*[@id="page-right"]/div/div/div/form/div[4]/div[2]/span').text \
          == "Пароль должен содержать хотя бы 1 спецсимвол или хотя бы одну цифру"




# TC_rostelecom_auth_0012
def test_uncorret_data_0012(selenium):
   # Переходим на страницу авторизации
   selenium.get('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=c05af488-19f8-4b74-8368-cffa877f1c97&theme&auth_type')

   # Неявное ожидание
   selenium.implicitly_wait(10)

   # Ожидаем, что заголовок на странице содержит текст "Авторизация"
   assert selenium.find_element(By.CSS_SELECTOR, ".card-container__title").text == "Авторизация"
   # Кликаем по ссылке Зарегистрироваться
   selenium.find_element(By.ID, 'kc-register').click()

   # Вводим Имя
   selenium.find_element(By.NAME, 'firstName').send_keys('Йя')
   # Вводим Фамилию
   selenium.find_element(By.NAME, 'lastName').send_keys('И')
   # Вводим Почту
   selenium.find_element(By.ID, 'address').send_keys('sojogo1848@.com')
   # Вводим Пароль
   selenium.find_element(By.ID, 'password').send_keys('fgfgfgfg')
   # Повторяем Пароль
   selenium.find_element(By.ID, 'password-confirm').send_keys('fgfgfgfg')
   # Кликаем по кнопке Зарегистрироваться
   selenium.find_element(By.NAME, 'register').click()

   # Ожидаем, что на странице появятся оповещения о некорректности данных
   # Фамилия
   assert selenium.find_element(By.XPATH,
                                '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/span').text \
          == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."
   # Почта
   assert selenium.find_element(By.XPATH,
                                '//*[@id="page-right"]/div/div/div/form/div[3]/div/span').text \
          == "Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru"
   # Пароль
   assert selenium.find_element(By.XPATH,
                                '//*[@id="page-right"]/div/div/div/form/div[4]/div[1]/span').text \
          == "Пароль должен содержать хотя бы одну заглавную букву"
   # Повтор пароля
   assert selenium.find_element(By.XPATH,
                                '//*[@id="page-right"]/div/div/div/form/div[4]/div[2]/span').text \
          == "Пароль должен содержать хотя бы одну заглавную букву"




# TC_rostelecom_auth_0013
def test_uncorret_data_0013(selenium):
   # Переходим на страницу авторизации
   selenium.get('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=c05af488-19f8-4b74-8368-cffa877f1c97&theme&auth_type')

   # Неявное ожидание
   selenium.implicitly_wait(10)

   # Ожидаем, что заголовок на странице содержит текст "Авторизация"
   assert selenium.find_element(By.CSS_SELECTOR, ".card-container__title").text == "Авторизация"
   # Кликаем по ссылке Зарегистрироваться
   selenium.find_element(By.ID, 'kc-register').click()

   # Вводим Имя
   selenium.find_element(By.NAME, 'firstName').send_keys('Йяй')
   # Вводим Фамилию
   selenium.find_element(By.NAME, 'lastName').send_keys('Илья')
   # Вводим Почту
   selenium.find_element(By.ID, 'address').send_keys('sojogo1848@.com')
   # Вводим Пароль
   selenium.find_element(By.ID, 'password').send_keys('Fgfgfg1')
   # Повторяем Пароль
   selenium.find_element(By.ID, 'password-confirm').send_keys('Fgfgfg1')
   # Кликаем по кнопке Зарегистрироваться
   selenium.find_element(By.NAME, 'register').click()

   # Ожидаем, что на странице появятся оповещения о некорректности данных
   # Почта
   assert selenium.find_element(By.XPATH,
                                '//*[@id="page-right"]/div/div/div/form/div[3]/div/span').text == "Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru"
   # Пароль
   assert selenium.find_element(By.XPATH,
                                '//*[@id="page-right"]/div/div/div/form/div[4]/div[1]/span').text == "Длина пароля должна быть не менее 8 символов"
   # Повтор пароля
   assert selenium.find_element(By.XPATH,
                                '//*[@id="page-right"]/div/div/div/form/div[4]/div[2]/span').text  == "Длина пароля должна быть не менее 8 символов"




# TC_rostelecom_auth_0014
def test_uncorret_data_0014(selenium):
   # Переходим на страницу авторизации
   selenium.get('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=c05af488-19f8-4b74-8368-cffa877f1c97&theme&auth_type')

   # Неявное ожидание
   selenium.implicitly_wait(10)

   # Ожидаем, что заголовок на странице содержит текст "Авторизация"
   assert selenium.find_element(By.CSS_SELECTOR, ".card-container__title").text == "Авторизация"
   # Кликаем по ссылке Зарегистрироваться
   selenium.find_element(By.ID, 'kc-register').click()

   # Вводим Имя
   selenium.find_element(By.NAME, 'firstName').send_keys('Йяй')
   # Вводим Фамилию
   selenium.find_element(By.NAME, 'lastName').send_keys('ИльяИльяИльяИльяИльяИльяИльяИл')
   # Вводим Почту
   selenium.find_element(By.ID, 'address').send_keys('')
   # Вводим Пароль
   selenium.find_element(By.ID, 'password').send_keys('Fgfgfgfg')
   # Повторяем Пароль
   selenium.find_element(By.ID, 'password-confirm').send_keys('Fgfgfgfg')
   # Кликаем по кнопке Зарегистрироваться
   selenium.find_element(By.NAME, 'register').click()

   # Ожидаем, что на странице появятся оповещения о некорректности данных
   # Почта
   assert selenium.find_element(By.XPATH,
                                '//*[@id="page-right"]/div/div/div/form/div[3]/div/span').text \
          == "Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru"
   # Пароль
   assert selenium.find_element(By.XPATH,
                                '//*[@id="page-right"]/div/div/div/form/div[4]/div[1]/span').text \
          == "Пароль должен содержать хотя бы 1 спецсимвол или хотя бы одну цифру"
   # Повтор пароля
   assert selenium.find_element(By.XPATH,
                                '//*[@id="page-right"]/div/div/div/form/div[4]/div[2]/span').text \
          == "Пароль должен содержать хотя бы 1 спецсимвол или хотя бы одну цифру"




# TC_rostelecom_auth_0015
def test_uncorret_data_0015(selenium):
   # Переходим на страницу авторизации
   selenium.get('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=c05af488-19f8-4b74-8368-cffa877f1c97&theme&auth_type')

   # Неявное ожидание
   selenium.implicitly_wait(10)

   # Ожидаем, что заголовок на странице содержит текст "Авторизация"
   assert selenium.find_element(By.CSS_SELECTOR, ".card-container__title").text == "Авторизация"
   # Кликаем по ссылке Зарегистрироваться
   selenium.find_element(By.ID, 'kc-register').click()

   # Вводим Имя
   selenium.find_element(By.NAME, 'firstName').send_keys('Йяй')
   # Вводим Фамилию
   selenium.find_element(By.NAME, 'lastName').send_keys('ИльяИльяИльяИльяИльяИльяИльяИлья')
   # Вводим Почту
   selenium.find_element(By.ID, 'address').send_keys('sojogo1848@wlmycn.com')
   # Вводим Пароль
   selenium.find_element(By.ID, 'password').send_keys('fgfgfgfg')
   # Повторяем Пароль
   selenium.find_element(By.ID, 'password-confirm').send_keys('fgfgfgfg')
   # Кликаем по кнопке Зарегистрироваться
   selenium.find_element(By.NAME, 'register').click()

   # Ожидаем, что на странице появятся оповещения о некорректности данных
   # Фамилия
   assert selenium.find_element(By.XPATH,
                                '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/span').text \
          == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."
   # Пароль
   assert selenium.find_element(By.XPATH,
                                '//*[@id="page-right"]/div/div/div/form/div[4]/div[1]/span').text \
          == "Пароль должен содержать хотя бы 1 спецсимвол или хотя бы одну цифру"
   # Повтор пароля
   assert selenium.find_element(By.XPATH,
                                '//*[@id="page-right"]/div/div/div/form/div[4]/div[2]/span').text \
          == "Пароль должен содержать хотя бы 1 спецсимвол или хотя бы одну цифру"




# TC_rostelecom_auth_0018
def test_using_existing_email_0018(selenium):
   # Переходим на страницу авторизации
   selenium.get('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=c05af488-19f8-4b74-8368-cffa877f1c97&theme&auth_type')

   # Неявное ожидание
   selenium.implicitly_wait(10)

   # Ожидаем, что заголовок на странице содержит текст "Авторизация"
   assert selenium.find_element(By.CSS_SELECTOR, ".card-container__title").text == "Авторизация"
   # Кликаем по ссылке Зарегистрироваться
   selenium.find_element(By.ID, 'kc-register').click()

   # Вводим Имя
   selenium.find_element(By.NAME, 'firstName').send_keys('Йия')
   # Вводим Фамилию
   selenium.find_element(By.NAME, 'lastName').send_keys('Илья')
   # Вводим Почту
   selenium.find_element(By.ID, 'address').send_keys(valid_email)
   # Вводим Пароль
   selenium.find_element(By.ID, 'password').send_keys(valid_password)
   # Повторяем Пароль
   selenium.find_element(By.ID, 'password-confirm').send_keys(valid_password)
   # Кликаем по кнопке Зарегистрироваться
   selenium.find_element(By.NAME, 'register').click()

   # Ожидаем, что на странице появятся оповещения о существовании учетной записи
   assert selenium.find_element(By.CLASS_NAME, 'card-modal__title').text == "Учётная запись уже существует"




# TC_rostelecom_auth_0019
def test_auth_after_unsccssfl_registration_0019(selenium):
    # Переходим на страницу авторизации
    selenium.get('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=c05af488-19f8-4b74-8368-cffa877f1c97&theme&auth_type')

    # Неявное ожидание
    selenium.implicitly_wait(10)

    # Ожидаем, что заголовок на странице содержит текст "Авторизация"
    assert selenium.find_element(By.CSS_SELECTOR, ".card-container__title").text == "Авторизация"
    # Кликаем по ссылке Зарегистрироваться
    selenium.find_element(By.ID, 'kc-register').click()

    # Неявное ожидание
    selenium.implicitly_wait(10)

    # Вводим Имя
    selenium.find_element(By.NAME, 'firstName').send_keys('Йия')
    # Вводим Фамилию
    selenium.find_element(By.NAME, 'lastName').send_keys('Илья')
    # Вводим Почту
    selenium.find_element(By.ID, 'address').send_keys(valid_email)
    # Вводим Пароль
    selenium.find_element(By.ID, 'password').send_keys(valid_password)
    # Повторяем Пароль
    selenium.find_element(By.ID, 'password-confirm').send_keys(valid_password)
    # Кликаем по кнопке Зарегистрироваться
    selenium.find_element(By.NAME, 'register').click()

    # Неявное ожидание
    selenium.implicitly_wait(10)

    # Ожидаем, что на странице появятся оповещения о существовании учетной записи
    assert selenium.find_element(By.CLASS_NAME, 'card-modal__title').text == "Учётная запись уже существует"

    # Кликаем Войти
    selenium.find_element(By.NAME, 'gotoLogin').click()

    # Неявное ожидание
    selenium.implicitly_wait(10)

    # Ожидаем, что заголовок на странице содержит тест "Авторизация"
    assert selenium.find_element(By.CSS_SELECTOR, ".card-container__title").text == "Авторизация"

    # Вводим Почту
    selenium.find_element(By.ID, 'username').send_keys(valid_email)
    # Вводим Пароль
    selenium.find_element(By.ID, 'password').send_keys(valid_password)
    # Клик Войти
    selenium.find_element(By.NAME, 'login').click()

    # Неявное ожидание
    selenium.implicitly_wait(10)

    # Ожидаем, что вход совершен
    assert selenium.find_element(By.CLASS_NAME, 'card-title').text == "Учетные данные"