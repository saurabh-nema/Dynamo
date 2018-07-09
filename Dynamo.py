import webbrowser as wb #thia is a import lib which open browser
import os # this is import which allows us to use the os (windows files)
import speech_recognition as sr # this a import which allows us to use the speech and convert it into text
import ctypes # it is used for wwindows functions.
import win32com.client as wincl # here we are using the windows speech recognization voices.
import requests
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

speak = wincl.Dispatch('SAPI.SpVoice') # these are the voices which we are using
# path = (r'F:\\All Python Codes With Django\\My_Project\\Dynamo_Magic\\change_name.txt')
# file=open(path)
# name=file.read()
# date = time.ctime()
# test=str(date)
# speak.speak("Hello"+" "+ name+ " "+"Good Moring") # this is a voice which speaks to us
# speak.speak("today is " + date)
# print(date)
r=sr.Recognizer() # this is a recognizer which recognize our voice3
with sr.Microphone() as source: # in this we are using a microphone to record our voicecmd
  speak.speak("What can i do for you!") # this a speak invoke method w3hich ask us something
  print("Ask me Something!") # this a print statement which come on console to ask something
  audio=r.listen(source,timeout=60,phrase_time_limit=3) # tis a listen source what we going to say it will going to listen it carefully always remember it take 2 argument and it's imp to give otherwise it will rum it in infinite loop and keep on listing us until and unless we put the prog ti kill

data="" # this is a variable which is going to store a our voice and data what we have given
try:
        """
        this is a try block it will recognize it our voice and say what we have told
        """
        data= r.recognize_google(audio,language="en-US")
        print("dynamo think you said!" + "  "+data) # this will print on your console what will going to recognize by google apis
except:
        """
        this is a except block which except the error which come in try block and the code is not able to run it will pass a value
        """
        print("not able to listen you or your microphone is not good")


        """
        From here the data checking is done by our prog what the client say it will recognize it and print all the all the values accordingly which matches the values.
        """
if('who are you' in data or 'tum kaun ho' in data):
            print("just a voice to help you")
            speak.speak("just a voice to help you")

elif('whats your name' in data or 'what is your name' in data):
    print('dynamo')
    speak.speak('Hello! i am dynamo a small part of artificial intelligence that take your audio as input and work on it! and according to it give you answer. Thank you! ')


elif('nothing' in data):
    print("Ok! I'll do nothing")

elif('change my name' in data or 'what is my name' in data or 'what you call me' in data):
    path = (r'your path')
    file=open(path)
    name=file.read()
    print(name)
    print('i always call you!'+name)
    speak.speak('You set this in my memory'+name)
    speak.speak('Do you want to change')
    test=input("say yes or no:- ")
    if('yes' in test or 'y' in test or 'Yes' in test or 'Y' in test):
        change=sr.Recognizer()
        with sr.Microphone() as source:
            print('what you want me to call')
            speak.speak('what you want me to call')
            changen=change.listen(source,timeout=60,phrase_time_limit=3)
            changename=change.recognize_google(changen,language='en-IND')
            path=(r'your path') // where you want to store this data.
            file3 = open(path, 'w+')# it will open a path for us and write the change name what we have told to him.
            speak.speak('Now i will call you:- ' + changename)
            print(file3.write(changename))
            file3.close()
            print(changename)


    else:
        print('i will call you!'+ name)
        speak.speak('you are still'+ name)


elif('what can you do' in data or 'tum kya kya kar sakte ho' in data or 'tum kya kar sakte ho' in data):
        print('can tell you a joke\n'
              'can sing a song\n'
              'can give you weather updates\n'
              'can store a notes for you\n'
              'and learning more.........\n')
        speak.speak('can tell you a joke\n'
              'can sing a song\n'
              'can give you weather updates\n'
              'can store a notes for you\n'
              'and learning more.........\n')


elif('how are you' in data or 'kaise ho' in data):
              print("good!" + "  " + "what about you")
              speak.speak('good!'+" "'what about you!!')

elif('who created you' in data or 'tumhe kisne banaya hai' in data):
             print("Saurabh Nema")
             speak.speak('Saurabh Nema')

elif('who gave you this idea' in data):
             print("Stefin George" + " " +'&' +" "+ "MarkZukerberg")
             speak.speak('Stefin George'+"  "+'and mark zukarberg influence me')

