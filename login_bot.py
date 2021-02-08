from selenium import webdriver
from time import sleep


#function to login with our bot called in instabot2
def login(properties,driver):
    
    #it takes as argument the email and password to login
    sleep(4)
    password= properties[1]
    email= properties[0]
    
    driver.get("https://www.instagram.com/")
    sleep(3)
    driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]/button[1]").click()

    driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input").send_keys(email)
                                
    driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input").send_keys(password)
    sleep(0.5)
    driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button").click()
    
    sleep(4)
    #driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button").click()
                                #/html/body/div[4]/div/div/div/div[3]/button[2]
    sleep(0.5)
    driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]").click()