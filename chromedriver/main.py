from selenium import webdriver
import configparser
import time
import random

userAgents = [
    "Hello from C!",
    "best of the best",
    "another world"
]

#  Читаем настройки программы
config = configparser.ConfigParser()  # создаём объекта парсера
config.read("../settings.ini")  # читаем конфиг

# Settings
OS: str = config["OperatingSystem"]["OS"]
siteUrl: str = config["Chrome"]["site_url"]
driverPath: str = config["Chrome"]["driver_url"]
# userAgent: str = config["Chrome"]["user_agent"]

print("driverPath: " + driverPath)
print("siteUrl: " + siteUrl)
print("OS: " + OS)
# print("userAgent: " + userAgent)

# Options
options = webdriver.ChromeOptions()
# options.add_argument("user-agent=" + userAgent)
options.add_argument(f"user-agent={random.choice(userAgents)}")

#  Распарсить путь для ОС  Windows так:
# "C:\\users\\LearningSelenium\\chromedriver\\chromedriver.exe"
#  или так ( синтаксис сырой строки):  r"C:\users\LearningSelenium\chromedriver\chromedriver.exe"
if OS == "Windows":
    print("It is Windows")
else:
    print("It is not Windows")

driver = webdriver.Chrome(
    executable_path=driverPath,
    options=options
)

try:
    # driver.get(url=siteUrl)
    # driver.save_screenshot("Screenshot1.png")
    # time.sleep(3)

    # Проверка юзерагента
    driver.get("https://whatismybrowser.com/detect/what-is-my-user-agent")
    driver.save_screenshot("UserAgent.png")
    time.sleep(3)
except Exception as ex:
    print("Error message:")
    print(ex)
finally:
    driver.close()
    driver.quit()
