#imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import ui
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from time import sleep
from random import randint
from datetime import datetime,timedelta
import csv
import shutil
import sys
import os
import schedule
import functions
import createRandom
import login_bot
import first


#We definne the class instabot
class instaBot:
    def __init__(self): 

        #We ask the user if he want his password, fullname, email, username, birthday and profile photo to be: auto-generated
        #or if he want to specify the properties  with  inputs
        self.mode=input("Do you want to be auto-generated or to write them yourslef?:  ")

        #if he want to write it himself 
        if self.mode=="w" or self.mode=="write":
            #it ask for the phone number or email, fullname, username, password and birth date
            self.phone_number=str(input("Phone_number or email:  "))
            self.fullname=str(input("Fullname:  "))
            self.username=str(input("Username:  "))
            self.password=str(input("Password:  "))  
            cumpleaños=input("Birth day: (D/M/Y) ")

            #here we are separating the birth into day, month and year 
            #and converting the year into the neccessary index
            cumpleaños_list=cumpleaños.split("/")
            self.day=cumpleaños_list[0]
            self.month=cumpleaños_list[1]
            year=cumpleaños_list[2]
            año_actual = "2021-04-22 00:00:00"
            ahora = datetime.strptime(año_actual, '%Y-%m-%d %H:%M:%S')
            fecha = str(ahora - timedelta(days=int(year)*365))
            fecha_lista=fecha.split("-")
            index_year=fecha_lista[0]
            self.index_year=index_year.lstrip("0")


        #if the user wants the properties to be auto-generated:
        elif self.mode=="a" or self.mode=="Auto" or self.mode=="Auto-generated":
            #we call the functions of createRandom
            tmp=createRandom.create_random()
            self.phone_number=tmp[0]
            self.fullname=tmp[1]
            self.username=tmp[2]
            self.password=tmp[3]
            

        #If the mode is not correct, we finish the program
        else:
            print("The mode must be write, w, a, auto or auto-generated ")
            sys.exit(1)


        want=input("Do you want to add a profile picture?  ")
        if want=="y" or want=="yes":

            #we delete the folder
            try:
                shutil.rmtree("C:\\Users\\lmoli\\Pictures\\Instagram profile image", ignore_errors=True)
                sleep(2)
            
            except:
                pass

            #We create a folder to store the profile image
            try:
                path = "C:\\Users\\lmoli\\Pictures"
                path = os.path.join(path, "Instagram profile image")
                os.mkdir(path)
                sleep(1)

            except:
                pass


            #we ask for the location of the profile picture
            location=input("Enter the path of your profile image:  ")

            try:
                #and we copy and rename the image to the appropiate folder
                os.replace(location, "C:\\Users\lmoli\Pictures\Instagram profile image\\descarga.jpg")

            except: 
                pass
        
        else:
            pass
        

        #we call the function to store all the data of our bot in a csv
        self.put_data_in_table()
        
        #we set the driver
        self.driver =webdriver.Chrome("chromedriver")

        #we call the create_account function
        self.create_account()
        

    #function to create the account
    def create_account(self):
        #we open instagram:
        self.driver.get("https://www.instagram.com/accounts/emailsignup/")

        self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]/button[1]").click()
        sleep(1.2)

        #we pass the phone number,  fullname,  username and  password
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div/form/div[3]/div/label/input").send_keys(self.phone_number)
        sleep(0.4)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div/form/div[4]/div/label/input").send_keys(self.fullname)
        sleep(0.4)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div/form/div[5]/div/label/input").send_keys(self.username)
        sleep(0.4)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div/form/div[6]/div/label/input").send_keys(self.password)
      
        sleep(1)
        #we click on next
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/section/main/div/div/div[1]/div/form/div[7]/div/button"))).click()
        sleep(4)


        #Birthday verification
    
        if self.mode=="a":
            #If the mode is auto-generated, we select a random birth date
            mes_path="/html/body/div[1]/section/main/div/div/div[1]/div/div[4]/div/div/span/span[1]/select/option["+str(randint(1,11))+"]"  
            day_path="/html/body/div[1]/section/main/div/div/div[1]/div/div[4]/div/div/span/span[2]/select/option["+str(randint(1,30))+"]"
            year_path="/html/body/div[1]/section/main/div/div/div[1]/div/div[4]/div/div/span/span[3]/select/option["+str(randint(16,60))+"]"
        
        elif self.mode=="w":
            #id mode is write, we pass the birthday defined above
            mes_path="/html/body/div[1]/section/main/div/div/div[1]/div/div[4]/div/div/span/span[1]/select/option["+self.month+"]"
            day_path="/html/body/div[1]/section/main/div/div/div[1]/div/div[4]/div/div/span/span[2]/select/option["+self.day+"]"
            year_path="/html/body/div[1]/section/main/div/div/div[1]/div/div[4]/div/div/span/span[3]/select/option["+self.index_year+"]"



        self.driver.find_element_by_xpath(mes_path).click()
        self.driver.find_element_by_xpath(day_path).click()
        self.driver.find_element_by_xpath(year_path).click()
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div/div[6]/button").click()


        #finally, we need to get the verification code
        #to that, we slip the email into different parts
        fMail = self.phone_number.split("@")
        mailName = self.phone_number
        domain = fMail[1]
        first=fMail[0]

        sleep(3)
        if self.mode=="a":
            #if the mode is auto.generated, we call the function to get the verification code
            instCode = self.getInstVeriCode(mailName, domain,first)

        elif self.mode=="w":
            #If mode is write, we do an input for th everification code
            instCode=input("Enter the verification code that has been sended to your phone number or email:  ")

        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[1]/input").send_keys(instCode)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[2]/button").click()

        sleep(5)

        #we ask if everything worked fine 
        #(here sometimes there could be an anti-robot verification 
        #the user must verify he has corrrectly entered to the account)
        fine=input("Everything fine?  ")

        if fine=="no" or "n":
            #if it didn't work correctly, we finish the program
            sys.exit(1)



    def put_data_in_table(self):
        #we  store all the data of our bot in a csv  called bot_properties.csv 
        #(password, username, fullname and phone number)
        with open("bot_properties.csv", "a",newline="") as file:
            writer = csv.writer(file)
            propertie=[[self.phone_number,self.fullname,self.username,self.password]]
            writer.writerows(propertie)

    
    
    def getInstVeriCode(self,mailName,domain,first):
        #function to get the verification code. 
        #It will open the website for fake mails and it will read the code from the mailbox
        #it returns the code
        #it takes as arguments the different parts of the mail
        INST_CODE = 'https://email-fake.com/' + domain + '/' + first
    
        self.driver.execute_script("window.open('');")
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get(INST_CODE)
        sleep(13)
        code = self.driver.find_element_by_xpath("//*[@id='email-table']/div[2]/div[1]/div/h1").text
        code = code.replace("is your Instagram code", "")
        self.driver.switch_to.window(self.driver.window_handles[0])
        return code



    def get_properties(self):
        #function to return the phone_number and password of our bot
        return self.phone_number, self.password

    def return_driver(self):
        #function to return the driver
        return self.driver



#We create the bot (creating the object)
bot1=instaBot()
#we create an empty list to store the people that we are following
following=[] 
#we call the function to get the properties of our bot and driver
properties=bot1.get_properties() 
driver=bot1.return_driver()


#and then we call the main function in first
print("entering to first") 
first.main(driver,following)
print("first finished")
sleep(3)


#We set the random hour to execute the script
random_hour= str(randint(1,23))+":"+str(randint(1,58))


#All the below will execute the functions code 
#(previously logging in) once a day at the random hour set above
driver=webdriver.Chrome("chromedriver")
schedule.every().day.at(random_hour).do(login_bot.login,properties=properties,driver=driver)


while True:
    try:
        schedule.run_pending()  
        sleep(3)
        functions.Function(driver)
        sleep(5)

    except:
        continue

    sleep(3)
