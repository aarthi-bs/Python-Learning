def new_multiplied(k):
    return lambda x : x * k
new_double = new_multiplied(2)
new_triple = new_multiplied(3)
print(new_double(2))
print(new_triple(3))