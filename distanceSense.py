import RPi.GPIO as GPIO
import time
import configparser
import requests
import socket
import json
from simple_salesforce import Salesforce


# Read config
config = configparser.ConfigParser()
config.read('config.ini')
hostname = socket.gethostname()
print(hostname + ' running as user: '+ config['SALESFORCE']['USERNAME'])

#Declare GPIO Setup
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Connect to Salesforce
sf = Salesforce(
    username=config['SALESFORCE']['USERNAME'],
    password=config['SALESFORCE']['PASSWORD'],
    security_token=config['SALESFORCE']['TOKEN'],
    domain=config['SALESFORCE']['DOMAIN'])
# Fetch train IP
device = sf.apexecute('Device/Train', method='GET')
trainIp = device['Last_Known_IP__c']
print('Train last known IP: '+ trainIp)
trainStopUrl = 'http://'+ trainIp +':8080/api/train/stop'



print('Scanning...')
try:
    while True:
        sensorValue = GPIO.input(12)
        if sensorValue == 1:
            print('Stopping train')
            time.sleep(float(config['TRAIN']['STOP_DELAY']))

            payload = { 'sender': hostname }
            headers = {'content-type': 'application/json'}
            response = None
            while True:
                try:
                    response = requests.post(trainStopUrl, data=json.dumps(payload), headers=headers, timeout=5)
                except:
                    print('REST call timed out after 5s, retrying in 1s')
                    response = None
                if response is not None and response.ok == True:
                    break
                time.sleep(1)
            time.sleep(float(config['TRAIN']['SCAN_RESUME_DELAY']))
            print('Resuming scan')
        time.sleep(0.1)
except KeyboardInterrupt:
    GPIO.cleanup()
