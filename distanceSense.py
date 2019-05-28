import RPi.GPIO as GPIO
import time
import configparser
import requests

from simple_salesforce import Salesforce


# Read config
config = configparser.ConfigParser()
config.read('config.ini')
print('Running as user: '+ config['SALESFORCE']['USERNAME'])

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
            time.sleep(int(config['TRAIN']['STOP_DELAY']))
            requests.post(trainStopUrl)
            time.sleep(int(config['TRAIN']['SCAN_RESUME_DELAY']))
            print('Resuming scan')
        time.sleep(0.1)
except KeyboardInterrupt:
    GPIO.cleanup()
