import threading
import time

def monitor_tea_temp():
    while True:
        print(f"Monitoring tea temperature...")
        time.sleep(2)

t = threading.Thread(target=monitor_tea_temp)
t.start()


#what is the difference this non demon thread will be keep running
print("Main program done")