from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get("https://appbrewery.github.io/fake-newsletter-signup/")
# element = driver.find_element(By.XPATH, '//*[@id="mwDw"]')
# print(f"{element.text}")

# # FIND an element by linkText
# all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")

# Find a search <input> by name
search = driver.find_element(By.NAME, value="fName")
search1 = driver.find_element(By.NAME, value="lName")
search2 = driver.find_element(By.NAME, value="email")
search3 = driver.find_element(By.CLASS_NAME, value="btn-block")

# Find, sending keyboard input
search.send_keys("Honda")
search1.send_keys("deani")
search2.send_keys("Honda@gmail.com")
search3.click()
