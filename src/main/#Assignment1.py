#Assignment 1
import struct
import numpy

#double precision = 64 bits
#given string:
#0 10000000111 111010111001
#0 11 52
binary_data = '010000000111111010111001'

for i in range(0, 64 - len(binary_data)):
    binary_data = binary_data + "0"

#print(type(binary_data))
#print(binary_data)
#print(len(binary_data))

sign = pow(-1, int(binary_data[0]))
#print(f"Sign is {sign}")

exponent = 0

for i in range(1, 12):
    #print(f"exponent {exponent} on i {i}")
    exponent = exponent + int(binary_data[i]) * pow(2, 11-i)
    #print(f"i {i}, added {int(binary_data[i])} * 2^{(11-i)} to get new exponent {exponent}")

mantissa = 0

for i in range(12, 64):
    #print(f"Mantissa {mantissa} on i {i}")
    mantissa = mantissa + int(binary_data[i]) * pow(0.5, i - 11)
    #print(f"i {i}, added {int(binary_data[i])} * 1/2^{(i-11)} to get new mantissa {mantissa}")

floatVal = sign * pow(2, (exponent - 1023)) * (1 + mantissa)

#print(type(floatVal))
#print(floatVal)
print(f"{floatVal:.5f}")
