from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome(r'C:\Users\haneef\PycharmProjects\nani\venv\code\chromedriver_win32\browers\chromedriver.exe')
driver.set_window_size(720, 640)
#driver.set_window_size(1920, 1080)
time.sleep(1)
size = driver.get_window_size()
print("Window size: width = {}px, height = {}px.".format(size["width"], size["height"]))
time.sleep(4)
driver.close()