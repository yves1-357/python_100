promissed_down = 150
promissed_up = 10
twitter_email = yvinho2024@gmail.com
twiter_pass = ptCZmxHUVrlup_UT

SIMILAR_ACCOUNT = "chefsteps"   # the account whose followers you'll follow
USERNAME = "your_email"       # your Share-a-Naan (or Instagram) username (your email)
PASSWORD = "your_pw"   
BASE_URL = "https://app.100daysofpython.dev/services/share-a-naan"   # If using the mock
LOGIN_URL = f"{BASE_URL}/login"

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get("https://www.speedtest.net/fr")
element = driver.find_element(By.CLASS_NAME, "data-ad-slot")
elementCents = driver.find_element(By.CLASS_NAME, "data-ad-slot")
print(f"Alerte, le prix est à {element.text}.{elementCents.text}")

driver.quit() 


