# INSTAGRAM BOT
#### Video Demo:  <https://www.youtube.com/watch?v=3m95r3Oi0UU>
#### Description:

This is a full featured instagram bot. Please note that it's only for educational purposes  and not created to create botnets (it is not even capable of it, it can only handle one bot which is not programmed to follow a specific person).
The bot is mainly created using selenium in python.

This bot is capable of doing several things:

1. Firstly, it's capable of creating a new account. This process is done in the instabot.py file. There are 2 different ways of creating bots: the first  one is by specifying  all the properties of the bot by inputs (the properties are name, fullname, password, email or phone number, birthday and profile picture). The second way is by generating all those things randomly (except from the profile picture which you can choose to specify one or to not having one). This process of creating the random properties is done in the createRandom.py file. The password is generated by a random sequence of letters and numbers. The username is created by a random number and some random extra things and the fullname is the name selected as part of the username. For the email, it takes an email from a page to create a valid email so then we are able to see our  emails (to receive the verification code). After writing all those properties, in instabot.py, it puts a random birth or the specified one and it finally writes the verification code. This code is sended to an email so there are also 2 ways of getting it. The first one is that, if you've specified your own properties, it asks the code by an input. If the properties have been automatically  generated, it enters the mail, read the email with the verification code and stores the code. All the properties of the bot are stored in a csv called bot_properties.csv.


2. Once the account has been created, the fist.py file is executed. This file has 2 different parts. The first one is responsible for following people. It follows 10 people from the "for you" part. The other function  of the file is responsible  for uploading a profile picture. To do this, it executes  the Profile.exe file. This is an autoit  script for window manipulation that takes the path of the image that has been specified and uploads the profile picture. It finally quits the drive. 


3. Then, it sets a random hour to execute the following functions every day (with a module called schedule).  The first thing it does is logging in with our bot with the login_bot.py file. After that, we execute the functions file. This is capable of doing several things: the first thing it does is following people. It follows between 2 and 4 people from the "for you part". This people and the people that the bot follows in first.py are stored in a list for later purposes. After that, it sees the people that have started following the bot and the bot follows them. It later calls the function to like the pictures of the people you follow. It will open up each of the people you follow, then it will open up the first  image (if there are images). It will check if the image is from, at maximum, a day before. If the picture is from a day before, it likes half pictures and passes to the next image (then it repeats the same process: check if it is from the day before, like and pass to the next). If the picture is not from a day before, it will pass to the next person you are following (taken from the following list). The last thing it does is seeing the stories. It finally quits the drive.
