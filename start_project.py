import math
import random

# Generate a random password
def generate_password(length):
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+"
    password = "".join(random.choice(characters) for p in range(length))
    return password 

def main(): 

    # Create an f-string with variables
    name = "Jingyuan Dai"
    print(f"My name is {name} and this is my second Python practice script.")

    # Calculate the square root
    number = 16
    square_root = math.sqrt(number)
    print(f"The square root of {number} is {square_root}")

    # A list of numbers and calculate the squared numbers
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    squared_numbers = [x**2 for x in numbers]
    print("Original Numbers:", numbers)
    print("Squared Numbers:", squared_numbers)

    generated_password = generate_password(6)
    print(f"Generated Password: {generated_password}")

if __name__ == "__main__":
    main()