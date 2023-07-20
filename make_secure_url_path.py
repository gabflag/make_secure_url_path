import string
import random
import time

def generate_random_url(length=50, depth=5):
    characters = string.ascii_letters + string.digits
    random_url = '/'.join(''.join(random.choice(characters) for _ in range(length)) for _ in range(depth))
    return random_url

# Exemplo de uso
url = generate_random_url()
print("URL aleatória gerada:", url)
time.sleep(20)
