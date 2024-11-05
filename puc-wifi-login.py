import configparser
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from datetime import datetime

# Load configuration
config = configparser.ConfigParser()
config.read('config.ini')

username = config['settings']['username']
password = config['settings']['password']
geckodriver_path = config['settings']['geckodriver_path']
config_schedule = config['settings'].getboolean('config_schedule')
schedule_days = list(map(int, config['settings']['schedule_days'].split(',')))
start_hour = int(config['settings']['start_hour'])
end_hour = int(config['settings']['end_hour'])

# Define the allowed days and time range
def within_schedule():
    # Check if schedule should be applied based on config_schedule setting
    if not config_schedule:
        return True  # Always allow if configSchedule is False

    current_time = datetime.now()

    # Check if today is within the allowed schedule days
    today = current_time.weekday()  # Monday=0, Sunday=6
    is_allowed_day = today in schedule_days

    # Check if the current time is within the allowed hour range
    in_time_range = start_hour <= current_time.hour < end_hour

    return is_allowed_day and in_time_range

# Run only if within schedule
if within_schedule():
    print("Running script...")

    geckodriver_path = '/usr/local/bin/geckodriver'
    service = Service(executable_path=geckodriver_path)

    # Adding the headless argument so it runs without a GUI
    # Adicionando o argumento headless para rodar sem GUI
    options = Options()
    options.add_argument("--headless")

    driver = webdriver.Firefox(service=service, options=options)

    driver.get("https://www.google.com")
    WebDriverWait(driver, 3)

    try:
        # Seleção e preenchimento do campo de usuário e senha
        # Username and password field identification and filling
        username_field = driver.find_element(By.ID, "ft_un")
        username_field.send_keys(username)

        password_field = driver.find_element(By.ID, "ft_pd")
        password_field.send_keys(password)
    except TimeoutException:
        print("Timeout waiting for the username or password field to be available.")

    try:
        submit_button = driver.find_element(By.CSS_SELECTOR, "button.primary")
        submit_button.click()
    except TimeoutException:
        print("Failed to submit data: the submit button was not found or did not load within the expected time.")

    print("Login OK!")
    driver.quit()

else:
    print("Outside of allowed schedule. Script will not run.")
