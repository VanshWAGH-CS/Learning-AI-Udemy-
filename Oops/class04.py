#self args

class Chaicup:
    size = 150 #ml

    def describe(self):
        return f"A {self.size}ml chai cup"
    

cup = Chaicup()
print(cup.describe())#this object has the context
print(Chaicup.describe(cup))#we need to pass on the context the reference "cup" here