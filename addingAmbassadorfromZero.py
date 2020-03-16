# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 17:15:12 2020

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
direccion = r"file direction"
os.chdir(direccion)
# setting the name of the excel
df = pd.read_excel("excel.xlsx",sheet_name="Data")
listRun = []
listToRun =["email"]
listRun = listToRun

#starting to set everything and the type of data we want to upload
# Firebase dataset
columnsDataBase = ["bio","carType",
                                  ["DQoQMSAjltFfjB1p3uqN","G3D2fZhpE9y3Nl08kmah","QcbZbhVyxc3vXUS6oHOd","KB67tdt57U2QQrSCSrcu"
                ,"t0yBSawiUs5cumRvZ8Nz","Ei95oyO6kPQntGX0qRnO","JQrfgqO4ZEW4mmgMQBEg","DpKQ3Ldh7DymDGidQXlu"
                ,"f0lL8XvpmU5z0H70z7sx","3DjxSqsAfFvDgvJJpxiM","P3ghJW1Za8G29kvc87py","Gw7ktFK4PzCT6mcsRDV4"
                ,"QHiLPQzOHNue9ixM6fXB","8UekcweFxqBmuBCfW468","lvohKqckBE5jf8Gn6tGZ","HRMeXmCi4lC5gCHs4KxY"
                ,"VDDbuYoYUIMtK9jsFDNj","vXgDdB1UuBoOGoFTxnmJ","K44Q1NrhIsB8C0CTIoWS","D5eeFRpD7fx9s8Y4v49x"
                ,"F81caNGGs6Frd62i9qt4","Se3wMYRSTOmoFTjzZfaI","vaHYsgHjVvO0zAcXrzmi","MPFfI1RKzee8r0tp8FUf"
                ,"MlLpwYavOtrk226VX2px","HiPMLgADzGjV7i4oFmmu"]
                ,"city","country","coutryOrigin",["Hour1","Hour2","Hour3","Hour4","Hour5"]
                ,"fav","firstName","gender",["name","description"]
                ,"isAmbassador","rkVerified","languages","places","tagline","tariff"]
# how they are called in the excel
columnsForm = ["bioUpgraded","carType",
               ["DQoQMSAjltFfjB1p3uqN","G3D2fZhpE9y3Nl08kmah","QcbZbhVyxc3vXUS6oHOd","KB67tdt57U2QQrSCSrcu"
                ,"t0yBSawiUs5cumRvZ8Nz","Ei95oyO6kPQntGX0qRnO","JQrfgqO4ZEW4mmgMQBEg","DpKQ3Ldh7DymDGidQXlu"
                ,"f0lL8XvpmU5z0H70z7sx","3DjxSqsAfFvDgvJJpxiM","P3ghJW1Za8G29kvc87py","Gw7ktFK4PzCT6mcsRDV4"
                ,"QHiLPQzOHNue9ixM6fXB","8UekcweFxqBmuBCfW468","lvohKqckBE5jf8Gn6tGZ","HRMeXmCi4lC5gCHs4KxY"
                ,"VDDbuYoYUIMtK9jsFDNj","vXgDdB1UuBoOGoFTxnmJ","K44Q1NrhIsB8C0CTIoWS","D5eeFRpD7fx9s8Y4v49x"
                ,"F81caNGGs6Frd62i9qt4","Se3wMYRSTOmoFTjzZfaI","vaHYsgHjVvO0zAcXrzmi","MPFfI1RKzee8r0tp8FUf"
                ,"MlLpwYavOtrk226VX2px","HiPMLgADzGjV7i4oFmmu"]
               ,"City","Country","coutryOrigin",
               ["Activity1","Activity2","Activity3"
            ,"Activity4","Activity5"],"favPlaces"
                ,"Name","Gender"
            ,["interviewBy","descriptionInterviewBy"]
            ,"isAmbassador","rkVerified","LANGUAGES","placesBeen","Field of study","tariff"]
# Type of data that they are

columnsType = ["string","string",("categoryScores","number"),"string","string"
               ,"string",["exampleDay","string"],"string","string","string"
               ,{1: 'interviewBy', 2: 'Description'}
               ,True,True,"string","string","string","number"]


# Setting chrome options

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

# This part of the code looks for the Chrome driver
browser = webdriver.Chrome(chrome_options=options,executable_path=r"chromedriver.exe")
# Getting into the link of Fire Base

#------------ Getting into user database