elif('tell me a joke' in data):
            print("I have the perfect son Does he smoke? No, he doesnt.\n"
                  "Does he drink whiskey? No, he doesnt. \n"
                  "Does he ever come home late? No, he doesnt.\n"
                  "I guess you really do have the perfect son.\n"
                  "How old is he. He will be six months old next Wednesday.\n")
            speak.speak(" I have the perfect son Does he smoke? No, he doesnt!"
                        "Does he drink whiskey? No, he doesnt! " 
                        "Does he ever come home late? No, he doesnt!"
                        "I guess you really do have the perfect son How old is he,! "
                        "!ohh!! he will be six months old next Wednesday.")

elif('sing a song' in data):
        print(      "And all those things I didn't say\n"
                    "Wrecking balls inside my brain,\n"
                    "I will scream them loud tonight,\n"
                    "Can you hear my voice this time?,\n"
                    "This is my fight song,\n"
                    "Take back my life song,\n"
                    "Prove I'm alright song,\n"
                    "My power's turned on,\n"
                    "Starting right now I'll be strong,\n"
                    "I'll play my fight song,\n"
                    "And I don't really care if nobody else believes,\n"
                    "Cause I've still got a lot of fight left in me.\n")

        speak.speak("And all those things I didn't say!!!\n"
                    "Wrecking balls inside my brain!!!,\n"
                    "I will scream them loud tonight!!,\n"
                    "Can you hear my voice this time?!!,\n"
                    "This is my fight song!!!,\n"
                    "Take back my life song!!!,\n"
                    "Prove I'm alright song!!!,\n"
                    "My power's turned on!!!,\n"
                    "Starting right now I'll be strong!!!,\n"
                    "I'll play my fight song!!!,\n"
                    "And I don't really care if nobody else believes!!!  ,\n"
                    "Cause I've still got a lot of fight left in me.\n")

elif('play music' in data or 'play music' in data or 'kuch gana' in data or 'Kuch Gaane' in data or 'play' in data):
         speak.speak('wait a second! data is collecting')
         speak.speak('ok! now i am at your working Drive where you always found with good music!')
         print('what you want me to play')
         speak.speak('what you want me to play?!!')
         tet = sr.Recognizer()
         with sr.Microphone() as source:
             audio2 = tet.listen(source, timeout=20, phrase_time_limit=5)
             data2 = tet.recognize_google(audio2, language='en-IND')
             os.startfile(r'your music path'+data2+'."format like .mp4, mkv"')
             print('enjoy your music'+" "+data2)
             speak.speak('heres'+data2)


elif('play movie' in data or 'Movie' in data or 'movie' in data):
    speak.speak('there are two folders that i can see these are '
                'English Movie And Hindi Movie what you want me to open')
    movie=input('enter what you want me to open:- ')
    if('english movie' in movie or 'english' in movie):
        print('Say the name of the movie what you want to see')
        speak.speak('ok! now i am in english movie folder, Say the name of the movie what you want to see!')
        tet = sr.Recognizer()
        with sr.Microphone() as source:
            audio2 = tet.listen(source, timeout=60, phrase_time_limit=3)
            data2 = tet.recognize_google(audio2, language='en-IND')
            os.startfile(r'your path'+data2+'.mp4')
            print('enjoy your movie')
            speak.speak('enjoy!'+data2)
    elif('hindi movie' in movie or 'hindi' in movie or 'hindi movies' in movie):
        print('what you want me to open')
        speak.speak('ok! now i am in your hindi movie folder, Say the name of the movie what you want to see!')
        tet = sr.Recognizer()
        with sr.Microphone() as source:
            audio2 = tet.listen(source, timeout=60, phrase_time_limit=3)
            data2 = tet.recognize_google(audio2, language='en-IND')
            os.startfile(r'your path'+data2+'.mkv')
            print('enjoy your movie')
            speak.speak('enjoy!'+movie)
    else:
        print('I think that you dont have any movie like this in your drive')
        speak.speak('I think you dont have any movie like this in your folder if you still want to watch i can take you to youtube')
        wb.open('https://www.youtube.com/results?search_query='+movie)

elif('weather update'in data or 'todays forecast' in data or 'mausam' in data or 'Todays' in data or 'todays' in data):
        url = 'http://api.openweathermap.org/data/2.5/weather?appid=your-api-key='
        speak.speak('please enter a city')
        city=input('Enter the city:- ')
        print('you have enter'+" "+city)
        fullurl=url+city
        weather=requests.get(fullurl).json()
        final_weather= weather['weather'][0]['description']
        degree = weather['main']['temp']
        final_degree = int(degree-273.15) // conversion of f to c
        cal_deg = str(final_degree)
        speak.speak('The weather in '+"  "+ city+" "+ 'is')
        speak.speak( cal_deg + 'degree celcius and its')
        print(final_degree)
        print(final_weather)
        if (final_degree > 30):
            speak.speak("i recommand you should wear a light weight cloths because its" + cal_deg)
        elif (final_degree < 15):
            speak.speak("Should wear warm cloths because its" + cal_deg)
        else:
            speak.speak("today weather is good to go because its" + cal_deg)
            print("today weather is good to go because its" + "  " +cal_deg)

