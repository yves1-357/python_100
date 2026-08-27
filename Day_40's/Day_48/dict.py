from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get("https://www.python.org/")
element = driver.find_elements(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li')
events_direct = {}
for i in range(len(element)):
    text_complet = element[i].text
    données_events = text_complet.split("\n")
    events_direct[i] = {"Time": données_events[0], "Name": données_events[1]}

print(events_direct)





driver.quit()