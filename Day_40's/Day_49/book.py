from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep,time
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
options = Options()

options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get("https://appbrewery.github.io/gym/login/")

# Find a search <input> by name
wait = WebDriverWait(driver, 2)
search_Email = wait.until(ec.element_to_be_clickable((By.ID, "email-input")))
name = "student@test.com"
search_Email.clear()
# for lettre in name:
search_Email.send_keys(name)
    # time.sleep(0.1)


search1_Pass = wait.until(ec.element_to_be_clickable((By.ID, "password-input")))
password = "password123"
search1_Pass.clear()
# for letter in password:
search1_Pass.send_keys(password)
    # sleep(0.1)

Login = driver.find_element(By.ID, "submit-button")
Login.click()
# driver.execute_script("arguments[0].click();", Login)
# driver.execute_script("arguments[0].click();", Login)






















# element = driver.find_element(By.XPATH, '//*[@id="mwDw"]')
# print(f"{element.text}")

# # FIND an element by linkText
# all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")