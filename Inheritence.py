#Parentclass
from multiobjects import Ashok


class Parent:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    def method(self):
       print(self.first_name,self.last_name)
obj = Parent("Ashok", "Thirunavukarasu")
obj.method()
#Childclass
class child(Parent):
   pass
obj1 = child("Ashok", "T")
obj1.method()