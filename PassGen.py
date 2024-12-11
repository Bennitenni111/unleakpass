import random
import string
import sys
import time
import requests
import hashlib


def generate_random_password(length=15):
    """Generates a secure random password of a given length."""
    letters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(letters) for _ in range(length))


def is_password_safe(password):
    """Checks if a password is safe using the Have I Been Pwned API."""
    sha1_hash = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix, suffix = sha1_hash[:5], sha1_hash[5:]

    try:
        response = requests.get(f'https://api.pwnedpasswords.com/range/{prefix}')
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error checking password safety: {e}")
        return False

    leaked_passwords = response.text.splitlines()
    for leaked_password in leaked_passwords:
        leaked_suffix, count = leaked_password.split(':')
        if leaked_suffix == suffix:
            print(f"Warning: This password has been found {count} times in data breaches.")
            return False

    print("Good news — no pwnage found! This password is safe.")
    return True


def loading_animation():
    """Displays a loading animation."""
    animation = [
        "[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]",
        "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"
    ]
    for frame in animation:
        time.sleep(0.2)
        sys.stdout.write("\r" + frame)
        sys.stdout.flush()
    print("\n")


def main():
    """Main function to generate or check password safety."""
    print("Welcome to the Password Safety Checker!")
    password = input('Type a password to check if it is safe, or press Enter to generate one: ')

    if password:
        print("Checking your password...")
        loading_animation()
        if not is_password_safe(password):
            print("Your password is not safe. Generating a new secure password for you...")
            loading_animation()
            safe_password = generate_random_password()
            print(f"Safe Password: {safe_password}")
    else:
        print("Generating a secure password...")
        loading_animation()
        safe_password = generate_random_password()
        print(f"Safe Password: {safe_password}")

        print("Checking the safety of the generated password...")
        loading_animation()
        is_password_safe(safe_password)


if __name__ == '__main__':
    main()
