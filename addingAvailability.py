# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 16:23:40 2020

@author: david
"""
# Importing packages
import selenium
import pyautogui
from tkinter import *
import webbrowser
import datetime
from selenium import webdriver
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
import time
import pandas as pd
import logging
import numpy
import xlrd
from selenium.webdriver.support.ui import WebDriverWait
import pdb
#setting the place where the excel is
direccion = r"file direction"
os.chdir(direccion)
df = pd.read_excel("excel.xlsx",sheet_name="Data")
ultimoDia = datetime.date(2021,1, 1)
ahora = datetime.date.today()
# fecha is the date from which you want to calculate the availability
fecha = ahora
#generating the list of emails to run
listRun = []
#listToRun = df["Email"].tolist()
listToRun =["email"]

#Cleaning the given list with only those emails for the ones we have ID
for email in listToRun:
    if df[df["Email"]==email]["ID"].tolist()[0]!=0:
        listRun.append(email)
len(listRun)
#vhalderson@gmail.com

# Getting ready everything for the Chrome bot

logger = logging.getLogger("root")

logger.setLevel(logging.DEBUG)


options = webdriver.ChromeOptions()

options.add_argument("--allow-running-insecure-content")

options.add_experimental_option("prefs", {

 

    "download.default_directory": os.getcwd(),

 

    "download.prompt_for_download": False,

 

    "download.directory_upgrade": True,

 

    "safebrowsing.enabled": True

 

})

# Opening chromeDriver.exe

browser = webdriver.Chrome(chrome_options=options,executable_path=r"chromedriver.exe")

# Browsing the website
browser.get(r'direction')


#------------ Selecting the user Database

usersDataBase = WebDriverWait(browser,80).until(ec.visibility_of_element_located((By.XPATH,'/html/body/angular-home-app/fireconsole-home/main/fire-router-outlet/firestore-data/firestore-landing/f7e-data/div/div/data/div/mat-card/div[1]/div[2]/div[1]/f7e-collection-panel/f7e-data-panel/div[2]/mat-list/virtual-scroll/div[3]/mat-list-item[7]')))

usersDataBase.click()

for email in listToRun:
    # filtering for the user
    filtersDataBase = WebDriverWait(browser,1).until(ec.presence_of_element_located((By.XPATH,'/html/body/angular-home-app/fireconsole-home/main/fire-router-outlet/firestore-data/firestore-landing/f7e-data/div/div/data/div/mat-card/fire-card-action-bar/div/fire-breadcrumbs')))
    filtersDataBase.click()
    dfEmail = df[df["Email"]==email]
    ID = dfEmail["ID"].tolist()[0]
    pyautogui.typewrite(r'/users/'+ID)
    pyautogui.press('enter')
    # email
    time.sleep(2)
    addBotton = WebDriverWait(browser,50).until(ec.presence_of_element_located((By.XPATH,'/html/body/angular-home-app/fireconsole-home/main/fire-router-outlet/firestore-data/firestore-landing/f7e-data/div/div/data/div/mat-card/div[1]/div[2]/div[3]/f7e-field-panel/f7e-data-panel/div[2]/div[1]/button')))
    addBotton.click()
    columnsDates = ["Mondays","Tuesdays","Wednesdays","Thursdays","Fridays","Saturdays","Sundays"]
    dicDates = {}
    for weekDay in range(0,len(columnsDates)):
        dicDates[weekDay]=dfEmail[columnsDates[weekDay]].tolist()[0]
#-------------- adding his or her availability
    from datetime import datetime
    import datetime
    contador = 1
    contadorString= str(contador)
    Firtinfo = WebDriverWait(browser,30).until(ec.visibility_of_element_located((By.XPATH,'/html/body/angular-home-app/fireconsole-home/main/fire-router-outlet/firestore-data/firestore-landing/f7e-data/div/div/data/div/mat-card/div[2]/f7e-inline-editor/mat-card/mat-card-content/form/f7e-document-field-editor/div/div/div/div/div/div/f7e-key-value-editor/div/div/div[1]/input')))
    FirtQ = WebDriverWait(browser,30).until(ec.visibility_of_element_located((By.XPATH,'/html/body/angular-home-app/fireconsole-home/main/fire-router-outlet/firestore-data/firestore-landing/f7e-data/div/div/data/div/mat-card/div[2]/f7e-inline-editor/mat-card/mat-card-content/form/f7e-document-field-editor/div/div/div/div/div/div/f7e-key-value-editor/div/div/div[2]/mat-select')))
    Firtinfo.send_keys("availability")
    FirtQ.send_keys("map")
    addToMap = WebDriverWait(browser,30).until(ec.visibility_of_element_located((By.XPATH,'/html/body/angular-home-app/fireconsole-home/main/fire-router-outlet/firestore-data/firestore-landing/f7e-data/div/div/data/div/mat-card/div[2]/f7e-inline-editor/mat-card/mat-card-content/form/f7e-document-field-editor/div/div/div/div/div[2]/f7e-document-field-editor/div/div[2]/div[2]/button/span')))
    addClick = WebDriverWait(browser,30).until(ec.visibility_of_element_located((By.XPATH,'/html/body/angular-home-app/fireconsole-home/main/fire-router-outlet/firestore-data/firestore-landing/f7e-data/div/div/data/div/mat-card/div[2]/f7e-inline-editor/mat-card/mat-card-content/form/mat-card-actions/div/button[2]')))
    while fecha < ultimoDia:
        if dicDates[fecha.weekday()]:
            if contador!= 1:
                addToMap.click()
            Firtinfo = WebDriverWait(browser,30).until(ec.visibility_of_element_located((By.XPATH,'/html/body/angular-home-app/fireconsole-home/main/fire-router-outlet/firestore-data/firestore-landing/f7e-data/div/div/data/div/mat-card/div[2]/f7e-inline-editor/mat-card/mat-card-content/form/f7e-document-field-editor/div/div/div/div/div[2]/f7e-document-field-editor/div/div[2]/div[1]/div['+contadorString+']/div/div[2]/f7e-key-value-editor/div/div/div[1]/input')))
            FirtQ = WebDriverWait(browser,30).until(ec.visibility_of_element_located((By.XPATH,'/html/body/angular-home-app/fireconsole-home/main/fire-router-outlet/firestore-data/firestore-landing/f7e-data/div/div/data/div/mat-card/div[2]/f7e-inline-editor/mat-card/mat-card-content/form/f7e-document-field-editor/div/div/div/div/div[2]/f7e-document-field-editor/div/div[2]/div[1]/div['+contadorString+']/div/div[2]/f7e-key-value-editor/div/div/div[2]/mat-select')))
            Firtinfo.send_keys(fecha.strftime('%m-%d-%Y'))
            FirtQ.send_keys("boolean")
            contador = contador + 1
            contadorString= str(contador)
        fecha = fecha + datetime.timedelta(days = 1)
    addClick.click()
    element = browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/ng-transclude/fb-feature-bar/div/div/div[2]/div/fb-resource-selector/div/button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", element)
    time.sleep(5)
#---- hasta acá llega el proceso