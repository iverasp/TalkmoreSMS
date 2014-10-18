import requests
from sys import exit
import json

BASE_URL = "https://www.talkmore.no"
LOGIN_URL = "/talkmore3/servlet/Login"
SMS_URL = "/talkmore3/servlet/SendSmsFromSelfcare"

class TalkmoreAPI:
    
    def __init__(self, phonenumber, password):
        self.phonenumber = phonenumber
        self.password = password
        self.session = requests.session()
        
    def login(self):
        login_data = {
            'username': self.phonenumber,
            'password': self.password,
            'submit': 'submit'
        }
        request = self.session.post(BASE_URL + LOGIN_URL, data=login_data)
        if (request.status_code == 200): print("Login successful")
        else:
            print("Could not login, exiting")
            sys.exit()

    def send_sms(self, contacts, message):
        if len(message) > 480:
            print("Message too long. Max is 480 characters")
            pass

        request = self.session.post(BASE_URL + SMS_URL, data= {
            'message1': message,
            'list': contacts
        })
        if (request.status_code == 200): print("Sucessfully sent SMS(s)")
        else: print("Something went wrong")

