import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument('start-maximized')

driver = webdriver.Chrome(options=options)

driver.get('https://spbexchange.ru/ru/stocks/index/SPB100/')
assert 'ПАО СПБ Биржа' in driver.title

driver.execute_script("window.scrollTo(0, 500)")

element = WebDriverWait(driver, 30).until(EC.presence_of_element_located(
    (By.XPATH, "//ul/li[@data-tab='tab-2']")))

element.click()

tickers = driver.find_elements(By.XPATH, "//tr/td[2]")
company_names = driver.find_elements(By.XPATH, "//tr/td[3]")
ISIN = driver.find_elements(By.XPATH, "//tr/td[4]")


def get_list_from_table(column):
    list_el = []
    for i in column:
        spam = i.text
        list_el.append(spam)

    return list_el


tickers_spb = pd.Series(get_list_from_table(tickers))
company_spb = pd.Series(get_list_from_table(company_names))
ISIN_spb = pd.Series(get_list_from_table(ISIN))

data_spb_100 = {'tickers': tickers_spb,
                'name_company': company_spb,
                'ISIN': ISIN_spb}

df = pd.DataFrame(data_spb_100)

print(df.head())

#сохраним таблицу в csv

file_name = 'spb100.csv'

df.to_csv(file_name, encoding='utf-8', index=False)

driver.quit()
