
# First, I am going to write a function to check if the given number is prime:
def isprime(number):
    if number%2 == 0:
        return False
    else:
        for n in range(3,number,2):
            if number%n == 0:
                return False
        return True


# Using a mathematical formula for perfect numbers, I am going to write a function to find perfect numbers up to a given number:
def getPerfectNumbers(number):
    perfect_numbers = []
    perfect_number = 0
    power = 2
    while True:
        perfect_number = (2**(power-1))*((2**power)-1)
        if perfect_number > number:
            break
        if isprime((2**power)-1):
            perfect_numbers.append(perfect_number)
        power += 1
    return perfect_numbers


# Now I am going to write a function for an interactive program:
def interactive():
    """
    Interactive program to find perfect numbers.
    """
    while True:
        try:
            number = int(input("Enter a number: "))
            if number < 0:
                raise Exception
            the_list = getPerfectNumbers(number)
            break
        except:
            print("Please enter a positive integer!")
    if len(the_list) != 0:
        print("Here is the list of your perfect numbers:", *map(lambda x: str(x)+',', the_list[:-1]), str(the_list[-1])+'.', sep=" ")
    else:
        print("There are no perfect numbers in this range!")


# Launching the program!
interactive()