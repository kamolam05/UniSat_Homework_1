from functools import reduce


# WARNING!!! Because my list of prime numbers contains only the first 1000 primes, the program will work only with numbers up to 1000!


# First of all, I need a list of prime numbers from 0 to 1000:
list_of_prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]


# Now I am going to write a function to find all prime divisors of any given number:
def getPrimeDivisors(number):
    """
    For the given number finds all the prime divisors and their powers (how many times the number can be divided by this particular prime).
    Returns a dictionary of these prime divisors in a format: {'prime divisor': 'power'}
    """
    primes = list(filter(lambda x: x<=number, list_of_prime_numbers))
    divisors = {}
    for prime in primes:
        if number%prime == 0:
            count = 1
            number = number/prime
            while True:
                if number%prime == 0:
                    count += 1
                    number = number/prime
                else:
                    break
            divisors[prime] = count
        else:
            pass
    return divisors


# Now I am going to write a function to calculate the sum of all divisors, except itself, of any given number (Using a special mathematical formula):
def sumDivisors(number):
    """
    Finds the sum of all divisors of the given number using a special mathematical formula.
    Then substracts the number itself from this sum.
    Returns the final answer.
    """
    prime_divisors = getPrimeDivisors(number)
    list_to_multiply = []
    for key in prime_divisors:
        to_list = 1
        for power in range(1, prime_divisors[key]+1):
            to_list += key**power
        list_to_multiply.append(to_list)
    divisors_sum = reduce(lambda x, y: x*y, list_to_multiply) - number
    return divisors_sum


# Now I am going to write the final function to find all perfect integers up to the given number:
def getPerfectNumbers(number):
    """
    Creates a list of all perfect numbers from 0 to the given number.
    """
    perfect_numbers = []
    for integer in range(2,number+1):
        the_sum = sumDivisors(integer)
        if the_sum == integer:
            perfect_numbers.append(integer)
    return perfect_numbers


# WARNING!!! Because my list of prime numbers contains only the first 1000 primes, the program will work only with numbers up to 1000!


# Let's try it with integers up to 1000!
# print(getPerfectNumbers(1000))   # Uncomment this line to try it out.


# Now I am going to write a function for an interactive program:
def interactive():
    """
    Interactive program to find perfect numbers.
    """
    while True:
        try:
            number = int(input("Enter a number (from 0 to 1000): "))
            if number < 0 or number > 1000:
                raise Exception
            the_list = getPerfectNumbers(number)
            break
        except:
            print("Please enter a positive integer smaller than or equal to 1000!")
    if len(the_list) != 0:
        print("Here is the list of your perfect numbers:", *map(lambda x: str(x)+',', the_list[:-1]), str(the_list[-1])+'.', sep=" ")
    else:
        print("There are no perfect numbers in this range!")


# Launching the program!
interactive()


