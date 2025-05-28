# debug_example.py
import pdb

def multiply(x, y):
    pdb.set_trace()
    return x * y

print(multiply(3, 4))