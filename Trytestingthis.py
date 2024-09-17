from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://trytestingthis.netlify.app/")


driver.find_element(By.ID,"fname").send_keys("Nafis")
time.sleep(2)
driver.find_element(By.ID,"lname").send_keys("Ulfat")
time.sleep(2)
driver.find_element(By.ID,"male").click()
time.sleep(2)
driver.find_element(By.ID,"option").click()
time.sleep(2)
driver.find_element(By.XPATH,"//select[@id='option']//option[@value='option'][normalize-space()='Option']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//select[@id='owc']//option[@value='option 2'][normalize-space()='Option 2']").click()
time.sleep(2)
driver.find_element(By.ID,"moption").click()
time.sleep(2)
driver.find_element(By.XPATH,"//textarea[@name='message']").send_keys("The kids ran across the field, laughing with joy.")
time.sleep(2)
driver.find_element(By.XPATH,"//button[normalize-space()='Submit']").click()
time.sleep(2)

driver.quit()
print("Successfully processed")