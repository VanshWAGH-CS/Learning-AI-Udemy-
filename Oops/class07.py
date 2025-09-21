#base class

class Chai:

    def __init__(self, type_, strength):
        self.type = type_
        self.streangth = strength


# class GingerChai(Chai):#code duplication
#     def __init__(self, type_, strength, spice_level):
#         self.type = type_
#         self.strength = strength
#         self.spice_level = spice_level



# class GingerChai(Chai):
#     def __init__(self, type_, strength, spice_level):#Explicit call
#         Chai.__init__(self, type_, strength)
#         self.spice_level = spice_level


class GingerChai(Chai):
    #super says i am calling the parent class method
    def __init(self, type_, strength, spice_level):#super call
        super().__init__(type_, strength)
        self.spice_level = spice_level