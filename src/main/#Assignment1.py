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

def AlternatingSeries(x, errorOfTenToThe):
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

def f(x):
    return (x + 4) * x * x - 10

def IsNegative(x):
    if(x < 0):
        return True
    else:
        return False

def ShareSigns(x, y):
    #if they are both positive or both negative, will be True
    #otherwise, will be false
    return IsNegative(x) == IsNegative(y)

def Bisection(a, b, tolerance):
    #
    iterations = 0
    error = tolerance + 1
    left = a
    right = b

    while(error >= tolerance):
        iterations = iterations + 1
        midpoint = (left + right) / 2
        fLeft = f(left)
        fRight = f(right)
        fMid = f(midpoint)

        temp = 0
        #if left and mid share a sign, then new midpoint should be between mid and right
        #visca versca for if right and mid share a sign
        if(ShareSigns(fLeft, fMid)):
            temp = right
            left = midpoint
        else:
            temp = left
            right = midpoint

        error = numpy.abs(temp - midpoint)

    return iterations

def derivativeF(x):
    #f'(x) = 3x^2 + 8x, or (3x + 8)x
    return (3 * x + 8) * x

def NewtonRaphson(a, b, tolerance):
    iterations = 0
    approx = (a + b) / 2

    while(True):
        iterations = iterations + 1
        if(derivativeF(approx) != 0):
            nextApprox = approx - (f(approx) / derivativeF(approx))

            if(numpy.abs(nextApprox - approx) < tolerance):
                return iterations
            else:
                approx = nextApprox
        else:
            return f"Unsuccessful: derivative was 0 after {iterations} iterations"

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
print(f"{AlternatingSeries(1, -4)}\n")

#problem 6
print(f"{Bisection(-4, 7, pow(10, -4))}")
print(f"{NewtonRaphson(-4,7, pow(10, -4))}\n")
