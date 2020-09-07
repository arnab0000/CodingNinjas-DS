from selenium import webdriver
path = '/usr/local/bin/chromedriver'
driver = webdriver.Chrome(executable_path=path)
driver.get('https://www.codingninjas.in/')
print(driver.title)
driver.back()
driver.forward()
driver.save_screenshot('test_shot.png')