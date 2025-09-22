class InvalidChaiError(Exception):
    pass

def bill(flavor, cups):
    menu = {"masala": 20, "ginger": 40}
    try:
        if( flavor not in menu):
            raise InvalidChaiError("We do not serve this flavor")
        if not isinstance(cups, int):
            raise TypeError("Cups should be a number")
        total = menu[flavor] * cups
        print(f"total bill is {total}")
    except (InvalidChaiError, TypeError) as e:
        print(f"Error: {e}")

bill("masala", 2)
bill("unknown", 2)
bill("ginger", "two")