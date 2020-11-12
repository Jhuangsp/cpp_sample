
# g++ -c main.cpp
# g++ -static -shared -o main.dll main.o


from ctypes import cdll, c_float
import os 
# lib = WinDLL("./main.dll")
lib = cdll.LoadLibrary("./main.dll")
i = lib.hello()
print("i", i)

print("4+5=", lib.add_int(4,5))
lib.add_float.restype = c_float
print("5.5+4.1=", lib.add_float(c_float(5.5), c_float(4.1)))