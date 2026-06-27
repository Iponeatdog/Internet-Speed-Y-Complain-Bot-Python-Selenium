import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

PROMISED_DOWN = 1000
PROMISED_UP = 1000
Y_EMAIL = "@gmail.com"
Y_PASSWORD = ""
Y_LOGIN_URL = "https://app.100daysofpython.dev/services/y#"
INTERNET_SPEED_URL = "https://fast.com/"

class InternetSpeedTwitterBot:
    def __init__(self):
        self.speed = 0
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.wait = WebDriverWait(self.driver, 10)

    def get_internet_speed(self):
        self.driver.get(INTERNET_SPEED_URL)
        self.speed = self.wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, "div.speed-results-container.succeeded"))).text

    def tweet_at_provider(self):
        self.driver.get(Y_LOGIN_URL)
        time.sleep(2)
        y_login = self.wait.until(ec.element_to_be_clickable((By.CLASS_NAME, "y-login-link")))
        y_login.click()

        email = self.wait.until(ec.presence_of_element_located((By.NAME, "email")))
        email.send_keys(Y_EMAIL)
        password = self.driver.find_element(By.NAME, value="password")
        password.send_keys(Y_PASSWORD)
        submit_btn = self.driver.find_element(By.CLASS_NAME, value="y-login-submit")
        submit_btn.click()

        post_text = self.wait.until(ec.presence_of_element_located((By.CLASS_NAME, "x-compose")))
        post_text.send_keys(f"Hey Internet Provider, why is my speed {self.speed} when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?!")
        post_btn = self.driver.find_element(By.ID, value="post-btn")
        post_btn.click()
