#imports
from random import randint
import random
import string
import csv
import requests
from bs4 import BeautifulSoup



#List of names to create the fullname and username
fullname_list=[
    "Samuel","Pablo","Alejandra","Carla","Maria","Pepe","Manolo","Eustaquio","Claudia","Mario",
    "Carlos","Blanca","Rosa","Violeta","Antonio","Gustavo","Jorge","Jose","Susana","Sonia","Luis",
    "Raquel","Carmen","Eduardo","Miguel","Iñigo","Joel","Shams","Guillermo","Nacho","Paula",
    "Alejandro","Sebastian","Sergio","Alvaro","Martina","Daniela","Daniela","Martina","Marina",
    "Nora","Marcelo","Marco","Gimena","Lucia","Lola","Francisco","Hector","Juan","Zoe","Fernando",
    "Javier","Ruben","Celia","Ramon","Omar","Nerea","Marian","Wouter","Maribel","Pedro","Felipe",
    "Aitor","Bruno","Noa","Leonardo","Lorenzo","Laura","Africa","Izan","Alberto","Angel","Adrian",
    "Adriana","Aitana","Alfonso","Alfredo","Aurora","Abril","Ana","Sara","Oscar","Olga","Olivia",
    "David","Leandro","Amparo","Consuelo","Tomás","Melchor","Gapar","Baltasar"
]


#This function is called in instabot2 if the user wants the properties of the bot to be auto-generated
#this function returns a username, email, password and fullname
def create_random():

    #the name is a random choice of the list above   
    name=random.choice(fullname_list)

    #function to create a "fake" email -- it returns the mail
    def create_email():
        #it will take the mail form the page below with the libraries request and beautifulsoup
        url = 'https://email-fake.com/'
        req = requests.get(url)
        soup = BeautifulSoup(req.content, "html.parser")
        mail = soup.find_all("span", {"id": "email_ch_text"})
        return mail[0].contents


    def create_password():
        #function to create an aleatory password of 4 random letters (uppercase or lowercase)
        #and then 4 random numbers
        #this function returns the password
        
        numeros=[]
        letras=""
        tmp=""
        for x in range (4):
            numeros.append(randint(1,9))
        for x in range (4):
            tmp=tmp+str(numeros[x])
        
        for x in range(4):
            letras=letras+random.choice(string.ascii_letters)

        password=letras+tmp
        return password
    

    def create_username():
        #for creating the username, we take into account 4 things randomly ordered:
        #1. a random number between 10 and 99
        #2. an "extra" which is . or _
        #3. a random name from the list above (the same of the fullname)
        #4. 2 random letters
        #it returns  the username

        letras=""
        number=str((randint(10,99)))
        for x in range(2):
            letras=letras+random.choice(string.ascii_letters)
        extra=random.choice([".","_"])
        username=random.choice([name+number+extra+letras,name+extra+number+letras,name+letras+extra+number])
        return username
        

    #finally, we call the avobe functions to create the 4 parameters
    #fullname= name = random chocie from the list which is the same for the username
    #email=username+@mail.com
    password=create_password()
    username=create_username()
    fullname=name
    tmp=create_email()
    email=tmp[0]
    return email,fullname,username,password
