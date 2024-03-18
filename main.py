import schedule, time, os, smtplib # Import the smtp library
import random,requests,json
from replit import db
from email.mime.multipart import MIMEMultipart # Import the mime library to create multipart messages
from email.mime.text import MIMEText # Import the mime library to create text messages
from bs4 import BeautifulSoup

response=requests.get("https://zenquotes.io/api/random")
json_data=json.loads(response.text)
quote=json_data[0]['q'] + " -" +json_data[0]['a']


password = os.environ['mailPassword']
username = os.environ['mailUsername']

def sendMail():
  
    
  email = quote # Contents of the message
  server = "smtp.gmail.com" # Address of the mail server, change it to yours if you need to
  port = 587 # Port of the mail server, change it to yours if you need to
  s = smtplib.SMTP(host = server, port = port) # Creates the server connection using the host and port details
  s.starttls() # Sets the encryption mode
  s.login(username, password) # Logs into the email server for us

  msg = MIMEMultipart() # Creates the message
  msg['To'] = "chijn.kong.156@gmail.com" # Sets the receiver's email address
  msg['From'] = username # Sets the sender's email address
  msg['Subject'] = "Always Remember!"
  msg.attach(MIMEText(email, 'html')) # Attaches the email content to the message as html

  s.send_message(msg) # Sends the message
  del msg # Deletes the message from memory

sendMail() # Call the subroutine to test it.



schedule.every().day.at("08:00").do(sendMail) # Sets the schedule

while True:
  schedule.run_pending()
  time.sleep(1)
