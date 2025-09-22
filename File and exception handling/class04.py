#custom exception
class OutOfIngredientsError(Exception):
    pass

def make_chai(milk, sugar):
    if milk == 0 or sugar == 0:
        raise OutOfIngredientsError("missing milk or sugar")
    print("chai is ready")

make_chai(0, 1)