#custom exception 

def brew_chai(flavor):
    if flavor not in ["masala", "ginger",  "lemon"]:
        raise ValueError("We do not serve this flavor")
    print(f"Brewing {flavor} chai...")
    return f"{flavor} chai is ready!"

brew_chai("masala")
brew_chai("unknown")  # This will raise a ValueError