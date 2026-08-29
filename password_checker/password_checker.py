import getpass

special_caracters= ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", "\\", ":", ";", "\"", "'", "<", ">", ",", ".", "?", "/"]
majuscule = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
minuscule = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
common_passwords = ["123456", "password", "123456789", "qwerty", "azerty", "letmein", "admin", "welcome", "iloveyou", "monkey"]

def check_password_strength(password):
    if password.lower() in common_passwords:
                return "WEAK PASSWORD: your password is too common"
    
    if len(password) < 8 :
        return "WEAK PASSWORD: your password must be at least 8 characters long"

    for caracter in password:
        if caracter in majuscule:
            break
    else:
        return "WEAK PASSWORD: your password must contain at least one uppercase letter"

    for caracter in password:
        if caracter in minuscule:
            break
    else:
        return "WEAK PASSWORD: your password must contain at least one lowercase letter"

    for caracter in password:
        if caracter in numbers:
            break
    else:
        return "WEAK PASSWORD: your password must contain at least one number"

    for caracter in password:
        if caracter in special_caracters:
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