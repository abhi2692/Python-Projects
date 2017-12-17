from selenium import webdriver
from getpass import getpass

usr = input("Enter username: ")
pwd = getpass(prompt="Enter Password")

# get the path of ChromeDriverServer
driver = webdriver.Chrome()
driver.get("https://www.facebook.com")

send_usr = driver.find_element_by_id("email")
send_usr.send_keys(usr)

send_pwd = driver.find_element_by_id("pass")
send_pwd.send_keys(pwd)

login = driver.find_element_by_id("u_0_2")
login.submit()

