#!/usr/bin/env python3
#_*_ coding:utf8 _*_

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import requests
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Firefox(executable_path=r'/home/cmorenom/Escritorio/Portafolio GitHub/Ciberseguridad/Python/geckodriver')
home_link = 'https://accounts.google.com/signin/v2/identifier?service=classroom&passive=1209600&continue=https%3A%2F%2Fclassroom.google.com%2Fu%2F0%2Fh%3Fhl%3Des&followup=https%3A%2F%2Fclassroom.google.com%2Fu%2F0%2Fh%3Fhl%3Des&hl=es&flowName=GlifWebSignIn&flowEntry=ServiceLogin'

username = 'cmorenom@uni.pe'
password = 'pass'

driver.get(home_link)
element = driver.find_element_by_id('identifierId')
element.send_keys(username)
element.send_keys(Keys.ENTER)
# submit = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button")
# submit.click()
time.sleep(5)

element = driver.find_element_by_name('password')
element.send_keys(password)
element.send_keys(Keys.ENTER)
# submit = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button")
# submit.click()
time.sleep(5)

# element.send_keys(Keys.RETURN)
# element.close()
page = 'https://classroom.google.com/'

url = requests.get(page + 'u/0/r/MzIwMDAxNzcwMTE2/sort-last-name?hl=es')
print(url)

if url.status_code == 200:
    pagina = BeautifulSoup(url.text, 'html5lib')
    print(pagina)
    tabla = pagina.findAll('table')[1]
    #print(tabla)

    nueva_tabla = pd.DataFrame(columns=['Lista'], index=range(0,30))
    #print(nueva_tabla)

    n_fila = 0
    for fila in tabla.findAll('tr'):
        n_columna = 0
        columnas = fila.findAll('td')
        #print(fila)
        for columna in columnas:
            nueva_tabla.iat[n_fila,n_columna] = columna.getText()
            n_columna +=1
        n_fila +=1
    print(nueva_tabla)

#if __name__ == '__main__':
#    try:
#        main()
#    except KeyboardInterrupt:
#        print("Fin del programa")