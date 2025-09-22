chai_menu = {"masala" : 30, "ginger" : 40}

try:
    print(chai_menu["elaichi"])
except KeyError:
    print("Key not found in dictiionary")

print("Hello World")