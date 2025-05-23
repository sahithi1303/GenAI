import random

# Generate a single random number between 1 and 100
random_number = random.randint(1, 100)
print(f"Random number: {random_number}")

# Generate 10 random numbers between 1 and 100
print("\nGenerating 10 random numbers between 1 and 100:")
for i in range(10):
    number = random.randint(1, 100)
    print(f"Number {i+1}: {number}")

# If you want to generate a list of random numbers
random_numbers = [random.randint(1, 100) for _ in range(5)]
print("\nList of 5 random numbers:", random_numbers)
