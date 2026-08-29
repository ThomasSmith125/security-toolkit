import getpass

special_characters= ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", "\\", ":", ";", "\"", "'", "<", ">", ",", ".", "?", "/"]
upper_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
lower_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
common_passwords = ["123456", "password", "123456789", "qwerty", "azerty", "letmein", "admin", "welcome", "iloveyou", "monkey"]

def check_password_strength(password):
    if password.lower() in common_passwords:
                return "WEAK PASSWORD: your password is too common"
    
    if len(password) < 8 :
        return "WEAK PASSWORD: your password must be at least 8 characters long"

    for character in password:
        if character in upper_letters:
            break
    else:
        return "WEAK PASSWORD: your password must contain at least one uppercase letter"

    for character in password:
        if character in lower_letters:
            break
    else:
        return "WEAK PASSWORD: your password must contain at least one lowercase letter"

    for character in password:
        if character in numbers:
            break
    else:
        return "WEAK PASSWORD: your password must contain at least one number"

    for character in password:
        if character in special_characters:
            break
    else:
             return "WEAK PASSWORD: your password must contain at least one special character"
    
    return "STRONG PASSWORD"


def main():
    print("Welcome to the Password Strength Checker!")
    print("Here you can check how strong is your password and learn how to upgrade it.")
    password = getpass.getpass("Enter password to check: ")
    result = check_password_strength(password)
    print(result)

if __name__ == "__main__":
    main()