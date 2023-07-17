import time
import subprocess

def sleep_and_run(t):
    time.sleep(t)
    subprocess.call(["python", "expld.py"])
    time.sleep(11)
    subprocess.call(["python", "expld.py"])

if __name__ == "__main__":
    sleep_and_run(73)
