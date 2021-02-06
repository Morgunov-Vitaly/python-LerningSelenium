from selenium import webdriver
import configparser
import time
from datetime import datetime
# https://pypi.org/project/fake-useragent/ pip install fake-useragent
from fake_useragent import UserAgent

useragent = UserAgent()


def get_file_name():
    now = datetime.now()
    return f"{now.year}-{now.month}-{now.day}_{now.hour}-{now.minute}-{now.second}_user_agent.png"


#  Читаем настройки программы
config = configparser.ConfigParser()
config.read("./../settings.ini")

# Settings
OS: str = config["OperatingSystem"]["OS"]
siteUrl: str = config["Firefox"]["site_url"]
driverPath: str = config["Firefox"]["driver_url"]

# Options
options = webdriver.FirefoxOptions()
# set_preference vs add_argument в Chrome
options.set_preference("general.useragent.override", useragent. random)
# Возможны варианты:
#  Просто строка "Hello!"
# Вариации браузера opera: useragent.opera
# Полностью рандомные варианты  useragent.random


driver = webdriver.Firefox(
    executable_path=driverPath,
    options=options
)

try:
    # Проверка юзерагента
    driver.get("https://whatismybrowser.com/detect/what-is-my-user-agent")

    driver.save_screenshot(get_file_name())
    time.sleep(3)
except Exception as ex:
    print("Error message:")
    print(ex)
finally:
    driver.close()
    driver.quit()
