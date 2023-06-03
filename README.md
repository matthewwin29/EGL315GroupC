
this is the start of EGL315's project github reporsitory.
# **EGL315 GROUP C**

This **markdown document** will explain the steps necessary to install the required libraries to run the feature's python script, a detailed explanation of the funtions of the code, the reasoning for the theme I selected for the project and my intention on how it would interact with the audience during the End Of Semester showcase.

# Syntax
1. ## Theme
    1. Theme choice
    2. Intention of use
2. ## Research
    1. Benefits of Interactive Features

# Theme

## **Theme choice**
The theme we have chosen for our 315 Module is **Multiplayer Bomb Defusal**, We chose this theme as we want to give our players a thrilling experience as they try to defuse a bomb within 20 or 30 seconds while also making it competitive between 2 humans.


## **Intention of use**
We intend to give our users/players a memorable, immersive, competitive and interactive multiplayer experience that will require them to click buttons according to a sequence to make it our "alive".

## **Hardware Used**
- Raspberry Pi
- Christie's Pandora Box
- Speakers
- Lighting
- Buttons


# Research

## Benefits of Interactive Features
- Immersive Experience: The combination of lights, surround sound, and high-quality video creates an immersive experience for the audience.
- Enhanced Engagement: The use of lights, surround sound, and good video can enhance engagement by capturing and holding the attention of the viewers
- Memorable Experience: The combination of lights, surround sound, and good video can create a memorable experience that stays with the viewers long after the project is over.

## System Diagram
## Control
![Alt text](images/control%20system%20diagram1.jpg)


## Video
![Alt text](images/video%20system%20diagram.jpg)

## Audio
![Alt text](images/audio%20system%20diagram.jpg)

## Lighting
![Alt text](images/lighting%20system%20diagram.jpg)


![](images/Pi4.jpg)

[source](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/)

## StoryBoard

![Alt text](Images/0.PNG)
![Alt text](Images/1.PNG)
![Alt text](Images/2.PNG)
![Alt text](Images/3.PNG)
![Alt text](Images/4.PNG)




## Code:

import RPi.GPIO as GPIO
import time
import socket
import random


TCP_IP = '192.168.254.11'
TCP_PORT = 5612
BUFFER_SIZE = 1024
MESSAGE = b'Easy'
MESSAGE1 = b'Hard'
MESSAGE2 = b'0'
MESSAGE3 = b'Correct'
MESSAGE4 = b'Wrong'
MESSAGE5 = b'correct'



GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.IN)
GPIO.setup(16,GPIO.IN)
GPIO.setup(17,GPIO.IN)
GPIO.setup(22,GPIO.IN)
GPIO.setup(26,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(6,GPIO.OUT)
GPIO.setup(5,GPIO.IN)


s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((TCP_IP,TCP_PORT))


while True:
    light = random.randint(1,2)
    if GPIO.input(16):
        GPIO.output(26, True)
        s.send(MESSAGE3)
        time.sleep(1)
        s.send(MESSAGE2)
        time.sleep(1)
        
    elif GPIO.input(17):
        GPIO.output(27, True)
        s.send(MESSAGE3)
        time.sleep(1)
        s.send(MESSAGE2)
        time.sleep(1)
        
    elif GPIO.input(22):
        GPIO.output(6, True)
        s.send(MESSAGE5)
        time.sleep(1)
        s.send(MESSAGE2)
        time.sleep(1)
        
    elif GPIO.input(5):
        GPIO.output(23, True)
        s.send(MESSAGE4)
        time.sleep(1)
        s.send(MESSAGE2)
        time.sleep(1)
        
        
        
        
    
    elif GPIO.input(24):
        print (light)
        if light == 1:
            s.send(MESSAGE)
            time.sleep(1)
            s.send(MESSAGE2)
        elif light == 2:
            s.send(MESSAGE1)
            time.sleep(1)
            s.send(MESSAGE2)
    else:
            GPIO.output(23,False)
            GPIO.output(26,False)
            GPIO.output(27,False)
            GPIO.output(6,False

## References

https://www.youtube.com/watch?v=Wa5aasz5VXg&ab_channel=RottenTomatoesTrailers - trailer(scene 0)

https://www.youtube.com/watch?v=qEX7iznFi3E - Audio Spectrum(wave)

https://www.topmediai.com/text-to-speech/ - Used for dialouge 

https://www.youtube.com/watch?v=OYrTQsi1NtE&t=4s - C4 Bomb with Timer

https://www.youtube.com/watch?v=7guNNC2QEKo - Timer Ticking Noise

https://www.youtube.com/watch?v=RfUKmEDNlsA - Explosion

https://www.youtube.com/watch?v=_ttHanoHTL4 - explosion sound







 
