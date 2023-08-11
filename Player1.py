import RPi.GPIO as GPIO
import time
import socket
import subprocess


TCP_IP = '192.168.254.11'
TCP_PORT = 5612
BUFFER_SIZE = 1024
MESSAGE = b'Correct2'
MESSAGE1 = b'correct2'
MESSAGE2 = b'Wrong2'
MESSAGE3 = b'0'




GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(22,GPIO.IN)
GPIO.setup(24,GPIO.IN)
GPIO.setup(5,GPIO.IN)

GPIO_TRIGGER1 = 19
GPIO_ECHO1 = 26

GPIO.setup(GPIO_TRIGGER1, GPIO.OUT)
GPIO.setup(GPIO_ECHO1, GPIO.IN)


    

def distance1():

    GPIO.output(GPIO_TRIGGER1, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER1, False)
    StartTime = time.time()
    StopTime = time.time()
    while GPIO.input(GPIO_ECHO1) == 0:
        StartTime = time.time()
    while GPIO.input(GPIO_ECHO1) == 1:
        StopTime = time.time()
    TimeElapsed = StopTime - StartTime
    distance1 = (TimeElapsed * 34300) / 2

    return distance1

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((TCP_IP,TCP_PORT))


count = 0

while True:
    if GPIO.input(22):
        count = count + 1
        print (count)
        time.sleep(1)
        if count == 1:
            s.send(MESSAGE1)
            subprocess.run(["python", "Seq2ON.py"])
            time.sleep(1)
            subprocess.run(["python", "Seq2.py"])
           
            subprocess.run(["python", "static.py"])
            s.send(MESSAGE3)
            time.sleep(1)
        else:
            s.send(MESSAGE2)
            subprocess.run(["python", "Seq1ON.py"])
            time.sleep(1)
            s.send(MESSAGE3)
            subprocess.run(["python", "Seq1.py"])
            subprocess.run(["python", "Seq1.py"])
            subprocess.run(["python", "static.py"])
            time.sleep(1)
            
    elif GPIO.input(24):
        count = count + 1
        print (count)
        time.sleep(1)
        if count == 1:
            s.send(MESSAGE2)
            subprocess.run(["python", "Seq1ON.py"])
            time.sleep(1)
            subprocess.run(["python", "Seq1.py"])
            subprocess.run(["python", "Seq1.py"])
            subprocess.run(["python", "static.py"])
            s.send(MESSAGE3)
            time.sleep(1)
        elif count == 2:
            s.send(MESSAGE1)
            subprocess.run(["python", "Seq2ON.py"])
            time.sleep(1)
            subprocess.run(["python", "Seq2.py"])
           
            subprocess.run(["python", "static.py"])
            s.send(MESSAGE3)
            time.sleep(1)
        elif count == 3:
            s.send(MESSAGE2)
            subprocess.run(["python", "Seq1ON.py"])
            time.sleep(1)
            subprocess.run(["python", "Seq1.py"])
            subprocess.run(["python", "Seq1.py"])
            subprocess.run(["python", "static.py"])
            s.send(MESSAGE3)
            time.sleep(1)
            
    elif GPIO.input(5):
        count = count + 1
        print (count)
        time.sleep(1)
        if count == 3:
            s.send(MESSAGE)
            subprocess.run(["python", "Seq2ON.py"])
            time.sleep(1)
            subprocess.run(["python", "Seq2.py"])
           
            subprocess.run(["python", "static.py"])
            s.send(MESSAGE3)
            time.sleep(1)
        else:
            s.send(MESSAGE2)
            subprocess.run(["python", "Seq1ON.py"])
            time.sleep(1)
            subprocess.run(["python", "Seq1.py"])
            subprocess.run(["python", "Seq1.py"])
            subprocess.run(["python", "static.py"])
            s.send(MESSAGE3)
            time.sleep(1)
            
    elif __name__ == '__main__':
        try:
            dist1 = distance1()
            
            if dist1 >= 2 and dist1 <= 5:
                print("picture")
                subprocess.run(["python", "Clue2.py"])
                time.sleep(1)
                
            
            elif dist1 >= 25 and dist1 <= 30:
                print("audio")
                subprocess.run(["python","yamaha2.py"])
                time.sleep(1)
                
            
            
                
                
                
                
                
        except KeyboardInterrupt:
            print("gg")
     
           