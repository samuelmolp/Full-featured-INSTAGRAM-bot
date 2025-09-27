#imports
from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from random import randint 
from time import sleep
import os



#the main function is called in instabot2 just after the bot is created
def main(driver,following):

    #Function to follow 10 people the first time that the app is opened
    #it will follow the 10 people that instagram reccomends
    def follow_first():
        for x in range (10):
            sleep(1)
            path="/html/body/div[1]/section/main/section/div/div/div/div/div/div["+str(x+1)+"]/div[3]/button"
            driver.find_element_by_xpath(path).click()


            #we append to the following list (list of the people that we are following) 
            #the people that we have just started following
            name=driver.find_element_by_xpath("/html/body/div[1]/section/main/section/div/div/div/div/div/div["+str(x+1)+"]/div[2]/div[1]/div/span/a")                
            following.append(name.get_attribute("text"))
            sleep(0.5)
    
        sleep(5)
        #we refresh the page
        driver.refresh()
        sleep(5)


        #we call the function to add a profile image
        photo()

    #Function to add a profile image 
    def photo():

        try:
            #we click on the button to add a profile image
            #and we execute the exe for window manipulation
            #it will take as picture the one of the folder that has been created in pictures called instagram profile picture
            driver.get("https://www.instagram.com/pepe97.gi/")
            sleep(2)
            driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/div/div/div/button").click()
            #driver.find_element_by_xpath("/html/body/div[1]/section/main/section/div/div[2]/div[1]/div[2]/div/div/div/div/ul/li[5]/div/div/div/div/button").click()
            sleep(3)
            os.system('".\\Profile.exe"')
            sleep(7)

            #finally, we refresh and quit the broser
            driver.refresh()
            sleep(5)

        except:
            print("error")
            pass

    #we call the follow_first function
    follow_first()
    driver.quit()
    sleep(4)

