import time

from selenium.webdriver import Edge
from selenium.webdriver.common import keys,by


web=Edge()

web.get('http://lagou.com')


web.find_element(by.By.XPATH,'//*[@id="cboxClose"]').click()

time.sleep(1)

web.find_element(by.By.XPATH,'//*[@id="search_input"]').send_keys('python',keys.Keys.ENTER)

time.sleep(1)

web.find_element(by.By.XPATH,'//*[@id="openWinPostion"]').click()

time.sleep(1)

web.switch_to.window(web.window_handles[-1])

time.sleep(1)
intr=web.find_element(by.By.XPATH,'//*[@id="job_detail"]/dd[2]').text

print(intr)
web.close()

web.switch_to.window(web.window_handles[0])

time.sleep(20)