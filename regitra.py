import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options


userId = input("Iveskite Swedbank naudotojo ID: ")
identityNumber = input("Iveskite asmens koda: ")
raides = input("Iveskite norimu numeriu raides: ")
skaiciai = input("Iveskite norimu numeriu skaicius: ")


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
os.environ['PATH'] += r"C:/SeleniumDrivers"
driver = webdriver.Chrome()

driver.get("https://www.eregitra.lt/eketris-web/faces/pages/common/Login.xhtml")

driver.maximize_window()
driver.implicitly_wait(500)

driver.find_element_by_xpath("/html/body/div/div[2]/div/div[1]/div[2]/span/div/a").click()

# Get current tab
current_tab = driver.current_window_handle

# Get list of all tabs
tabs = driver.window_handles

for tab in tabs:
    # switch focus to each open tab one by one
    if tab != current_tab:
        # Switch to tab
        driver.switch_to.window(tab)

        # Get tab name
        title = driver.title


#El. Vartai

driver.find_element_by_xpath("/html/body/div/div[4]/div[2]/div/div[3]/div/div/div/div[2]/div/div[1]").click()

driver.find_element_by_xpath("/html/body/div[1]/div[4]/div[2]/div/div[3]/div/div[1]/div/div/div[1]/div/div[2]/div/div[1]/div[1]/a").click()

# Swedbank

driver.find_element_by_xpath("/html/body/ui-cookie-consent/ui-modal/div[2]/div/div/div/div/button[1]").click()

#sendkeys ID ir asmens kodas

driver.find_element_by_name("userId").send_keys(userId)

driver.find_element_by_name("identityNumber").send_keys(identityNumber)

driver.find_element_by_class_name("-positive").click()

driver.find_element_by_xpath("//button[@onclick=\"linkAction('private.home.more.eservices.redirect.e-government','eServiceId','e-government','','','','eService');\"]").click()

# Get current tab
current_tab = driver.current_window_handle

# Get list of all tabs
tabs = driver.window_handles

for tab in tabs:
    # switch focus to each open tab one by one
    if tab != current_tab:
        # Switch to tab
        driver.switch_to.window(tab)
        # Get tab name
        title = driver.title

# el. valdzios vartai [gyventojas ar rezidentas]

driver.find_element_by_xpath("/html/body/div[1]/div[4]/div[2]/div/div[1]/div[2]/div/div/div[3]/div/button").click()

# eregitra [rezervuoti numerio zenklus]

driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[2]/form/ul[2]/li/a").click()
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div[1]/form[1]/div[8]/div[2]/ul/li[1]/a").click()

# eregitra [1. pasirinkti numerio zenklu grupe]

driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div[1]/form[1]/table/tbody/tr[2]/td/span/select/option[2]").click()
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div[1]/form[1]/span[5]/table/tbody/tr[2]/td/span/select/option[2]").click()
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div[1]/form[1]/span[6]/table/tbody/tr[2]/td/span/select/option[2]").click()
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div[1]/form[1]/span[7]/table/tbody/tr[2]/td/span/span/div/div[1]/div/table/tbody/tr[1]/td/input").click()
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div[1]/form[1]/span[9]/table/tbody/tr[2]/td/div/button/span").click()


# eregitra [numerio paieska]

driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[1]/form[1]/div[2]/span[1]/table/tbody/tr/td[2]/div/input").send_keys(raides)
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[1]/form[1]/div[2]/span[1]/table/tbody/tr/td[4]/input").send_keys(skaiciai)
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[1]/form[1]/div[2]/span[2]/span/button").click()
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[1]/form[1]/span/div[2]/div/div/table/tbody/tr/td[1]/div/input").click()
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[1]/form[1]/span/span[2]/span/button").click()
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div[1]/form[1]/span[11]/table/tbody/tr[2]/td/span/span/div/div[1]/select/option[12]").click()
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div[1]/form[1]/div[2]/div/a/span[1]").click()
time.sleep(5000)
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div[1]/form[1]/div[3]/input").click()
time.sleep(5000)
