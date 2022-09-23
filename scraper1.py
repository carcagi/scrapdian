from pyvirtualdisplay import Display
from selenium import webdriver
#from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import time, re, sys, os
#import psycopg

display = Display(visible=0, size=(1920, 1080))
display.start()

d = webdriver.Chrome()
d.get('https://muisca.dian.gov.co/WebRutMuisca/DefConsultaEstadoRUT.faces')
nit = sys.argv[1]
company_id = sys.argv[2]

def get_nitinfo(nitNumber='', company_id=''):

    nit_field = d.find_element(By.ID, "vistaConsultaEstadoRUT:formConsultaEstadoRUT:numNit")
    nit_field.send_keys(str(nitNumber))

    submit_btn =  d.find_element(By.ID, "vistaConsultaEstadoRUT:formConsultaEstadoRUT:btnBuscar")
    submit_btn.click()

    name = d.find_element(By.ID, "vistaConsultaEstadoRUT:formConsultaEstadoRUT:razonSocial")
    
    try:
        name = d.find_element(By.ID, "vistaConsultaEstadoRUT:formConsultaEstadoRUT:razonSocial")
        company_name = name.text
    except:
        company_name = ''

    try:
        status = d.find_element(By.ID, "vistaConsultaEstadoRUT:formConsultaEstadoRUT:estado")
        company_status = status.text
    except:
        company_status = ''

    d.quit()

    print('Razon social: ', company_name)
    print('Estado: ', company_status)    

def save_nitinfo(company_name, company_status, company_id):
    with psycopg.connect("dbname=test user=postgres") as conn:
        cur.execute("""
            INSERT INTO companie_dian_validated (company_id, company_name, company_status)
            VALUES (%s, %s, %s);
            """,
            (company_id, company_name, company_status))

get_nitinfo(nit)    
display.stop()    
