from selenium import webdriver
chromedriver = r'C:\Users\haneef\PycharmProjects\nani\venv\code\chromedriver_win32\browers\chromedriver.exe'
driver=webdriver.Chrome(chromedriver)
driver.get('https://temp-mail.org/en/')
driver.find_element_by_xpath('//*[@id="mail"]').click()

#driver.send_keys(Keys.CONTROL, 'a') #highlight all in box
driver.send_keys(Keys.CONTROL, 'c') #copy
#driver.send_keys(Keys.CONTROL, 'v') #paste