elif('add notes' in data or 'notes' in data or 'to do list' in data):
        print('what you want me to write down for you!')
        speak.speak('what you want me to write down.')
        speak.speak('first tell me that,"do you want it to write it down or you want me to write it down?! i will recomment you to write it down!"')
        print('first tell me that,"do you want it to write it down or you want me to write it down?! i will recomment you to write it down!"')
        speak.speak('Please give me the keyboard input!')
        data=input('type here yes or no:- ')
        if('yes' in data):
            path = (r'"your path"+"file name"')  # here i have set a path in this path the value come and store.
            speak.speak('now say what should i store')
            tet=sr.Recognizer()
            with sr.Microphone() as source:
                audio2=tet.listen(source,timeout=60,phrase_time_limit=5)
                data2=tet.recognize_google(audio2,language='en-IND')
                file = open(path, 'w+') # it will go on that location and write a file what we going to say
                print(file.write(data2)) # writr the things that we going to say
                file.close() # it's imp to close the connection after completing the task
                print(data2)
                speak.speak('ok! I have wrote this '+" "+ data2)
        else:
            path = (r'your path + file name')  # here i have set a path in this path the value come and store.
            file = open(path, 'w+')  # it will go on that location and write a file what we going to say
            data2=input('type here what you want to store:- '+"")
            print(file.write(data2))  # writr the things that we going to say
            file.close()  # it's imp to close the connection after completing the task
            print(data2)

elif('show my to do list' in data or 'show notes' in data or 'show note' in data ):
        print('collecting data! please wait')
        speak.speak('collecting data! please wait')
        path=(r'your path + file name')
        file1=open(path,'r') # it will open a path for us
        speak.speak('this are your todo list')
        print(file1.read()) # it will read the text which is there in a file and print it on console
        #os.startfile(r'F:\\All Python Codes With Django\\My_Project\\Dynamo_Magic\\notes.txt') # it will open a notepad for us and the location is given where we have stored as txt file.
        file1.close()

elif('shutdown pc' in data or 'Shutdown' in data or 'shutdown' in data or 'system list' in data):
    print('what type of input would be there a voice or keyboard')
    speak.speak('what type of input would be there a voice or keyboard')
    speak.speak('say now?')
    tet = sr.Recognizer()
    with sr.Microphone() as source:
        audio2 = tet.listen(source, timeout=60, phrase_time_limit=5)
        data2 = tet.recognize_google(audio2, language='en-IND')
        condition = data2
        if('keyboard' in data2 or 'Keyboard' in data2):
            speak.speak('choose accordingly')
            print('shutdown \n'
                  'lockscreen \n'
                  'restart')
            speak.speak('shutdown \n'
                        'lockscreen \n'
                        'restart \n')
            choose=input('Enter your choise here:-'+"")
            if('shutdown' in choose):
                print('system will shut down after 60 !sec')
                speak.speak('system will shutdown after !60 sec')
                os.system('shutdown -s')
            elif('lockscreen' in choose):
                ctypes.windll.user32.LockWorkStation()
            elif('restart' in choose):
              os.system('shutdown -r')
            else:
                print('enter choise is incorrect')
                speak.speak('enter choise is incorrect')
        elif('voice' in data or 'Voice' in data2 or 'dell' or 'audio' in data2):
            speak.speak('choose accordingly')
            print('shutdown \n'
                  'lockscreen \n'
                  'restart')
            speak.speak('shutdown \n'
                        'lockscreen \n'
                        'restart \n')
            speak.speak('say now')
            tet = sr.Recognizer()
            with sr.Microphone() as source:
                audio2 = tet.listen(source, timeout=60, phrase_time_limit=5)
                data2 = tet.recognize_google(audio2, language='en-IND')
                condition = data2
                if ('shutdown' in data2):
                    print('system will shut down after 60 !sec')
                    speak.speak('system will shutdown within a minute please close all programe that are running by yourself bugger!')
                    os.system('shutdown -s')
                elif ('lockscreen' in data2):
                    ctypes.windll.user32.LockWorkStation()
                elif ('restart' in data2):
                    os.system('shutdown -r')
                else:
                    print('enter choise is incorrect')
                    speak.speak('enter choise is incorrect')
        else:
            print('I didnt get you! sorry?')
            speak.speak('I didnt get you! sorry?')


