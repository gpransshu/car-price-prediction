from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options as options
from selenium.webdriver.firefox.options import Options as Firefox_Options
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import WebDriverWait

firefox_options = Firefox_Options()
firefox_options.binary = r'C:\Program Files\Mozilla Firefox\firefox.exe';
driver = webdriver.Firefox(executable_path=r'D:\github\HelloWorld\geckodriver.exe',options=firefox_options)
url = "https://www.cardekho.com/electric-cars"
driver.get(url)
driver.refresh()
wait = WebDriverWait(driver, 10)
time.sleep(10)
#wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "gsc_col-xs-12 gsc_col-sm-6 gsc_col-md-6 gsc_col-lg-4 desktop conatntVisable")))

products = []
product = driver.find_elements(By.CLASS_NAME,"desktopWrapper gsc_row  gsc_container_hold")
for p in product:
    a = p.find_element(By.CLASS_NAME,"gsc_col-xs-12 holder truncate")
    print(a.text)
