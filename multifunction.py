class domath:
    def function1(self, x, y):
        return x + y
    def function2(self,x,y):
        return x - y
obj1 = domath()
print(obj1.function1(2,3))
print(obj1.function2(3,2))
obj2 = domath()
print(obj2.function1(10,11))
print(obj2.function1(20,10))