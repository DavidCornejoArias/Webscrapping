# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 16:36:07 2020

@author: david
"""
# importing the packages
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
direccion = r"direction"
os.chdir(direccion)
# setting the name of the excel
df = pd.read_excel("excel.xlsx",sheet_name="Data")

#starting to set everything and the type of data we want to upload
columnsDataBase = ["languages"]

# I should add an input varible for the ones that are not so clear carType, city
columnsForm = ["languages"]
#columnsForm = ["favPlaces","Field of study"]

columnsType = ["string"]
#columnsType = ["string","string"]
listRun = []
# The one below is to change a whole list of emails
#listToRun = df["Email"].tolist()
# the following one is to change an specific email, you can add more with a coma within ""
listToRun =["email"]

# Running only through the list that actually has an ID in the database
for email in listToRun:
    if df[df["Email"]==email]["ID"].tolist()[0]!=0:
        listRun.append(email)
len(listRun)

logger = logging.getLogger("root")

logger.setLevel(logging.DEBUG)

# Setting everything for the browser

options = webdriver.ChromeOptions()

options.add_argument("--allow-running-insecure-content")

options.add_experimental_option("prefs", {

 

    "download.default_directory": os.getcwd(),

 

    "download.prompt_for_download": False,

 

    "download.directory_upgrade": True,

 

    "safebrowsing.enabled": True

 

})

# Opening Chrome bot

browser = webdriver.Chrome(chrome_options=options,executable_path=r"chromedriver.exe")
# Getting into the link of Fire Base
browser.get(r'direction')

#------------ Getting into user database

usersDataBase = WebDriverWait(browser,80).until(ec.visibility_of_element_located((By.XPATH,'/html/body/angular-home-app/fireconsole-home/main/fire-router-outlet/firestore-data/firestore-landing/f7e-data/div/div/data/div/mat-card/div[1]/div[2]/div[1]/f7e-collection-panel/f7e-data-panel/div[2]/mat-list/virtual-scroll/div[3]/mat-list-item[7]/div/div[3]')))

usersDataBase.click()

# Running through all the emails
for email in listRun:
    # Clicking on the search place
    element = browser.find_element_by_xpath("/html/body/angular-home-app/fireconsole-home/main/fire-router-outlet/firestore-data/firestore-index/fire-feature-bar/div/div[2]/fire-feature-bar-tabs/div/nav/div[2]/div/div/a[1]")
    browser.execute_script("return arguments[0].scrollIntoView(true);", element)

    # Filtering so that we have only one row of a database
    dfEmail = df[df["Email"]==email]
    # Selecting the ID of this row
    ID = dfEmail["ID"].tolist()[0]
    # Getting to the search place in the database
    time.sleep(5)
    filtersDataBase = WebDriverWait(browser,1).until(ec.presence_of_element_located((By.XPATH,'/html/body/angular-home-app/fireconsole-home/main/fire-router-outlet/firestore-data/firestore-landing/f7e-data/div/div/data/div/mat-card/fire-card-action-bar/div/fire-breadcrumbs')))
    filtersDataBase.click()
    # Typing with the keyboard through pyautogui package
    pyautogui.typewrite(r'/users/'+ID)
    pyautogui.press('enter')
    # Waiting 50 seconds until the add collection appears
    addBotton = WebDriverWait(browser,50).until(ec.presence_of_element_located((By.XPATH,'/html/body/angular-home-app/fireconsole-home/main/fire-router-outlet/firestore-data/firestore-landing/f7e-data/div/div/data/div/mat-card/div[1]/div[2]/div[3]/f7e-field-panel/f7e-data-panel/div[2]/div[1]/button')))
    addBotton.click()
    for i in range(0,len(columnsDataBase)):
        # Adding the variable name
        addBotton = WebDriverWait(browser,50).until(ec.presence_of_element_located((By.XPATH,'/html/body/angular-home-app/fireconsole-home/main/fire-router-outlet/firestore-data/firestore-landing/f7e-data/div/div/data/div/mat-card/div[1]/div[2]/div[3]/f7e-field-panel/f7e-data-panel/div[2]/div[1]/button')))
        if i!= 0:
            addBotton.click()
        # Firt info equals the variable name
        Firtinfo = WebDriverWait(browser,30).until(ec.visibility_of_element_located((By.XPATH,'/html/body/angular-home-app/fireconsole-home/main/fire-router-outlet/firestore-data/firestore-landing/f7e-data/div/div/data/div/mat-card/div[2]/f7e-inline-editor/mat-card/mat-card-content/form/f7e-document-field-editor/div/div/div/div/div/div/f7e-key-value-editor/div/div/div[1]/input')))
        # FirtQ equals the type of data
        FirtQ = WebDriverWait(browser,30).until(ec.visibility_of_element_located((By.XPATH,'/html/body/angular-home-app/fireconsole-home/main/fire-router-outlet/firestore-data/firestore-landing/f7e-data/div/div/data/div/mat-card/div[2]/f7e-inline-editor/mat-card/mat-card-content/form/f7e-document-field-editor/div/div/div/div/div/div/f7e-key-value-editor/div/div/div[2]/mat-select')))
        # FirtQ2 equals the value of the variable
        FirtQ2 = WebDriverWait(browser,30).until(ec.visibility_of_element_located((By.XPATH,'/html/body/angular-home-app/fireconsole-home/main/fire-router-outlet/firestore-data/firestore-landing/f7e-data/div/div/data/div/mat-card/div[2]/f7e-inline-editor/mat-card/mat-card-content/form/f7e-document-field-editor/div/div/div/div/div/div/f7e-key-value-editor/div/div/div[3]/input')))
        # AddClick is the add this variable
        addClick = WebDriverWait(browser,30).until(ec.visibility_of_element_located((By.XPATH,'/html/body/angular-home-app/fireconsole-home/main/fire-router-outlet/firestore-data/firestore-landing/f7e-data/div/div/data/div/mat-card/div[2]/f7e-inline-editor/mat-card/mat-card-content/form/mat-card-actions/div/button[2]')))
        # Depending of the columnsType variable the actions of the code will be different
        if columnsType[i]=="string" or columnsType[i]=="number":
            Firtinfo.click()
            Firtinfo.send_keys(columnsDataBase[i])
            FirtQ.send_keys(columnsType[i])
            FirtQ2.click()
            FirtQ2.send_keys(dfEmail[columnsForm[i]].tolist()[0])
            addClick.click()
        elif type(columnsType[i])==list:
            Firtinfo.send_keys(columnsType[i][0])
            FirtQ.send_keys("map")
            addToMap = WebDriverWait(browser,30).until(ec.visibility_of_element_located((By.XPATH,'/html/body/angular-home-app/fireconsole-home/main/fire-router-outlet/firestore-data/firestore-landing/f7e-data/div/div/data/div/mat-card/div[2]/f7e-inline-editor/mat-card/mat-card-content/form/f7e-document-field-editor/div/div/div/div/div[2]/f7e-document-field-editor/div/div[2]/div[2]/button/span')))
            for nombreMap in range(0,len(columnsForm[i])):
                if nombreMap!= 0:
                    addToMap.click()
                div = str(nombreMap + 1)
                Firtinfo = WebDriverWait(browser,30).until(ec.visibility_of_element_located((By.XPATH,'/html/body/angular-home-app/fireconsole-home/main/fire-router-outlet/firestore-data/firestore-landing/f7e-data/div/div/data/div/mat-card/div[2]/f7e-inline-editor/mat-card/mat-card-content/form/f7e-document-field-editor/div/div/div/div/div[2]/f7e-document-field-editor/div/div[2]/div[1]/div['+div+']/div/div[2]/f7e-key-value-editor/div/div/div[1]/input')))
                FirtQ = WebDriverWait(browser,30).until(ec.visibility_of_element_located((By.XPATH,'/html/body/angular-home-app/fireconsole-home/main/fire-router-outlet/firestore-data/firestore-landing/f7e-data/div/div/data/div/mat-card/div[2]/f7e-inline-editor/mat-card/mat-card-content/form/f7e-document-field-editor/div/div/div/div/div[2]/f7e-document-field-editor/div/div[2]/div[1]/div['+div+']/div/div[2]/f7e-key-value-editor/div/div/div[2]/mat-select')))
                FirtQ2 = WebDriverWait(browser,30).until(ec.visibility_of_element_located((By.XPATH,'/html/body/angular-home-app/fireconsole-home/main/fire-router-outlet/firestore-data/firestore-landing/f7e-data/div/div/data/div/mat-card/div[2]/f7e-inline-editor/mat-card/mat-card-content/form/f7e-document-field-editor/div/div/div/div/div[2]/f7e-document-field-editor/div/div[2]/div[1]/div['+div+']/div/div[2]/f7e-key-value-editor/div/div/div[3]/input')))
                if type(columnsDataBase[i])==list:
                    Firtinfo.send_keys(dfEmail[columnsDataBase[i][nombreMap]].tolist()[0].strftime("%H:%M"))
                else:
                    Firtinfo.send_keys(columnsDataBase[i][nombreMap])
                FirtQ.send_keys(columnsType[i][1])
                send = str(dfEmail[columnsForm[i][nombreMap]].tolist()[0])
                FirtQ2.click()
                FirtQ2.send_keys(send)
            browser.execute_script("return arguments[0].scrollIntoView(true);", addClick)
            addClick.click()
        elif type(columnsType[i])==tuple:
            Firtinfo.send_keys(columnsType[i][0])
            FirtQ.send_keys("map")
            addToMap = WebDriverWait(browser,30).until(ec.visibility_of_element_located((By.XPATH,'/html/body/angular-home-app/fireconsole-home/main/fire-router-outlet/firestore-data/firestore-landing/f7e-data/div/div/data/div/mat-card/div[2]/f7e-inline-editor/mat-card/mat-card-content/form/f7e-document-field-editor/div/div/div/div/div[2]/f7e-document-field-editor/div/div[2]/div[2]/button/span')))
            for nombreMap in range(0,len(columnsForm[i])):
                if nombreMap!= 0:
                    addToMap.click()
                div = str(nombreMap + 1)
                Firtinfo = WebDriverWait(browser,30).until(ec.visibility_of_element_located((By.XPATH,'/html/body/angular-home-app/fireconsole-home/main/fire-router-outlet/firestore-data/firestore-landing/f7e-data/div/div/data/div/mat-card/div[2]/f7e-inline-editor/mat-card/mat-card-content/form/f7e-document-field-editor/div/div/div/div/div[2]/f7e-document-field-editor/div/div[2]/div[1]/div['+div+']/div/div[2]/f7e-key-value-editor/div/div/div[1]/input')))
                FirtQ = WebDriverWait(browser,30).until(ec.visibility_of_element_located((By.XPATH,'/html/body/angular-home-app/fireconsole-home/main/fire-router-outlet/firestore-data/firestore-landing/f7e-data/div/div/data/div/mat-card/div[2]/f7e-inline-editor/mat-card/mat-card-content/form/f7e-document-field-editor/div/div/div/div/div[2]/f7e-document-field-editor/div/div[2]/div[1]/div['+div+']/div/div[2]/f7e-key-value-editor/div/div/div[2]/mat-select')))
                FirtQ2 = WebDriverWait(browser,30).until(ec.visibility_of_element_located((By.XPATH,'/html/body/angular-home-app/fireconsole-home/main/fire-router-outlet/firestore-data/firestore-landing/f7e-data/div/div/data/div/mat-card/div[2]/f7e-inline-editor/mat-card/mat-card-content/form/f7e-document-field-editor/div/div/div/div/div[2]/f7e-document-field-editor/div/div[2]/div[1]/div['+div+']/div/div[2]/f7e-key-value-editor/div/div/div[3]/input')))
                Firtinfo.send_keys(columnsDataBase[i][nombreMap])
                FirtQ.send_keys(columnsType[i][1])
                if pd.isna((dfEmail[columnsForm[i][nombreMap]].tolist()[0])):
                    send = ""
                else:
                    send = str(dfEmail[columnsForm[i][nombreMap]].tolist()[0])
                FirtQ2.click()
                FirtQ2.send_keys(send)
            browser.execute_script("return arguments[0].scrollIntoView(true);", addClick)
            addClick.click()
        elif type(columnsType[i])==dict:
            Firtinfo.send_keys("interviewBy")
            FirtQ.send_keys("array")
            addToMap = WebDriverWait(browser,30).until(ec.visibility_of_element_located((By.XPATH,'/html/body/angular-home-app/fireconsole-home/main/fire-router-outlet/firestore-data/firestore-landing/f7e-data/div/div/data/div/mat-card/div[2]/f7e-inline-editor/mat-card/mat-card-content/form/f7e-document-field-editor/div/div/div/div/div[2]/f7e-document-field-editor/div/div[2]/div[2]/button')))
            for nombreMap in range(0,1):
                if nombreMap!= 0:
                    addToMap.click()
                div = str(nombreMap + 1)
                Firtinfo = WebDriverWait(browser,30).until(ec.visibility_of_element_located((By.XPATH,'/html/body/angular-home-app/fireconsole-home/main/fire-router-outlet/firestore-data/firestore-landing/f7e-data/div/div/data/div/mat-card/div[2]/f7e-inline-editor/mat-card/mat-card-content/form/f7e-document-field-editor/div/div/div/div/div[2]/f7e-document-field-editor/div/div[2]/div[1]/div/div/div[2]/f7e-key-value-editor/div/div/div[2]/mat-select')))
                Firtinfo.send_keys("map")
                if nombreMap == 0:
                    addToMap2 = WebDriverWait(browser,30).until(ec.visibility_of_element_located((By.XPATH,'/html/body/angular-home-app/fireconsole-home/main/fire-router-outlet/firestore-data/firestore-landing/f7e-data/div/div/data/div/mat-card/div[2]/f7e-inline-editor/mat-card/mat-card-content/form/f7e-document-field-editor/div/div/div/div/div[2]/f7e-document-field-editor/div/div[2]/div[1]/div/div[2]/f7e-document-field-editor/div/div[2]/div[2]/button')))
                else:
                    addToMap2 = WebDriverWait(browser,30).until(ec.visibility_of_element_located((By.XPATH,'/html/body/angular-home-app/fireconsole-home/main/fire-router-outlet/firestore-data/firestore-landing/f7e-data/div/div/data/div/mat-card/div[2]/f7e-inline-editor/mat-card/mat-card-content/form/f7e-document-field-editor/div/div/div/div/div[2]/f7e-document-field-editor/div/div[2]/div[1]/div/div[2]/f7e-document-field-editor/div/div[2]/div[2]/button')))
                #creating the first group
                FirtQ = WebDriverWait(browser,30).until(ec.visibility_of_element_located((By.XPATH,'/html/body/angular-home-app/fireconsole-home/main/fire-router-outlet/firestore-data/firestore-landing/f7e-data/div/div/data/div/mat-card/div[2]/f7e-inline-editor/mat-card/mat-card-content/form/f7e-document-field-editor/div/div/div/div/div[2]/f7e-document-field-editor/div/div[2]/div[1]/div/div[2]/f7e-document-field-editor/div/div[2]/div[1]/div/div/div[2]/f7e-key-value-editor/div/div/div[1]/input')))
                FirtQ2 = WebDriverWait(browser,30).until(ec.visibility_of_element_located((By.XPATH,'/html/body/angular-home-app/fireconsole-home/main/fire-router-outlet/firestore-data/firestore-landing/f7e-data/div/div/data/div/mat-card/div[2]/f7e-inline-editor/mat-card/mat-card-content/form/f7e-document-field-editor/div/div/div/div/div[2]/f7e-document-field-editor/div/div[2]/div[1]/div/div[2]/f7e-document-field-editor/div/div[2]/div[1]/div/div/div[2]/f7e-key-value-editor/div/div/div[3]/input')))
                FirtQ.send_keys(columnsDataBase[i][0])
                FirtQ2.send_keys(str(dfEmail[columnsForm[i][0]].tolist()[0]))
                #creating the second group[nombreMap]
                #time.sleep(2)
                addToMap2.click()
                FirtQ = WebDriverWait(browser,30).until(ec.visibility_of_element_located((By.XPATH,'/html/body/angular-home-app/fireconsole-home/main/fire-router-outlet/firestore-data/firestore-landing/f7e-data/div/div/data/div/mat-card/div[2]/f7e-inline-editor/mat-card/mat-card-content/form/f7e-document-field-editor/div/div/div/div/div[2]/f7e-document-field-editor/div/div[2]/div[1]/div/div[2]/f7e-document-field-editor/div/div[2]/div[1]/div[2]/div/div[2]/f7e-key-value-editor/div/div/div[1]/input')))
                FirtQ2 = WebDriverWait(browser,30).until(ec.visibility_of_element_located((By.XPATH,'/html/body/angular-home-app/fireconsole-home/main/fire-router-outlet/firestore-data/firestore-landing/f7e-data/div/div/data/div/mat-card/div[2]/f7e-inline-editor/mat-card/mat-card-content/form/f7e-document-field-editor/div/div/div/div/div[2]/f7e-document-field-editor/div/div[2]/div[1]/div/div[2]/f7e-document-field-editor/div/div[2]/div[1]/div[2]/div/div[2]/f7e-key-value-editor/div/div/div[3]/input')))
                FirtQ.send_keys(columnsDataBase[i][1])
                if str(dfEmail[columnsForm[i][1]].tolist()[0])== "nan":
                    text = ""
                else:
                    text = str(dfEmail[columnsForm[i][1]].tolist()[0])
                FirtQ2.send_keys(text)
            addClick.click()
        elif columnsType[i]==bool:
            Firtinfo.send_keys(columnsDataBase[i])
            FirtQ.send_keys("boolean")
            browser.execute_script("return arguments[0].scrollIntoView(true);", addClick)
            addClick.click()
        

    