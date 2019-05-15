#!/usr/bin/env python3

import os
import configparser
import smtplib
from email.message import EmailMessage
import subprocess


def check_staking():
   
    command = ("""
    staking="$$$PATH getstakingstatus"
    $staking
    """).replace("$$$PATH", core_path)

    result = os.popen(command).read()
    
    if "false" in result:
        send_mail(result)
    
    return
        


def send_mail(value):

    email_message = EmailMessage()
    email_message['Subject'] = str(topic)
    email_message['From'] = str(from_email)
    email_message['To'] = str(to_email)
    email_message.set_content(str(value))

    connect_email = smtplib.SMTP_SSL(address, str(port_email))
    connect_email.ehlo()
    connect_email.login(username, password)
    connect_email.send_message(email_message)
    connect_email.close()

    return



if __name__ == "__main__":

    config = configparser.RawConfigParser()

    config_file = os.path.join(os.path.dirname(__file__), 'config.ini')
    config.read(config_file)

    address = config['SMTP']['address']
    username = config['SMTP']['username']
    password = config['SMTP']['password']
    port_email = config['SMTP']['port']
    from_email = config['SMTP']['from']
    to_email = config['SMTP']['to']

    topic = config['MESSAGE']['topic']

    core_path = config['ENERGI']['core_path']

    check_staking()