elif('Train' in data or 'train' in data or 'train live status' in data):
    print("Please tell me the train name")
    speak.speak('Please,tell me the train number')
    train_number=input('Please enter train number:-'+"")
    speak.speak("please enter a date")
    date=input("Please enter a date in this format please(dd-mm-yyyy):- "+"")
    url="https://api.railwayapi.com/v2/live/train/"+train_number+"/date/"+date+"/apikey/your api key/"
    status=requests.get(url).json()
    train_name=requests.get(url).json()
    desc=requests.get(url).json()
    des=desc['position']
    final_status = status['current_station']['name'] // retreving data from APIs
    trainname=train_name ['train']['name']
    speak.speak("ok! you are enquiring of "+trainname)
    print(trainname)
    speak.speak(des)
    print(des)
    speak.speak("Current Station is"+final_status)
    print(final_status)


elif('send mails' in data or 'mail' in data or 'send' in data):

    speak.speak("You have two mail accounts from which did you want to send=>(outlook/gmail): ")
    mail_input = input("enter your account name:")
    if('outlook' in mail_input):
        speak.speak("Please tell me the input type")
        taking_input = input("enter the way that you want to send a mail by voice/type: ")
        if('type' in taking_input):
            email_user = 'your email id'
            email_password = 'your password'
            speak.speak("to whome you want to send")
            email_send = input("To whome you want to send: ")

            speak.speak("Please enter your mail subject: ")
            subject = input("please enter your subject here: ")

            msg = MIMEMultipart()
            msg['From'] = email_user
            msg['To'] = email_send
            msg['Subject'] = subject

            speak.speak("Enter your mail Content")
            body = input("enter the body of your mail: ")
            msg.attach(MIMEText(body, 'plain'))

            attachments = input("Did you want to add attachments: Y/N: ")
            if('Y' in attachments or 'y' in attachments or 'yes' in attachments or 'YES' in attachments):

                filename= input("enter a path where your attachements are present: ")
                attachment  =open(filename,'rb')

                part = MIMEBase('application','octet-stream')
                part.set_payload((attachment).read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition',"attachment; filename= "+filename)
                msg.attach(part)
                text = msg.as_string()

            server = smtplib.SMTP('smtp-mail.outlook.com', 587)
            server.starttls()
            server.login(email_user, email_password)
            server.sendmail(email_user, email_send, body)
            speak.speak("WOW!! just now sent your mail")
            print("sucess")

    else:
        email_user = 'your email id'
        email_password = 'your password'
        speak.speak("to whome you want to send")
        send_user = input("please enter to whome you want to sent this mail: ")
        print(send_user)

        speak.speak("Please say me the subject of this mail: ")
        tet = sr.Recognizer()
        with sr.Microphone() as source:
            audio2 = tet.listen(source, timeout=60, phrase_time_limit=5)
            data2 = tet.recognize_google(audio2, language='en-IND')
            condition = data2
            subject = condition
            print(subject)

        msg = MIMEMultipart()
        msg['From'] = email_user
        msg['To'] = send_user
        msg['Subject'] = subject


        speak.speak("Please say me the content of your mail: ")
        tet = sr.Recognizer()
        with sr.Microphone() as source:
            audio2 = tet.listen(source, timeout=60, phrase_time_limit=5)
            data2 = tet.recognize_google(audio2, language='en-IND')
            condition = data2
            content = condition
            print(content)

        msg.attach(MIMEText(content, 'plain'))

        speak.speak("Do you want to attached attachements with mail: ")
        con = input("Did you want to attached something with this mail: Y/N: ")

        if('Y' in con or 'y' in con or 'yes' in con or "YES" in con):


            filename=input("please enter a link towards your attachments: ")
            attachment  =open(filename,'rb')

            part = MIMEBase('application','octet-stream')
            part.set_payload((attachment).read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition',"attachment; filename= "+filename)

            msg.attach(part)
            text = msg.as_string()
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(email_user, email_password)

            server.sendmail(email_user, send_user, content)
            speak.speak("Sent your mail")
            print("sucess")

        else:

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(email_user, email_password)
            server.sendmail(email_user,send_user,content)
            assert "mail address not found."
            speak.speak("Sent your mail")
            print("sucess")








else:
        """
        if nothing will going to work it will run and show this content
        and this will also work if you will not say anything till 6 sec this will count as timeout and prog take you here.
        """
        print('Ok let me check a web for you!'+data)
        speak.speak('let me check a web for you for'+ data)
        wb.open_new_tab('https://www.google.com/#q='+ data) # it will open a web and give you details about it.
