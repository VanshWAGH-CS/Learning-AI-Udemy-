#difference between classmethod and static method

class ChaiOrder:
    def __init__(self, tea_type, sweetness, size):
        self.tea_type = tea_type
        self.sweetness = sweetness
        self.size = size

    @classmethod
    def from_dict(cls, order_data):
        return cls(
            order_data["tea_type"],
            order_data["sweetness"],    
            order_data["size"]
        )
    
    @classmethod
    def from_string(cls, order_string):
        tea_type, sweetness, size = order_string.split("-")
        return cls(tea_type, sweetness, size)
    



class ChaiUtils:
    @staticmethod
    def is_valid_size(size):
        return size in ["Small", "Medium", "Large"]
    


print(ChaiUtils.is_valid_size("Medium"))


order1 = ChaiOrder.from_dict({"tea_type": "Masala", "sweetness": "Medium", "size": "Large"})

order2 = ChaiOrder.from_string("Ginger-Low-Small")
print(order1.tea_type, order1.sweetness, order1.size)
print(order2.tea_type, order2.sweetness, order2.size)


print(order1.__dict__)
print(order2.__dict__)


