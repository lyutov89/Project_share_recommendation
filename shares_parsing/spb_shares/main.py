from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


options = Options()
options.add_argument('start-maximized')

driver = webdriver.Chrome(options=options)
actions = ActionChains(driver)

driver.get('https://spbexchange.ru/ru/stocks/index/SPB100/')
assert 'ПАО СПБ Биржа' in driver.title

element = WebDriverWait(driver, 30).until(EC.presence_of_element_located(
    (By.XPATH, "//li[@class='tab-link current']")))

webdriver.ActionChains(driver).move_to_element(element).perform()

element.click()




#driver.quit()