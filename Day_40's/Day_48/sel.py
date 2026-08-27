from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get("https://www.amazon.com.be/-/en/SONGMICS-Adjustable-Continuous-Adjustment-LSD136Y01/dp/B0DNSLWKFX?ref_=BrandDays-SONGMICS-Best_B0DNSLWKFX")
element = driver.find_element(By.CLASS_NAME, "a-price-whole")
elementCents = driver.find_element(By.CLASS_NAME, "a-price-fraction")
print(f"Alerte, le prix est à {element.text}.{elementCents.text}")

driver.quit() 




# # driver.close() ---> ferme le tab
# driver.quit() // ferme tt le navigateur/program
# XPATH = locates html element by path structure ( //*[@id="locating-elements-by-class-name"]/h2)