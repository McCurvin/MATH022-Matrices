"""
MATH022 - M1 Summative Assessment
Matrices Generation and Operation

Members:
Allan Dela Cruz
Joshua Famor
Laurence Lesmoras
Mc Curvin Royeras
"""
from os import system
import numpy as np

# Test Case Matrices
A = np.array([[5, 1, 2], [1, 3, 7], [2, 7, 8]])
B = np.array([[-1], [2], [-4], [5]])
C = np.array([[0, 0], [0, 0], [0, 0]])
D = np.array([[2, 1, 3, 6, 7]])

def main():
    system('clear')
    print("Math022 - M1 Summative Assessment")
    print("Matrices Generation and Operation")
    print("Members: Allan Dela Cruz, Joshua Famor, Laurence Lesmoras, Mc Curvin Royeras\n")
    print("Generate the following matrices:")
    print("A: \n" + str(A))
    print("B: \n" + str(B))
    print("C: \n" + str(C))
    print("D: \n" + str(D))
    
    print("\n\nOperations:")
    print("1.) Given matrices (Add):")
    problem1Array1 = np.array([[2, 1, 3], [3, -2, 1], [-1, 0, 1]])
    problem1Array2 = np.array([[1, -2], [2, 1], [4, -2]])
    print("A: \n" + str(problem1Array1))
    print("B: \n" + str(problem1Array2))
    try:
        problem1Result = np.add(problem1Array1, problem1Array2)
    except ValueError as a:
        print("Error: " + str(a))
    print("\n2.) Given matrices (Multiply):")
    problem2Array1 = np.array([[2, 1, 3]])
    problem1Array2 = np.array([[-2], [1], [-3]])
    print(str(np.multiply(problem2Array1, problem1Array2)))

    print("\n3.) Given matrices (Add):")
    F = np.array([[2, -1], [3, 0], [-5, 2]])
    print("Array F: \n" + str(F))
    H = np.array([[1, 6], [-1, -2], [0, -3]])
    print("Array H: \n" + str(H))
    print("Answer: \n")
    print(str(np.add(F, H)))

main()