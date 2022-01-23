#!/usr/bin/python3
import web_driver_configuration
from selenium.webdriver.common.by import By

# Call driver passing the url and driver name (firefox / chrome) as arguemnts
driver = web_driver_configuration.define_driver(
    "http://localhost/", "firefox")

# HOTELO PMS AUTOMATIC TESTS ---Can replace with other tests starting here---

# Login function
def login(username, password):
    # Finding the username input field
    username_input = driver.find_element(By.NAME, "username")

    # Finding the password input field
    password_input = driver.find_element(By.NAME, "pw")

    # Finding the submission button
    submit_button = driver.find_element(By.CLASS_NAME, "test")

    # Entering the receptionist username
    username_input.send_keys(username)

    # Entering the receptionist password
    password_input.send_keys(password)

    # Submitting the form
    submit_button.click()


def logout():
    # Find the user dropdown and click
    user_dropdown = driver.find_element(By.CLASS_NAME, "dropdown")
    user_dropdown.click()

    # Find the login button
    logout_button = driver.find_element(By.CLASS_NAME, "button")
    logout_button.click()


# Testing login "Receptionist"
# Enter username then password here:
login('xx', 'xx')

# Testing logout
logout()

# Login again
login('xx', 'xx')
