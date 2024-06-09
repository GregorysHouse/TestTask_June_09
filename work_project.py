from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
form_url = 'https://demoqa.com/automation-practice-form' 
driver.get(form_url)


driver.find_element(By.ID, 'firstName').send_keys('John')
driver.find_element(By.ID, 'lastName').send_keys('Doe')
driver.find_element(By.ID, 'userEmail').send_keys('john.doe@example.com')

driver.find_element(By.XPATH, '//*[@id="genterWrapper"]/div[2]/div[1]').click()

driver.find_element(By.ID, "userNumber").send_keys('9777777777')

driver.find_element(By.ID, 'dateOfBirthInput').click()

year_select = driver.find_element(By.XPATH, '//select[@class="react-datepicker__year-select"]')
year_select.click()
year_select.find_element(By.XPATH, '//option[@value="2000"]').click()

month_select = driver.find_element(By.XPATH, '//select[@class="react-datepicker__month-select"]')
month_select.click()
month_select.find_element(By.XPATH, '//option[@value="5"]').click()  # Июнь имеет индекс 5

driver.find_element(By.XPATH, '//div[contains(@class, "react-datepicker__day") and text()="8"]').click()

driver.find_element(By.ID, 'subjectsInput').send_keys('Maths')
driver.find_element(By.ID, 'subjectsInput').send_keys(Keys.RETURN)


hobbie_sport_element= driver.find_element(By.ID, 'hobbies-checkbox-1')
hobbie_reading_element= driver.find_element(By.ID, 'hobbies-checkbox-2')

driver.execute_script("arguments[0].click();", hobbie_sport_element)
driver.execute_script("arguments[0].click();", hobbie_reading_element)


driver.find_element(By.ID, 'uploadPicture').send_keys('/Users/Greg/Downloads/photo_2024-06-07 9.11.35 PM.jpeg')


driver.find_element(By.ID, 'currentAddress').send_keys('Tverskaya 12, 35')

dropdown = driver.find_element(By.ID, "react-select-3-input")
driver.execute_script("arguments[0].click();", dropdown)

dropdown.send_keys('NCR')
dropdown.send_keys(Keys.RETURN)


dropdown = driver.find_element(By.ID, "react-select-4-input")
driver.execute_script("arguments[0].click();", dropdown)

dropdown.send_keys('Delhi')
dropdown.send_keys(Keys.RETURN)

time.sleep(5)

driver.find_element(By.ID, 'submit').click()

time.sleep(5)
driver.quit()