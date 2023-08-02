import time

from selenium.webdriver import Edge
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import select
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.edge.options import Options


opt=Options()

opt.add_argument('--headless')

web=Edge()

web.get('https://star.endata.com.cn/Star/Search')
time.sleep(1)

print(web.find_element(By.XPATH,'//*[@id="app"]/section/main/div/div[1]/div/section/div[3]/ul/li[1]/section[1]').text)


print('========================================')






time.sleep(60)