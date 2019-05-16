# What is this??

This is a repo for a Distance Sensor with a Raspberry Pi to function as a Trip Wire and send that signal to Salesforce.

This is a small peice of the Robotics Ridge functionality for **TrailheaDX2019**. 

# Physical Install
This repository is meant to be run with the following hardware:
* Raspberry PI 3 B+ - https://www.sparkfun.com/products/14643
* Infrared Proximity Sensor Short Range - Sharp GP2Y0A41SK0F - https://www.sparkfun.com/products/12728
* Cana Kit - https://www.canakit.com/raspberry-pi-adapter-power-supply-2-5a.html (I prefer this since it comes with a handy on/off switch!)
* JST to Breadboard Jumper (3-pin) - https://www.sparkfun.com/products/13685
* Various Jumper Wires (F/F, M/M, M/F) - https://www.sparkfun.com/products/11710, https://www.sparkfun.com/products/11709, https://www.sparkfun.com/products/12794 

## GPIO 

Pin 2 - Power (Red cable)

Pin 4 - Ground (Black)

Pin 12 - Signal (Yellow)

![](https://github.com/slychika/pi_distance_sensor/blob/master/images/piAndSensorImage.jpg)


# Install
I am using Rasbian Strech Lite, but any OS from here should work: https://www.raspberrypi.org/downloads/raspbian/

Make sure you have Python installed 

Be sure to update/install RPi.GPIO

`pip install RPi.GPIO`

# Run the program
`python distanceSense.py`