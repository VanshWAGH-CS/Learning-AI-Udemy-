import threading
import time

def prepare_chai(type_, wait_time ):
    print(f"{type_} chai: brewing...")
    time.sleep(wait_time)
    print(f"{type_} chai: Ready.")


t1 = threading.Thread(target=prepare_chai, args=("Masala", 2))#a wait for 2 seconds
t2 = threading.Thread(target=prepare_chai, args=("Ginger", 4))

t1.start()
t2.start()
t1.join()

#join is used here to wait for the thread to complete before moving to the next line of code
t2.join()

#both threads runs concurantly t1 for 2 seconds and t2 for 3 seconds


