# file = open("order.txt", "w")

# try:
#     file.write("Masala chai - 2 cups")
# finally:
#     file.close()

with open("order.txt", "w") as file:
    file.write("giger tea 4 cups")

#this is done using dunder
# file.__enter__()
# file.__exit__()