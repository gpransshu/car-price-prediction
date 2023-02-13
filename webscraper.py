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
#driver.refresh()
wait = WebDriverWait(driver, 10)
#wait.until(EC.visibility_of_all_elements_located(By.CLASS_NAME, "gsc_col-xs-12 gsc_col-sm-6 gsc_col-md-6 gsc_col-lg-4"))
#wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "li.gsc_col-md-6:nth-child(1)")))

products = []

#product = driver.find_elements((By.CSS_SELECTOR, "li.gsc_col-md-6:nth-child(1)"))

#element = driver.find_element(By.PARTIAL_LINK_TEXT, "BMW")
element = driver.find_elements(By.XPATH, "/html/body/div[2]/div/div[1]/div/main/div/div[1]/ul/li[1]")
#class_name = element.get_attribute("class")
for i in element:
    print(i.text)
#print(class_name)

'''
for p in product:
    a = p.find_element(By.CSS_SELECTOR,"li.gsc_col-md-6:nth-child(1) > div:nth-child(1) > div:nth-child(2)")#title
    print(a.text)
    #for elem in a:
    #    print("Title",elem.text)
'''