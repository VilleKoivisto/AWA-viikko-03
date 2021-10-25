"""
List prime numbers to the number given by the user.
"""

def find_primes(limit):
    # make a boolean list from 0 to number + 1
    # True = number is a prime, False is not
    prime_numbers = [True for n in range(limit + 1)]

    # set starting point to list index 2 = number 2 (that's where primes start!)
    index = 2

    while limit >= index * index:
        if prime_numbers[index]:
            for num in range(index * index, limit + 1, index):
                prime_numbers[num] = False
        
        index += 1

    for num in range(2, limit + 1):
        if prime_numbers[num]:
            print(num)
    

if __name__ == "__main__":
    limiting_number = int(input("Give a number: "))

    find_primes(limiting_number)