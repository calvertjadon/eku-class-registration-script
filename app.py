from selenium import webdriver
from os import system
from types import SimpleNamespace
from config import config


def cls():  # Clear Screen
    system('clear')


cls()

config = SimpleNamespace(**config)
print(config)

# Setup WebDriver
driver = webdriver.Chrome()

# Go to EKUDirect Login Page
driver.get('https://web4s.eku.edu/prod/twbkwbis.P_WWWLogin')
page_title = 'EKUDirect User Login'
try:
    assert page_title in driver.title
except:
    print(
        f'Incorrect page title: Expected "{page_title}" recieved "{driver.title}"')
    driver.close()

# Grab input elements from page
login_page = {
    'id_input': driver.find_element_by_xpath('//*[@id="UserID"]'),
    'pin_input': driver.find_element_by_xpath('//*[@id="PIN"]/input'),
    'submit_button': driver.find_element_by_xpath('/html/body/div[4]/form/p/input[1]')
}
login_page = SimpleNamespace(**login_page)

# Add user information to inputs and submit
login_page.id_input.send_keys(config.user_id)
login_page.pin_input.send_keys(config.pin)
login_page.submit_button.click()

# Select registration term
driver.get('https://web4s.eku.edu/prod/bwskfreg.P_AltPin')

term_select = driver.find_element_by_xpath('//*[@id="term_id"]')
term_submit = driver.find_element_by_xpath('/html/body/div[4]/form/input')
for term in term_select.find_elements_by_tag_name('option'):
    if term.text == config.registration_term:
        term.click()
        term_submit.click()
        break

# Input RAC number
rac_input = driver.find_element_by_xpath('//*[@id="apin_id"]')
rac_submit = driver.find_element_by_xpath('/html/body/div[4]/form/input')

rac_input.send_keys(config.rac_number)

input('Press enter when ready to register')

rac_submit.click()

# Agree to terms
agreement = {
    'agreement_check': driver.find_element_by_xpath('//*[@id="agreetoterms"]'),
    'name_input': driver.find_element_by_xpath('//*[@id="txtName"]'),
    'pin_input': driver.find_element_by_xpath('//*[@id="txtPIN"]')
}
agreement = SimpleNamespace(**agreement)

agreement.agreement_check.click()
agreement.name_input.send_keys(config.full_name)
agreement.pin_input.send_keys(config.pin)

# Enter CRNS
for i in range(len(config.crns)):
    driver.find_element_by_id('crn_id'+str(i+1)).send_keys(config.crns[i])

# exit()

# Submit
if not config.testing:
    driver.find_element_by_xpath('/html/body/div[4]/form/input[19]').click()

input('Press enter to exit\n')
driver.close()
