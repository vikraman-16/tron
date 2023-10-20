import random

p = 23  # A prime number
g = 5   # A primitive root modulo p

a_private = random.randint(1, p - 1)
A = (g ** a_private) % p

b_private = random.randint(1, p - 1)
B = (g ** b_private) % p

shared_secret_A = (B ** a_private) % p
shared_secret_B = (A ** b_private) % p


print("Shared Secret (Alice):", shared_secret_A)
print("Shared Secret (Bob):", shared_secret_B)

