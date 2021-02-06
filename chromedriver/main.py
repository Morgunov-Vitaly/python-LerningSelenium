from selenium import webdriver
import configparser
import time
# https://pypi.org/project/fake-useragent/ pip install fake-useragent
from fake_useragent import UserAgent
from datetime import datetime

useragent = UserAgent()

#  Читаем настройки программы
config = configparser.ConfigParser()  # создаём объекта парсера
config.read("../settings.ini")  # читаем конфиг

# Settings
OS: str = config["OperatingSystem"]["OS"]
siteUrl: str = config["Chrome"]["site_url"]
driverPath: str = config["Chrome"]["driver_url"]

# Options
options = webdriver.ChromeOptions()
options.add_argument(f"user-agent={useragent.random}")
# Возможны варианты:
# Вариации браузера opera: useragent.opera
# Полностью рандомные варианты  useragent.random

driver = webdriver.Chrome(
    executable_path=driverPath,
    options=options
)


def get_file_name():
    now = datetime.now()
    return f"{now.year}-{now.month}-{now.day}_{now.hour}-{now.minute}-{now.second}_user_agent.png"


try:
    # Проверка юзерагента
    driver.get("https://whatismybrowser.com/detect/what-is-my-user-agent")
    filename = get_file_name()
    driver.save_screenshot(filename)
    time.sleep(3)
except Exception as ex:
    print("Error message:")
    print(ex)
finally:
    driver.close()
    driver.quit()
