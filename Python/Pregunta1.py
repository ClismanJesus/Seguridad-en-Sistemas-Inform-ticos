from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(executable_path=r'/Python/geckodriver')

home_link = 'https://accounts.google.com/signin/v2/identifier?service=classroom&passive=1209600&continue=https%3A%2F%2Fclassroom.google.com%2Fu%2F0%2Fh%3Fhl%3Des&followup=https%3A%2F%2Fclassroom.google.com%2Fu%2F0%2Fh%3Fhl%3Des&hl=es&flowName=GlifWebSignIn&flowEntry=ServiceLogin'

username = 'cmorenom@uni.pe'
password = 'pass'


driver.get(home_link)

element = driver.find_element_by_id('identifierId')
element.send_keys(username)
submit = driver.find_element_by_class_name("VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc qIypjc TrZEUc lw1w4b")
submit.click()

element = driver.find_element_by_id('whsOnd zHQkBf')
element.send_keys(password)
element.send_keys(Keys.RETURN)
element.close()
