
import secrets
import sys

special_characters= ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", "\\", ":", ";", "\"", "'", "<", ">", ",", ".", "?", "/"]
upper_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
lower_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


def password_generator(length,include_uppercase, include_lowercase, include_numbers, include_special_chars):

    password = ""
    character_pool = []
    
    if include_uppercase:
        character_pool.extend(upper_letters)
    if include_lowercase:
        character_pool.extend(lower_letters)
    if include_numbers:
        character_pool.extend(numbers)
    if include_special_chars:
        character_pool.extend(special_characters)

    if not character_pool:
        raise ValueError("No character types selected. Please select at least one.")

    for i in range(length):
        password += secrets.choice(character_pool)

    return password

def main():
    print("Welcome to the Password Generator!")
    length = int(input("Enter the desired length of the password, at least 10 for a stronger password: "))
    if length < 10:
        print("Warning: A password shorter than 10 characters is considered weak.")
    include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    include_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    include_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    include_special_chars = input("Include special characters? (y/n): ").lower() == 'y'

    try :
        password = password_generator(length,include_uppercase, include_lowercase, include_numbers, include_special_chars)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

    print(f"Generated password: {password}")

if __name__ == "__main__": 
    main()