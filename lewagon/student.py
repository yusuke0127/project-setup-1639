from datetime import date

class Student:
    # Constructor function
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    # Instance method
    def says(self, something):
        print(f"{self.name} says {something}")
        
    # Class method
    @classmethod
    def from_birth_year(cls, name, birth_year): # Note the `cls` parameter
        # Student("yann", brith_year)
        return cls(name, date.today().year - birth_year)
    
    def where_am_i(self):
        print(__file__)