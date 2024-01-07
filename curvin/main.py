import numpy

# 1. Generate the following matrices:
print("This is a:")
matA = numpy.array([[5, 1, 2], [1, 3,7], [2, 7, 8]])
print(matA)
print("--------------")
print("This is b:")
matB = numpy.array([[-1], [2], [-4], [5]])
print(matB)
print("--------------")
print("This is c:")
matC = numpy.array([[0, 0], [0, 0], [0, 0]])
print(matC)
print("--------------")
print("This is d:")
matD = numpy.array([[2, 1, 3, 6, 7]])
print(matD)

print("--------------")
#2. Perform the following:
print("Beyond this is for number 2 \"perform the following\"")
matE = numpy.array([[2, 1, 3,], [3, -2, 1], [-1, 0, 1]])
matF = numpy.array([[1, -2], [2, 1], [4, -2]])
print("--------------")
#add matE and matF, and the result should be Not Possible
try:
    result = numpy.add(matE, matF)
except ValueError:
    print("The answer to 2.1 is Not Possible")

print("--------------")
print("--------------")
matG = numpy.array([[2, 1, 3]])
matH = numpy.array([[-2], [1], [-3]])
#Multiply the two matrices and it should result to -12
print("The product is: ")
print(matG)
print(matH)
print("--------------")
print("The result of item 2.2 or multiplying the two matrices is: ")
print(numpy.dot(matG, matH))

print("--------------")
print("--------------")
matI = numpy.array([[2, -1], [3, 0], [-5, 2]]) #This is matrix F
matJ = numpy.array([[1, 6], [-1, -2], [0, -3]]) #This is matrix H

#Adding the two matrices
print("The answer 2.3 is: ")
print(numpy.add(matI, matJ))

print("--------------")
print("--------------")
matK = numpy.array([[3, -1], [-2, 2]]) #This is C
matL = numpy.array([[2, 0], [1, 4]]) #This is A

#Subtracting the two matrices
print("The answer 2.4 is: ")
print(numpy.subtract(matK, matL))

print("--------------")
matM = numpy.array([[1, 0, -3], [-2, 4, 1]])
matN = numpy.array([[1, 0, 4, 1], [-2, 3, -1, 5], [0, -1, 2, 1]])
print("The answer for item 2.5 is: ")
print(numpy.dot(matM, matN))


print("--------------")
print("--------------")
matO = numpy.array([[1, -2], [0, 4], [-3, 1]]) #This is C
matP = numpy.array([[2, -1], [3, 0]]) #This is D
print("The result for item 2.6 is: ")
try:
    result = numpy.dot(matP, matO)
except ValueError:
    print("Not Possible")

