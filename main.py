from random import randrange;

def generate_password(password_length, use_symbols):
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890";
    symbols = "!@#$%&";

    characters_being_used = ""

    if("y" in use_symbols.lower()):
        characters_being_used = characters + symbols;
    else:
        characters_being_used = characters;

    password = '';

    for i in range(password_length):
        randomNumber = randrange(0, len(characters_being_used), 1);
        password += characters_being_used[randomNumber];

    return password;

password_length = input("Choose the length for your password (numbers only): ")

use_symbols = str(input("Do you want to include symbols like ! or @ in your password (y/n)? "));

newPassword = generate_password(password_length, use_symbols);

print(f"Your new password is: {newPassword}");
