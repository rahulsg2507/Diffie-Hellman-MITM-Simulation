# alice.py

# Public Diffie-Hellman values
p = 23
g = 5

print("========== ALICE ==========")

# Alice's private key
private_key = 6

# Generate Alice's public key
public_key = pow(g, private_key, p)

print("Alice's Private Key :", private_key)
print("Alice's Public Key  :", public_key)

# In the real attack, Alice will receive Darth's fake public key.
# For now, we will enter it manually.
darth_public_key = int(input("Enter the public key received by Alice: "))

# Generate shared secret
shared_secret = pow(darth_public_key, private_key, p)

print("Alice's Shared Secret:", shared_secret)

print("============================")




