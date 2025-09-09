class Chai:
    def  __init__(self, sweetness, milk_level):
        self.sweentness = sweetness
        self.milk_level = milk_level
    
    def sip(self):
        print("sipping chai")

    def add_sugar(self, amount):
        print("adding sugar")

    my_chai = Chai (sweetness=3, milk_Level=2)

    my_chai.add_sugar(2)