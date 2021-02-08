#imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import ui
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from random import randint 
from time import sleep
import subprocess
import os
import schedule
import shutil




#this function is called in instabot2 once a day at a random hour after being logged in with the login function
def Function(following,driver):       
    #it takes as arguments the driver and the list of the people you're following 

    def follow():
        #function to follow people, between 2 and 4
        #it will follow the people that instagram reccomends you
        sleep(2)
        for x in range(randint(2,4)):
            
            path="/html/body/div[1]/section/main/section/div[3]/div[2]/div[2]/div/div/div/div["+str(x+1)+"]/div[3]/button"
            driver.find_element_by_xpath(path).click()

            #it appends the new people that you're following to the following list
            follow=driver.find_elements_by_xpath("/html/body/div[1]/section/main/section/div[3]/div[2]/div[2]/div/div/div/div["+str(x+1)+"]/div[2]/div[1]/div/span/a")[0]
            following.append(follow.get_attribute("text"))


        #we refresh
        sleep(1)
        driver.refresh()
        sleep(5)
        
        #and we cal the check_sol fucntion
        check_sol()


    def check_sol(): 
        #function to follow the people that follow you
        x=0
        driver.get("https://www.instagram.com/accounts/activity/")
        sleep(3)
        while True:
            #we try to follow person by person and when we see that we already follow that person, we finish
            try:
                driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/div["+str(x+1)+"]/div[3]/button").click()               
                x=x+1
                sleep(2)


            except:
                #if we already follow that person, we exit
                sleep(2)
                break
        


        #we refresh
        driver.refresh()
        sleep(3)

        #and we call the like function
        like()
                        
                


    def like():
        
        """
        function to like the images of the people you follow
        it will open up each of the people you follow, then it will open up the first image.
        It will check if the first image is from at maximum, a day before
        if it's from a day before, it will: like half pictures
        and passs to the next image and check if it's from at maximum, a day before

        if the first image is not from the day before, it will pass the the next person (taken from the following list)
        """

        sleep(2)
    
        for x in range (len(following)):
            #open each of the people you follow
            url= "https://www.instagram.com/"+following[x]+"/"
            driver.get(url)
            sleep(5)
            
            #scroll down
            driver.execute_script("window.scrollTo(0,280)")

            
            #if there are posts, we continue
            driver.find_element_by_class_name("v1Nh3").click()

            sleep(2)
                #we scroll down a little bit
            driver.execute_script("window.scrollTo(0,40)")
            x=0

            try:

                while True:
                    x=x+1

                    sleep(1)
                    fecha = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[3]/div[2]/a/time")                        
                    date = fecha.text
                    sleep(1)

                    if "HORAS" in date or "HACE 1 DÍA" in date:
                        #if it's from at maximun a day before
                
                        if randint(0,1)==1:
                            #we like half pictuers
                            driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]/button").click()
                            print("Like")
                    
                            sleep(1)

                        sleep(1)

                        #we pass to the next post
                        if x==1:
                            driver.find_element_by_xpath("/html/body/div[4]/div[1]/div/div/a").click()

                        else:
                            driver.find_element_by_xpath("/html/body/div[4]/div[1]/div/div/a[2]").click()

                        sleep(2)
                

                    else:
                        #if it's not from a day before, we pass to the next person
                        break

                    sleep(3)

            except:
                #if the account doesn't have any posts, it will pass to the next person
                pass
              

        #we call the stories function
        stories()



    def stories():
        x=0
        try:
            x+=1
            #TOCKECK 
            #Function to see the stories
            driver.get("https://www.instagram.com/")
            sleep(2)

            #we enter to the first story
            driver.find_element_by_xpath("/html/body/div[1]/section/main/section/div/div[1]/div/div/div/div/ul/li[3]/div/button").click()
            sleep(2)

            while True:
                sleep(0.5)
                try:
                    #we pass to the next storie

                    if x==0:
                        try:
                            driver.find_element_by_xpath("/html/body/div[1]/section/div[1]/div/div[5]/section/div/button").click()
                    
                        except:
                            driver.find_element_by_xpath("/html/body/div[1]/section/div[1]/div/div[5]/section/div/button[2]").click()
                        

                    else:
                        driver.find_element_by_xpath("/html/body/div[1]/section/div[1]/div/div[5]/section/div/button[2]").click()
                        

                except:
                    #if there are not more stories to watch, we finish the function
                    break

        except:
            #if there are not any stories, we pass
            pass


    #we call the follow function
    #follow()
    stories()
    sleep(3)

    #we quit the driver
    driver.quit()
    sleep(3)
