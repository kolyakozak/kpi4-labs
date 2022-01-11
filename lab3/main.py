from selenium import webdriver
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

URL = 'http://www.fb.com'
REDIRECT_URL='https://www.facebook.com/'

#user_data
first_name = 'Jack'
last_name = 'Johanson'
email = 'jack.johansoooonnnnn1999@gmail.com'
password = 'johndalton123456!@'
gender = 'male'
birth_day = '13'
birth_month = 'Jun'
birth_year = '1999'

#xpath
create_account_xpath = '//a[@class="_42ft _4jy0 _6lti _4jy6 _4jy2 selected _51sy"]'
sign_up_button_xpath = '//button[@class="_6j mvm _6wk _6wl _58mi _3ma _6o _6v"]'
verification_email_form_xpath = '//span[@class="d2edcug0 hpfvmrgz qv66sw1b c1et5uql b0tq1wua a8c37x1j fe6kdd0r mau55g9w c8b282yb keod5gw0 nxhoafnm aigsh9s9 d3f4x2em rwim8176 o0t2es00 f530mmz5 hnhda86s oo9gr5id hzawbc8m"]'
first_name_xpath = '//input[@class="inputtext _58mg _5dba _2ph-" and @name="firstname"]'
last_name_xpath = '//input[@class="inputtext _58mg _5dba _2ph-" and @name="lastname"]'
email_xpath = '//input[@class="inputtext _58mg _5dba _2ph-" and @name="reg_email__"]'
reenter_email_xpath = '//input[@class="inputtext _58mg _5dba _2ph-" and @name="reg_email_confirmation__"]'
password_xpath = '//input[@class="inputtext _58mg _5dba _2ph-" and @name="reg_passwd__"]'
birth_day_xpath = '//select[@id="day"]'
birth_month_xpath = '//select[@id="month"]'
birth_year_xpath = '//select[@id="year"]'

if gender == 'female':
    gender_xpath = '//input[@class="_8esa" and @value="1"]'
elif gender == 'male':
    gender_xpath = '//input[@class="_8esa" and @value="2"]'
elif gender == 'custom':
    gender_xpath = '//input[@class="_8esa" and @value="-1"]'
else:
    print("Unknown gender!")
    exit(1)


options = Options()
options.headless = False
driver = webdriver.Chrome(options=options)

driver.get(URL)
time.sleep(1)
current_url = driver.current_url
assert current_url == REDIRECT_URL

try:
    create_account_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, create_account_xpath))
    )
except TimeoutException:
    print("There is no create account button on page!")
    exit(1)

create_account_button.click()

try:
    sign_up_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, sign_up_button_xpath))
    )
except TimeoutException:
    print("There is no sign up form!")
    exit(1)

driver.find_element_by_xpath(first_name_xpath).send_keys(first_name)
driver.find_element_by_xpath(last_name_xpath).send_keys(last_name)
driver.find_element_by_xpath(email_xpath).send_keys(email)
driver.find_element_by_xpath(reenter_email_xpath).send_keys(email)
driver.find_element_by_xpath(password_xpath).send_keys(password)
driver.find_element_by_xpath(gender_xpath).click()
driver.find_element_by_xpath(birth_day_xpath).send_keys(birth_day)
driver.find_element_by_xpath(birth_month_xpath).send_keys(birth_month)
driver.find_element_by_xpath(birth_year_xpath).send_keys(birth_year)

sign_up_button.click()

try:
    verification_email_form = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, verification_email_form_xpath))
    )
    print("Verification email sent. Account almost created.")
except:
    print("Verification form doesn't exist!")
    exit(1)