# bob.py

# Public Diffie-Hellman values
p = 23
g = 5

print("=========== BOB ===========")

# Bob's private key
private_key = 15

# Generate Bob's public key
public_key = pow(g, private_key, p)

print("Bob's Private Key :", private_key)
print("Bob's Public Key  :", public_key)

# Bob receives Darth's fake public key
darth_public_key = int(input("Enter the public key received by Bob: "))

# Generate shared secret
shared_secret = pow(darth_public_key, private_key, p)

print("Bob's Shared Secret:", shared_secret)

print("============================")




