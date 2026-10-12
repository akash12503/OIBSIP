# Random Password Generator in Python

## Project Description

The Random Password Generator is a simple Python program that automatically generates random passwords using uppercase letters, lowercase letters, numbers, and special symbols.

The program does not ask the user to select characters or enter a password length. It automatically generates a password with a random length between 9 and 20 characters.

## Features

- Generates random passwords automatically.
- Includes uppercase and lowercase letters.
- Includes numbers (0–9).
- Includes special symbols and punctuation.
- Randomly selects a password length between 9 and 20 characters.
- Ensures at least one letter, one number, and one symbol in every generated password.
- Requires no user input.
- Uses Python's built-in modules.

## Technologies Used

- Python 3
- random module
- string module
  
## Requirements

- Python 3.x
- No external libraries required.

## How to Run

1. Install Python 3 on your computer.
2. Clone or download this repository.
3. Open a terminal or command prompt in the project folder.
4. Run the following command:

```bash
python password_generator.py
```

Depending on your system, you may need to use:

```bash
python3 password_generator.py
```

## Example Output

```text
Generated Password: gT7@pL2#vQ9!x
```

Note: The password will be different each time the program runs.

## How It Works

1. Randomly selects a password length between 9 and 20 characters.
2. Combines uppercase letters, lowercase letters, numbers, and symbols.
3. Ensures at least one letter, one number, and one symbol are included.
4. Randomly selects the remaining characters.
5. Shuffles the characters to randomize their positions.
6. Displays the generated password.
