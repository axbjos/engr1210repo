#different way to select one function from a python module vs. importing everything
from joes_useful_functions import factorial

#import as if you want to use a different name for the function in your code
from joes_useful_functions import fibonacci as fb

def main():

    print(factorial(5))

    print(fb(5))

main()