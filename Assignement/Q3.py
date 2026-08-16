import random
random.seed(int(roll_no))

numbers = []
for i in range(100):
    numbers.append(random.randint(100, 900))

print("100 random numbers:")
print(numbers)

odd_count = 0
odd_numbers = []

for x in numbers:
    if x % 2 != 0:
        odd_count = odd_count + 1
        odd_numbers.append(x)

print("ii. Number of odd numbers:", odd_count)
print("Odd numbers:", odd_numbers)

even_count = 0
even_numbers = []

for x in numbers:
    if x % 2 == 0:
        even_count = even_count + 1
        even_numbers.append(x)

print("iii. Number of even numbers:", even_count)
print("Even numbers:", even_numbers)

prime_numbers = []

for x in numbers:
    if x < 2:
        continue
    prime = True

    for i in range(2, x):
        if x % i == 0:
            prime = False
            break
    if prime:
        prime_numbers.append(x)

print("iv. Number of prime numbers:", len(prime_numbers))
print("Prime numbers:", prime_numbers)

most_common = numbers[0]
highest_count = numbers.count(numbers[0])

for x in numbers:
    count = numbers.count(x)
    if count > highest_count:
        highest_count = count
        most_common = x
print("v. Most frequent number:", most_common)
print("It occurs", highest_count, "times")
