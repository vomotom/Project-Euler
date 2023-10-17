import math

# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

# load numbers
with open("numbers.txt") as numbers_file:
    numbers = numbers_file.read().splitlines()

number_length = len(numbers[0])
digits = []

# make list of sums of each digit in all numbers
for i in range(number_length):
    digits.append(0)
    for number in numbers:
        digits[i] += int(number[-1 - i])

sum = 0
for i, digit in enumerate(digits):
    # if sum is ten digits or lower
    if sum < 10 ** 9:
        sum += digit * 10 ** i
    # if sum was ten digits
    else:
        sum = math.floor(sum/10)
        sum += digit * 10 ** 7
    print(sum)
