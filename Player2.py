import RPi.GPIO as GPIO
import time
import socket
import subprocess


TCP_IP = '192.168.254.11'
TCP_PORT = 5612
BUFFER_SIZE = 1024
MESSAGE = b'Easy'
MESSAGE2 = b'0'
MESSAGE3 = b'Correct'
MESSAGE4 = b'Wrong'
MESSAGE5 = b'correct'
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(22,GPIO.IN)
GPIO.setup(24,GPIO.IN)
GPIO.setup(5,GPIO.IN)
GPIO.setup(6,GPIO.IN)
GPIO_TRIGGER = 20
GPIO_ECHO = 21
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

def distance():
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
    StartTime = time.time()
    StopTime = time.time()
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
    TimeElapsed = StopTime - StartTime
    distance = (TimeElapsed * 34300) / 2

    return distance

count = 0

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((TCP_IP,TCP_PORT))

subprocess.run(["python","static.py"])

count = 0


while True:
    
    if GPIO.input(24):
        count = count +1
        print (count)
        time.sleep(1)
        if count == 1:
            s.send(MESSAGE4)
            subprocess.run(["python","rightred.py"])
            time.sleep(1)
            subprocess.run(["python","rightred.py"])
            subprocess.run(["python","staticPL.py"])
            s.send(MESSAGE2)
            time.sleep(1)
        elif count == 2:
            s.send(MESSAGE4)
            subprocess.run(["python","rightredON.py"])
            time.sleep(1)
            subprocess.run(["python","rightred.py"])
            subprocess.run(["python","staticPL.py"])
            s.send(MESSAGE2)
            time.sleep(1)
        else:
            s.send(MESSAGE3)
            subprocess.run(["python","Seq1LrRg.py"])
            time.sleep(1)
            subprocess.run(["python","Seq1LrRg.py"])
            subprocess.run(["python","staticPL.py"])
            s.send(MESSAGE2)
            time.sleep(1)    
        
    elif GPIO.input(5):
        count = count +1
        print (count)
        time.sleep(1)
        if count == 1:        
            s.send(MESSAGE5)
            
            subprocess.run(["python","Seq1LrRg.py"])
            time.sleep(1)
            subprocess.run(["python","Seq1LrRg.py"])
            subprocess.run(["python","staticPL.py"])
            s.send(MESSAGE2)
            time.sleep(1)
        else:
            s.send(MESSAGE4)
            subprocess.run(["python","rightred.py"])
            time.sleep(1)
            subprocess.run(["python","rightred.py"])
            subprocess.run(["python","staticPL.py"])
            s.send(MESSAGE2)
            time.sleep(1)
        
        
        
    elif GPIO.input(6):
        count = count + 1
        print (count)
        time.sleep(1)
        if count == 1:
            s.send(MESSAGE4)
            subprocess.run(["python","rightred.py"])
            time.sleep(1)
            subprocess.run(["python","rightred.py"])
            subprocess.run(["python","staticPL.py"])
            s.send(MESSAGE2)
            time.sleep(1) 
        elif count == 2:
            s.send(MESSAGE5)
            subprocess.run(["python","Seq1LrRg.py"])
            time.sleep(1)
            subprocess.run(["python","Seq1LrRg.py"])
            subprocess.run(["python","staticPL.py"])
            s.send(MESSAGE2)
            time.sleep(1)
        elif count == 3:
            s.send(MESSAGE4)
            subprocess.run(["python","rightred.py"])
            time.sleep(1)
            subprocess.run(["python","rightred.py"])
            subprocess.run(["python","staticPL.py"])
            s.send(MESSAGE2)
            time.sleep(1)
        
            

    #start of the game put timer bomb and static light shit here
    elif GPIO.input(22):
        print("start")
        subprocess.run(["python","staticTut.py"])
        subprocess.Popen(["python", "timer.py"])
        s.send(MESSAGE)
        time.sleep(1)
        s.send(MESSAGE2)
        subprocess.Popen(["python","staticGM.py"])
        time.sleep(1)
        

            
            
    elif __name__ == '__main__':
        try:
            dist = distance()
            if dist  >= 2 and dist <= 5:
                subprocess.run(["python", "Clue1.py"])
                
                
            elif dist >= 25 and dist <= 30:
                subprocess.run(["python", "yamaha.py"])
                
            
                              
        except KeyboardInterrupt:
            print("gg")
                
                
 
            
            
    
    
            
            

            
        

