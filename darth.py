# darth.py
# Public Diffie-Hellman values
p = 23
g = 5

print("========== DARTH ==========")

# Darth creates TWO private keys
private_key_alice = 7
private_key_bob = 10

# Generate two different public keys
public_key_alice = pow(g, private_key_alice, p)
public_key_bob = pow(g, private_key_bob, p)

print("Darth's Private Key for Alice :", private_key_alice)
print("Darth's Public Key for Alice  :", public_key_alice)
print()
print("Darth's Private Key for Bob   :", private_key_bob)
print("Darth's Public Key for Bob    :", public_key_bob)

# Alice's real public key
alice_public_key = int(input("\nEnter Alice's REAL public key: "))

# Bob's real public key
bob_public_key = int(input("Enter Bob's REAL public key: "))

# Shared secret with Alice
secret_with_alice = pow(alice_public_key, private_key_alice, p)

# Shared secret with Bob
secret_with_bob = pow(bob_public_key, private_key_bob, p)

print()
print("Secret shared with Alice:", secret_with_alice)
print("Secret shared with Bob  :", secret_with_bob)
print("============================")





