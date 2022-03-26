import os
import smtplib
import imghdr
from email.message import EmailMessage
from sendEmail import template_reader
from bs4 import BeautifulSoup
import json
import re

class GMailClient:
    def sendEmail(self,contacts):
        #EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
        #EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')
        EMAIL_ADDRESS = 'sender email'
        EMAIL_PASSWORD = 'sender password'

        #contacts = ['dineshraturi22@gmail.com']

        msg = EmailMessage()
        msg['Subject'] = 'Babina Appointment'
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = contacts[2]

        value = contacts[3]

        print(values)
        #print(contacts[2])
        template = template_reader.TemplateReader()
        email_message = template.read_course_template("simple")
        #print(email_message)
        appointment = "Babina Dainostic"
        patient_name1 = str(values.get("patient_name"))
        age1 = str(values.get("Age"))
        sex1 = str(values.get("sex"))
        date1 = str(values.get("date"))
        
      

        msg.add_alternative(email_message.format(patient_name=patient_name1,age=age1,sex=sex1, date=date1), subtype='html')


        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
            #print("email sent")
    def __init__(self):
        pass