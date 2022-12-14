##########################################
#
# Joe's Useful Functions
#
# Author: Joe Axberg
# 
# This program shows how to build a Python "module" of functions of your own
# and how to use the module both by itself and if imported into a different piece of code
#
# Either run this program by itself OR
# Use these two programs in the same directory to show how to import
# the functions in various ways
#
# program_that_imports_joes_functions_version1.py
# program_that imports_joes_functions_version2.py
#
##########################################

#factorial using recursion
def factorialr(n):
    
    #print("n is: ", n)

    if n == 1:

        return n

    else:

        return n * factorialr(n - 1)

#factorial using iteration
def factorial(n):

    result = 1

    for i in range(1,n+1):

        result = result * i

    return result

#fibonacci using recursion
def fibonaccir(n):

    #print("n is: ", n)

    #define fibonacci:  fib(n) = f(n-1) + f(n-2)
    #must start at F0 = 0 and F1 = 1

    if n <= 1:
        return n
    
    return fibonaccir(n-1) + fibonaccir(n-2)

#fibonacci using looping(iteration)
def fibonacci(n):

    #seed->start at 0 and 1
    n0 = 0
    n1 = 1

    #place to put the result
    result = 0

    for i in range(n-1):

        result = n0 + n1
        
        n0 = n1
        n1 = result

    return result

#this code will run the if this program is running as the MAIN program
#if this code is being imported into another program...python won't run the following
if __name__ == "__main__":

    #continuously print the menu
    while True:
        print("\n" + "="*40)
        print("\nJoe's Useful Function Program\n")
        print("="*40)
        print("\nPlease select one of the following:")
        print("\n1. Factorial Using Recursion\n2. Factorial Using Iteration\n\
3. Fibonacci Number Using Recurision\n4. Fibonacci Number Using Iteraction")
        
        #user enters menu selection
        selection = eval(input("\nEnter Selection: "))

        #run the function selected
        if selection == 1:

            num = eval(input("\nPlease enter a number: "))
            print("\nThe result is: ", factorialr(num))
            

        elif selection == 2:
            
            num = eval(input("\nPlease enter a number: "))
            print("\nThe result is: ", factorial(num))

        elif selection == 3:

            num = eval(input("\nPlease enter a number: "))
            print("\nThe ", num, " Fibonacci Number using Recursion is: ", fibonaccir(num))

        elif selection == 4:

            num = eval(input("\nPlease enter a number: "))
            print("\nThe ", num, " Fibonacci Number using Iteration is: ", fibonacci(num))

        else:

            print("\nYou didn't select a valid number!")



