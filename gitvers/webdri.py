from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service
from selenium.webdriver.chrome.options import Options
from time import sleep
URL = "https://docs.google.com/forms/d/e/1FAIpQLSc9wqcS-lget4dsuGuX26-LT-pHla558_nL3Cc032N1gr9Syg/viewform?usp=sf_link"
path = "/Users/utkuozer/chromedriver"


class WebDriverr:
    
    def sendkeys(self,a,b,c):
        optns = webdriver.ChromeOptions()
        optns.add_experimental_option("detach",True)
        driver = webdriver.Chrome(options=optns,executable_path=path)
        driver.get(URL)
        sleep(2)
        driver.find_element(By.XPATH,'/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(a)
        driver.find_element(By.XPATH,'/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(b)
        driver.find_element(By.XPATH,'/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(c)
        driver.find_element(By.CLASS_NAME,"NPEfkd").click()