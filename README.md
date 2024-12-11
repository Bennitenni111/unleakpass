# UnleakPass: Pwned Password Generator & Checker

[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)  
[![Python version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)

UnleakPass is a Python-based tool to generate secure, non-leaked passwords or check if a given password has been compromised using the Have I Been Pwned API. It provides a robust way to ensure your passwords are safe and secure.

## Features

- **Password Generation**: Creates secure passwords with random characters.
- **Password Safety Check**: Validates if a password has been leaked or compromised using the Have I Been Pwned database.
- **Intuitive Loading Animation**: Engages users with a visual loading screen.

## How It Works

1. **Generate a Secure Password**:  
   If no password is entered, the program generates a secure 15-character password.
2. **Check Password Safety**:  
   Verifies if the password exists in any known breaches via the Have I Been Pwned API.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/Bennitenni111/unleakpass.git
   cd unleakpass
