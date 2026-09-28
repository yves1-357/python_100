promissed_down = 150
promissed_up = 10
twitter_email = yvinho2024@gmail.com
twiter_pass = ptCZmxHUVrlup_UT

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


