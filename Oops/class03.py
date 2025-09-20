#Attributes Shadowing

class Chai:
    temperature = "hot"
    strength = "strong"


cutting = Chai()
print(cutting.temperature)

cutting.temperature = "Mild"
print("Ater changing : ", cutting.temperature)
print("Inside the Class : ", Chai.temperature)


del cutting.temperature
print("After deleting : ", cutting.temperature)
print("Inside the Class : ", Chai.temperature)