# Password Generator

A command-line tool that generates strong, random passwords with customizable length and character types.

## Security note
## Security note
I chose to use `secrets` instead of `random`. Python's `random` module is a pseudo-random generator not designed for security purposes — it's predictable if an attacker can reconstruct its internal state. Using it could make generated passwords easier to guess or brute-force. `secrets` uses a cryptographically secure source of randomness, making it the correct choice for this kind of tool.

## Usage
python password_generator.py

## Features
You can choose:
- The length of the password (at least 10 characters recommended)
- Which character types to include: uppercase letters, lowercase letters, numbers, and special characters

## Limitations (V1)

This version does not let users control how many characters of each type (uppercase, lowercase, numbers, special characters) appear in the generated password — only whether each type is included or not.