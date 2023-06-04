from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# load text files
nume = open("nume.txt", "r", encoding="UTF-8").read()
tel = open("tel.txt", "r", encoding="UTF-8").read()
email = open("email.txt", "r", encoding="UTF-8").read()
subiect = open("subiect.txt", "r", encoding="UTF-8").read()
mesaj = open("mesaj.txt", "r", encoding="UTF-8").read()
total = len(open('adrese.txt').readlines())
current = 0

# set up the webdriver
driver = webdriver.Firefox()
# navigate to the address
with open('adrese.txt') as adrese:
    for adresa in adrese:
        adresa = adresa.rstrip('\r\n')
        driver.get(adresa)
        # fill in the form fields
        try:
            driver.find_element(By.NAME, "nume").send_keys(nume)
            driver.find_element(By.NAME, "tel").send_keys(tel)
            driver.find_element(By.NAME, "email").send_keys(email)
            driver.find_element(By.NAME, "subiect").send_keys(subiect)
            driver.find_element(By.NAME, "des").send_keys(mesaj)
            # submit the form
            driver.find_element(By.NAME, "gdpr").click()
            driver.find_element(By.XPATH, "//input[@class='button wp50']").click()
            # wait for the page to load
            time.sleep(1)
        except Exception as e:
            pass
        # iterate through addresses
        current += 1
        print('finished', current, 'of', total)

# close the webdriver
driver.quit()
print('all done :)')