# Running through all the emails
for email in listRun:
    # if you want to add to staging you should check the following link
    browser.get(r'firebase url')
    # Clicking on the search place
    bontonRedknotDataBase =  WebDriverWait(browser,50).until(ec.visibility_of_element_located((By.XPATH,'/html/body/angular-home-app/fireconsole-home/main/fire-router-outlet/ng-component/authentication-users/div/div/div/div/md-single-grid/md-card/a12n-interactive-input/div/div[1]/div[2]/div/button')))
    table = WebDriverWait(browser,50).until(ec.visibility_of_element_located((By.XPATH,'/html/body/angular-home-app/fireconsole-home/main/fire-router-outlet/ng-component/authentication-users/div/div/div/div/md-single-grid/md-card/div/table')))
    #browser.execute_script("return arguments[0].scrollIntoView(true);", table)
    bontonRedknotDataBase.click()
    bontonCorreoElectronico =  WebDriverWait(browser,20).until(ec.visibility_of_element_located((By.XPATH,'/html/body/angular-home-app/fireconsole-home/main/fire-router-outlet/ng-component/authentication-users/div/div/div/div/md-single-grid/md-card/div/table/tbody[1]/tr/td/form/div[2]/div[1]/input')))
    
    bontonCorreoElectronico.send_keys(email)
    
    bontonContraseña = WebDriverWait(browser,20).until(ec.visibility_of_element_located((By.XPATH,'/html/body/angular-home-app/fireconsole-home/main/fire-router-outlet/ng-component/authentication-users/div/div/div/div/md-single-grid/md-card/div/table/tbody[1]/tr/td/form/div[2]/div[2]/input')))
    
    bontonContraseña.send_keys("password")
    
    bontonCrear = WebDriverWait(browser,10).until(ec.visibility_of_element_located((By.XPATH,'/html/body/angular-home-app/fireconsole-home/main/fire-router-outlet/ng-component/authentication-users/div/div/div/div/md-single-grid/md-card/div/table/tbody[1]/tr/td/form/div[3]/button[2]')))
    time.sleep(5)
    bontonCrear.click()
    time.sleep(5)
    botonCopiarID = WebDriverWait(browser,10).until(ec.visibility_of_element_located((By.XPATH,'/html/body/angular-home-app/fireconsole-home/main/fire-router-outlet/ng-component/authentication-users/div/div/div/div/md-single-grid/md-card/div/table/tbody[2]/tr/td[5]/div/ng-transclude')))
    valorID = botonCopiarID.get_attribute('innerHTML')
    valorID = valorID.replace('<div class="fb-table-cell-wrapper"><ng-transclude>','').replace('</ng-transclude></div>','')
    # Database
    browser.get(r'the url can go here')
    usersDataBase = WebDriverWait(browser,80).until(ec.visibility_of_element_located((By.XPATH,'/html/body/angular-home-app/fireconsole-home/main/fire-router-outlet/firestore-data/firestore-landing/f7e-data/div/div/data/div/mat-card/div[1]/div[2]/div[1]/f7e-collection-panel/f7e-data-panel/div[2]/mat-list/virtual-scroll/div[3]/mat-list-item[7]/div/div[3]')))
    usersDataBase.click()
    # Adding this person as a document
    addDocument = WebDriverWait(browser,80).until(ec.visibility_of_element_located((By.XPATH,'/html/body/angular-home-app/fireconsole-home/main/fire-router-outlet/firestore-data/firestore-landing/f7e-data/div/div/data/div/mat-card/div[1]/div[2]/div[2]/f7e-document-panel/f7e-data-panel/div[2]/f7e-add-data/div/button')))
    addDocument.click()
    IDDocument = WebDriverWait(browser,80).until(ec.visibility_of_element_located((By.XPATH,'/html/body/div[3]/div[7]/div/mat-dialog-container/f7e-data-dialog/fire-dialog/form/f7e-document-editor/div/div/input')))
    IDDocument.send_keys(valorID)
    saveDocument = WebDriverWait(browser,80).until(ec.visibility_of_element_located((By.XPATH,'/html/body/div[3]/div[7]/div/mat-dialog-container/f7e-data-dialog/fire-dialog/form/div/button[2]')))
    saveDocument.click()
    # the same thing as the adding code
    filtersDataBase = WebDriverWait(browser,20).until(ec.presence_of_element_located((By.XPATH,'/html/body/angular-home-app/fireconsole-home/main/fire-router-outlet/firestore-data/firestore-landing/f7e-data/div/div/data/div/mat-card/fire-card-action-bar/div/fire-breadcrumbs')))
    filtersDataBase.click()
    # Filtering so that we have only one row of a database
    dfEmail = df[df["Email"]==email]
    # Selecting the ID of this row
    # Getting to the search place in the database
    element = browser.find_element_by_xpath("/html/body/angular-home-app/fireconsole-home/main/fire-router-outlet/firestore-data/firestore-index/fire-feature-bar/div/div[2]/fire-feature-bar-tabs/div/nav/div[2]/div/div/a[1]")
    browser.execute_script("return arguments[0].scrollIntoView(true);", element)
    time.sleep(5)
    # Typing with the keyboard through pyautogui package
    pyautogui.press('delete')
    pyautogui.typewrite(r'/users/'+valorID)
    pyautogui.press('enter')
    # Waiting 50 seconds until the add collection appears
    addBotton = WebDriverWait(browser,50).until(ec.presence_of_element_located((By.XPATH,'/html/body/angular-home-app/fireconsole-home/main/fire-router-outlet/firestore-data/firestore-landing/f7e-data/div/div/data/div/mat-card/div[1]/div[2]/div[3]/f7e-field-panel/f7e-data-panel/div[2]/div[1]/button')))
    addBotton.click()
    for i in range(0,len(columnsDataBase)):
        # Adding the variable name
        element = browser.find_element_by_xpath("/html/body/angular-home-app/fireconsole-home/main/fire-router-outlet/firestore-data/firestore-index/fire-feature-bar/div/div[2]/fire-feature-bar-tabs/div/nav/div[2]/div/div/a[1]")
        #browser.execute_script("return arguments[0].scrollIntoView(true);", element)
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
        elif type(columnsType[i])==bool:
            Firtinfo.send_keys(columnsDataBase[i])
            time.sleep(2)
            FirtQ.send_keys("boolean")
            #browser.execute_script("return arguments[0].scrollIntoView(true);", addClick)
            addClick.click()
        

    
