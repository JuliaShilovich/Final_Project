Тестовые сценарии проверяют допустимые и недопустимые значения полей ввода в формах регистрации и авторизации, возможность изменения учетных данных и возможность входа через почту при выборе кнопок "Логин" и "Телефон".

Для проведения тестов применяется браузер Chrome и webdriver https://chromedriver.chromium.org/downloads. Для запуска тестов применяется команда pytest -v --driver Chrome --driver-path <driver path>\chromedriver.exe

Валидные данные (почта и пароль) вынесены в отдельный файл .env и не выгружены в GitHub. Предлагаю использовать свои данные :)