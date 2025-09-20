#Name Space in OOPS

class Chai:
    origin = "India"

print(Chai.origin)

Chai.is_hot = True
print(Chai.is_hot)

#createing object from class Chai
masala = Chai()
print(f"Masala {masala.origin}")
print(f"Masala {masala.is_hot}")

masala.is_hot = False

print("Class attribute", Chai.is_hot)
print(f"Masala {masala.is_hot}")

masala.flavor = "Masala"
print(masala.flavor)