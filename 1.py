from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options as options
from selenium.webdriver.firefox.options import Options as Firefox_Options
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.ui import WebDriverWait

firefox_options = Firefox_Options()
firefox_options.binary = r'C:\Program Files\Mozilla Firefox\firefox.exe';
driver = webdriver.Firefox(executable_path=r'D:\github\HelloWorld\geckodriver.exe',options=firefox_options)
url = "https://www.cardekho.com/latestcars"
driver.get(url)

driver.refresh()
#wait = WebDriverWait(driver, 10)
#element = wait.until(EC.visibility_of_element_located(By.CSS_SELECTOR,"li.gsc_col-md-6"))

wait = WebDriverWait(driver, 20)
wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,"li.gsc_col-md-6")))

car_elements = driver.find_elements(By.CSS_SELECTOR,"li.gsc_col-md-6")

# Print the text of each car element
for car in car_elements:
    
    print(car.text)