import RPi.GPIO as GPIO
import time

import salesforce_requests_oauthlib import SalesforceOAuth2Session
import salesforce_streaming_client import SalesforceStreamingClient
import salesforce_streaming_client import _decode_set
import salesforce_streaming_client import _encode_set

import json

#Declare GPIO Setup
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#Declare Salesforce Setup
salesforce_client_id = ''
salesforce_client_secret = ''
username = ''
password = ''

EVENT_TRAIN_STOP = 'Train_Stop'




try:
    while True:
        print(GPIO.input(12))
        time.sleep(1)
        print('--')
except KeyboardInterrupt:
    GPIO.cleanup()
