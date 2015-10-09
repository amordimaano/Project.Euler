__author__ = 'amordimaano'

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these
# multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

def main():
    # Declaring variables.
    max_number = 1000
    multiples = []
    sum_multiples = 0

    # Find multiples of 3 or 5.
    for i in range(3,max_number):
        if i % 3 == 0:
            multiples.append(i)
        else:
            if i % 5 == 0:
                multiples.append(i)

    # Get sum of multiples.
    for i in multiples:
        sum_multiples = sum_multiples + i

    # Print sum of multiples.
    print sum_multiples

main()