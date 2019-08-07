from selenium import webdriver
driver=webdriver.Chrome()
driver.maximize_window()

driver.implicitly_wait(10)

driver.get('http://ms.advt.sfc.com/login')
'''
#driver.find_element_by_xpath('//*[@id="app"]/div/form/div[3]/div/button').click()
driver.find_element_by_xpath('//*[@id="app"]/div/form/div[3]/div/button').send_keys('123')
'''
driver.find_element_by_name('username').click()
driver.implicitly_wait(3)
driver.find_element_by_name('username').clear()
driver.find_element_by_name('username').send_keys("guanshuxin")
driver.implicitly_wait(3)
driver.find_element_by_name('password').click()
driver.implicitly_wait(3)
driver.find_element_by_name('password').clear()
driver.find_element_by_name('password').send_keys("123456")
driver.implicitly_wait(3)
driver.find_element_by_xpath('//*[@id="app"]/div/form/div[3]/div/button').click()
driver.implicitly_wait(3)
driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div[1]/div/ul/div[2]/li/div').click()
driver.implicitly_wait(3)