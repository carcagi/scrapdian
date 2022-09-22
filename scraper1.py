from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time, re, sys
options = Options()
options.headless = True
s=Service('/usr/local/bin/chromedriver')
d = webdriver.Chrome(service=s, options=options)
d.get('https://muisca.dian.gov.co/WebRutMuisca/DefConsultaEstadoRUT.faces')

nit = sys.argv[1]
def get_combos(nitNumber=''):
    d.find_element(By.ID, "vistaConsultaEstadoRUT:formConsultaEstadoRUT:numNit").send_keys(str(nitNumber))
    d.find_element(By.ID, "vistaConsultaEstadoRUT:formConsultaEstadoRUT:btnBuscar").click()
    
    try:
        razon = d.find_element(By.ID, "vistaConsultaEstadoRUT:formConsultaEstadoRUT:razonSocial")
        razon_social = razon.text
    except:
        razon_social = 'Not Found!'

    try:
        status = d.find_element(By.ID, "vistaConsultaEstadoRUT:formConsultaEstadoRUT:estado")
        estado = status.text
    except:
        estado = 'Not Found!'

    print('Razon social: ', razon_social)
    print('Estado: ', estado)
    
    d.quit()
    

get_combos(nit)        
