import math
import argparse

argumentParser = argparse.ArgumentParser(description='Calculate the La Grange Bound Error or the degree of polynomial required to attain a certain error for Common Functions')

argumentParser.add_argument('function', action='store', choices=['exp', 'log', 'sin', 'cos'], help='The common function you wish to approximate with a maclaurin/taylor series. The current version supports exponentials ("exp"), logarithms ("log"), and oscillating functions ("sin" or "cos")', metavar='function')
argumentParser.add_argument('x', action='store', type=float, help='The x value you wish to approximate', metavar='x-value')
argumentParser.add_argument('-c','--center', action='store', default=0, type=float, help='The value the taylor series is centered at, if you are using a taylor series')
argumentParser.add_argument('-d','--degree', action='store', type=int, default=0, help='The degree of the maclaurin or taylor series polynomial you are using', metavar='degree')
argumentParser.add_argument('-e','--error', action='store', default=0, type=float, help='The error value as a decimal, the return value will be the degree polynomial you need to use to achieve at least this level of precision')

argumentValues = vars(argumentParser.parse_args())

def SimpleLaGrangeError(center, error, func, x, degree):
    if(error != 0):
        for n in range(1, 100):
            result=round(math.fabs((UpperBoundWithDegree(func, x, n, center)/(math.factorial(n+1))) * ((x-center)**(n+1))), 10)
            if(result <= error):
                return n
    return round(math.fabs((UpperBoundWithDegree(func, x, degree, center)/(math.factorial(degree+1))) * ((x-center)**(degree+1))), 10)

def UpperBoundWithDegree(function, x, degree, c):
    if(function=='sin' or function=='cos'):
        return 1
    if(function=='exp'):
        return (math.e)**(math.ceil(x))
    if(function=='log'):
        return ((-1)**degree)*(math.factorial(degree)/(min([x, c])**(degree+1)))

print(SimpleLaGrangeError(argumentValues['center'], argumentValues['error'], argumentValues['function'], argumentValues['x'], argumentValues['degree']))