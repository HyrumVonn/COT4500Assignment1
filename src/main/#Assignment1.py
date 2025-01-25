#Assignment 1
import struct
import numpy

#double precision = 64 bits
#given string:
#0 10000000111 111010111001
#0 11 52
def FloatFromBinString(binary_data):
    for i in range(0, 64 - len(binary_data)):
        binary_data = binary_data + "0"

    sign = pow(-1, int(binary_data[0]))

    exponent = 0

    for i in range(1, 12):
        exponent = exponent + int(binary_data[i]) * pow(2, 11-i)

    mantissa = 0

    for i in range(12, 64):
        mantissa = mantissa + int(binary_data[i]) * pow(0.5, i - 11)

    return sign * pow(2, (exponent - 1023)) * (1 + mantissa)

def AbsoluteError(p, pStar):
    return numpy.abs(p - pStar)

def RelativeError(p, pstar):
    return AbsoluteError(p, pstar) / numpy.abs(p)

def InfiniteSeries(x, errorOfTenToThe):
    acceptableError = pow(10, errorOfTenToThe)

    result = 0
    k = 0

    loop = True

    while(loop):
        k = k + 1
        kthTerm = pow(-1, k) * (pow(x, k) / (pow(k, 3)))
        
        #result will be the partial sum. we don't need it, but I like
        #having it
        result = result + kthTerm
        
        #print(f"{k}th Term: {kthTerm}")

        currentError = numpy.abs(kthTerm)
        if(currentError < acceptableError):
            loop = False

    return k

floatVal = FloatFromBinString('010000000111111010111001')

float3DigitRounded = float(f"{(floatVal + .0005):.3f}")
#problem 1
print(f"{floatVal:.5f}\n")

#problem 2
print(f"{floatVal:.3f}\n")

#problem 3
print(f"{float3DigitRounded}\n")

#problem 4 Errors:
print(AbsoluteError(floatVal, float3DigitRounded))
print(RelativeError(floatVal, float3DigitRounded))
print("")

#problem 5
print(f"{InfiniteSeries(1, -4)}\n")

#problem 6
print("Problem 6 Answer\n")
