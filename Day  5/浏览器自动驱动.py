import time

from selenium.webdriver import Edge

from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys


web=Edge(keep_alive='True')
web.get('http://lagou.com')

el=web.find_element(By.XPATH,value='//*[@id="changeCityBox"]/p[1]/a')
el.click()

time.sleep(1)

web.find_element(By.XPATH,'//*[@id="search_input"]').send_keys('python',Keys.ENTER)

time.sleep(2)
div_list=web.find_elements(By.XPATH,'//*[@id="jobList"]/div[1]/div')

for div in div_list:
     job=div.find_element(By.XPATH,'//*[@id="openWinPostion"]').text
     company=div.find_element(By.XPATH,'./div[1]/div[2]/div[1]/a').text
     money=div.find_element(By.CLASS_NAME,'money__3Lkgq').text
     print(job,company,money)








