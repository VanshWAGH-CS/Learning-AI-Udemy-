import threading
import time

def boil_milk():
    print(f"Boiling milk...")
    time.sleep(2)
    print(f"Milk Boiled...")

def toast_bun():
    print(f"Toasting bun...")
    time.sleep(3)
    print(f"Done with bun toast...")
    
start = time.time()

t1 = threading.Thread(target=boil_milk)#t1 runs the boil_Milk by storing the reference
t2 = threading.Thread(target=toast_bun)

t1.start()
t2.start()
t1.join()
t2.join()

end = time.time()#end of time we calculate how much time it takes to run a thread

print(f"Breakfast is ready in {end - start:.2f} seconds")#.2f means till 2 decimal places float value