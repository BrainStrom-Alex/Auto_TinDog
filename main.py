from selenium import webdriver
from selenium.common import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import os
from time import sleep

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://app.100daysofpython.dev/services/tindog/u/RNVp6FvR7PIjAWkFeso8YaLdcHjQhHPG")

wait = WebDriverWait(driver, 2)

base_window = driver.window_handles[0]

login_button = wait.until(ec.element_to_be_clickable(driver.find_element(By.CSS_SELECTOR, value="button[type^='button']")))
login_button.click()

facebook_login_button = wait.until(ec.element_to_be_clickable(driver.find_element(By.CSS_SELECTOR, value=".tindog-modal button")))
facebook_login_button.click()

fb_login_page = driver.window_handles[1]
driver.switch_to.window(fb_login_page)

email_button = wait.until(ec.element_to_be_clickable(driver.find_element(By.ID, value="email")))
email_button.send_keys("testing.brainstrom@gmail.com")

password_button = wait.until(ec.element_to_be_clickable(driver.find_element(By.ID, value="pass")))
password_button.send_keys("abc")

fb_login_button = driver.find_element(By.CSS_SELECTOR, value=".login-card button")
fb_login_button.click()

driver.switch_to.window(base_window)

location_button = driver.find_element(By.CSS_SELECTOR, value=".popup-card button")
location_button.click()

enable_notification = wait.until(ec.element_to_be_clickable(driver.find_element(By.XPATH, value='/html/body/main/div/div/form/button[2]')))
enable_notification.click()

cookies = wait.until(ec.element_to_be_clickable(driver.find_element(By.XPATH, value='/html/body/main/div/div/form/button')))
cookies.click()

for n in range(20):
    sleep(1)
    try:
        like_button = driver.find_element(By.CLASS_NAME, value='btn-like')
        like_button.click()
    except ElementClickInterceptedException:
        # Match popup is in the way — dismiss it and continue
        try:
            driver.find_element(By.CSS_SELECTOR, value='.match-popup a').click()
        except NoSuchElementException:
            sleep(2)
    except NoSuchElementException:
        # Like button not loaded yet OR all dogs have been swiped — wait and retry
        sleep(2)