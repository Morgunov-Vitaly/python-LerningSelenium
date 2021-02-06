from selenium import webdriver
import configparser
import time
import random

userAgents = [
    "Hello from F!",
    "best of the best",
    "another world"
]

#  Читаем настройки программы
config = configparser.ConfigParser()
config.read("./../settings.ini")

# Settings
OS: str = config["OperatingSystem"]["OS"]
siteUrl: str = config["Firefox"]["site_url"]
driverPath: str = config["Firefox"]["driver_url"]
# userAgent: str = config["Firefox"]["user_agent"]

# Options
options = webdriver .FirefoxOptions()
# options.add_argument("user-agent=" + userAgent)
options.add_argument(f"user-agent={random.choice(userAgents)}")

# print("driverPath: " + driverPath)
# print("siteUrl: " + siteUrl)
# print("OS: " + OS)
# print("userAgent: " + userAgent)

#  Распарсить путь для ОС  Windows так:
# C:\\users\\LearningSelenium\\chromedriver\\chromedriver.exe
#  или так ( синтаксис сырой строки):  r"C:\users\LearningSelenium\chromedriver\chromedriver.exe"
# if OS == "Windows":
#     print("It is Windows")
# else:
#     print("It is not Windows")

driver = webdriver.Firefox(
    executable_path=driverPath,
    options=options
)

try:
    # driver.get(url=siteUrl)
    # driver.save_screenshot("Screenshot.png")
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
