# Password Checker V.1

Simple password checker written in Python. It allow you to check how strong is your password, based on several test.

## Security note
I chose to use getpass for more security and to mitigate the risk of password theft while testing.
With getpass, the password is not echoed to the terminal and is never stored in the shell command history.

## Usage
python password_checker.py

## Checks performed
With this tool you can check how strong your password is. 
It checks the password's length, if it contains upper and lower letter. It also checks if there is a number and a special character in it. And verify if the password is not in a list of common password

## Limitations (V1)
- Common password list is a small static sample (10 entries), not a real breached-password dataset
- Case-insensitive comparison against the common password list (e.g. "Password" is still flagged if "password" is in the list)