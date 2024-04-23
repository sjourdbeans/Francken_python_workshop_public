
class Table:
    """
    A very introduction to the use of a class and what it means to have an object in python.
    """
    def __init__(self, colour, material):
        """
        Initialise the class by setting its intitial variables called attributes.
        """
        self.colour=colour
        self.material=material
        self.price=200          #price in euros
        self.assembled=False

    def build(self):
        """
        Use methods to change the attributes of an object.
        """
        self.assembled=True

    def paint(self,new_colour):
        """
        Change attribute by giving an extra variable.
        """
        self.colour=new_colour
    
    def discount(self):
        self.price=self.price*0.5

    def info(self,discount=False):
        """
        Returns a string with the info about the table. You can also call methods in other methods
        """
        if discount==True:
            self.discount()

        return f"{self.colour} table made of {self.material} for only €{self.price}"
    
    
    



