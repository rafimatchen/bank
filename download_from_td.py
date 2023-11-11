from selenium import webdriver
from selenium.webdriver.common.by import By

import config

URL = "https://wb.authentication.td.com/uap-ui/?consumer=webbroker&locale=en_CA#/uap/login"

config = config.get_config()

driver = webdriver.Chrome()

driver.get(URL)
driver.maximize_window()

title = driver.title

driver.implicitly_wait(5)

username_input = driver.find_element(by=By.ID, value="username")
password_input = driver.find_element(by=By.ID, value="uapPassword")

submit_button = driver.find_element(
    by=By.CSS_SELECTOR, value="button.btn.btn-block.td-button-secondary"
)

username_input.send_keys(config["td_login"])
password_input.send_keys(config["td_password"])
submit_button.click()

accounts_button = driver.find_elements(by=By.CSS_SELECTOR, value="td-wb-menu-item")[1]
accounts_button.click()

holdings_button = driver.find_element(
    by=By.CSS_SELECTOR, value='[href="#/page/account/holdings"]'
)
holdings_button.click()

export_button = driver.find_element(
    by=By.CSS_SELECTOR, value="td-wb-toolbar-item-export"
)
export_button.click()

csv_button = driver.find_element(by=By.ID, value="td-wb-toolbar-item-export-CSV")
csv_button.click()

input()
