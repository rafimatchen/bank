from selenium import webdriver
from selenium.webdriver.common.by import By
import tomllib

with open("config.toml", "rb") as f:
    config = tomllib.load(f)

driver = webdriver.Chrome()

driver.get(config["url"])

title = driver.title

driver.implicitly_wait(5)

username_input = driver.find_element(by=By.ID, value="username")
password_input = driver.find_element(by=By.ID, value="uapPassword")

submit_button = driver.find_element(
    by=By.CSS_SELECTOR, value="button.btn.btn-block.td-button-secondary"
)

username_input.send_keys(config["login"])
password_input.send_keys(config["password"])
submit_button.click()

accounts_button = driver.find_elements(by=By.CSS_SELECTOR, value="td-wb-menu-item")[1]
accounts_button.click()

holdings_button = driver.find_element(by=By.CSS_SELECTOR, value='[href="#/page/account/holdings"]')
holdings_button.click()

export_button = driver.find_element(by=By.CSS_SELECTOR, value="td-wb-toolbar-item-export")
export_button.click()

csv_button = driver.find_element(by=By.ID, value="td-wb-toolbar-item-export-CSV")
csv_button.click()

input()