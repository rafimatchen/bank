from selenium import webdriver
from selenium.webdriver.common.by import By
import tomllib

with open("config.toml", "rb") as f:
    config = tomllib.load(f)

driver = webdriver.Chrome()

driver.get(config["url"])

title = driver.title

driver.implicitly_wait(0.5)

username_input = driver.find_element(by=By.ID, value="username")
password_input = driver.find_element(by=By.ID, value="uapPassword")

submit_button = driver.find_element(
    by=By.CSS_SELECTOR, value="button.btn.btn-block.td-button-secondary"
)

username_input.send_keys(config["login"])
password_input.send_keys(config["password"])
submit_button.click()

input()
