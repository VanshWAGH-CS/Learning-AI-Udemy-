import threading

chai_stock = 0

def restock():
    global chai_stock
    for _ in range(100000):
        chai_stock += 1

threads = [ threading.Thread(target=restock) for _ in range(2)]

for t in threads: t.start()
for t in threads: t.join()

print("Chai stock: ", chai_stock)

#profiling : 
#python shows time spend on each thead
#python -m cProfile -s time 09_race_condition.py this is the command