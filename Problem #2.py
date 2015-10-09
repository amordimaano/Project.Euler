__author__ = 'amordimaano'

# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the
# even-valued terms.

def main():
    # Generate Fibonacci sequence
    fibonacci = [1,1]
    while fibonacci[-1] < 4000000 and fibonacci[-1] + fibonacci[-2] < 4000000 :
        fibonacci.append(fibonacci[-2] + fibonacci[-1])

    # Find even numbers
    even_numbers = []
    for i in fibonacci:
        if i % 2 == 0:
            even_numbers.append(i)

    #  Get sum of even numbers
    sum_even_numbers = 0
    for i in even_numbers:
        sum_even_numbers = sum_even_numbers + i

    # Answer
    print sum_even_numbers

main()