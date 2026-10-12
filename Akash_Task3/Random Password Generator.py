import random
import string
symbols = "#&*.!"

def generate_password():
    length = random.randint(9, 20)  
    characters = string.ascii_letters + string.digits + symbols
    password = [
        random.choice(string.ascii_letters),
        random.choice(string.digits),
        random.choice(symbols)
    ]
    password += random.choices(characters, k=length)
    random.shuffle(password)
    return ''.join(password)
print("Generated Password:", generate_password())
