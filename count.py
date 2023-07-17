import time
import subprocess

def countdown(t):
    while t > 0:
        print(t)
        time.sleep(1)
        t -= 1
        if t == 10:
            subprocess.call(["python", "boom3.py"])
            print("it works")
        if t == 1:
            subprocess.call(["python", "boom3.py"])
          
    
    

if __name__ == "__main__":
    countdown(171)

