# Diffie–Hellman Man-in-the-Middle (MITM) Attack Simulation

## 1. Project Overview

This project demonstrates a simulated Man-in-the-Middle (MITM) attack against the basic Diffie–Hellman key exchange protocol using Python.

The simulation consists of three programs:

- **Alice (`alice.py`): Represents the sender.
- **Bob (`bob.py`): Represents the receiver.
- **Darth (`darth.py`): Represents the attacker who establishes separate shared secrets with Alice and Bob.

The objective is to demonstrate how an attacker can manipulate an unauthenticated public-key exchange and establish separate shared secrets with two communicating parties.

## 2. Technologies Used

- Python 3
- Visual Studio Code (VS Code)
- Git and GitHub
- Diffie–Hellman key exchange
- Modular exponentiation

## 3. Project Structure

```
MITM-Simulation/
├── alice.py
├── bob.py
├── darth.py
└── README.md

```

## 4. Prerequisites

Before running the simulation, ensure that Python 3 is installed.

Check the installation by opening a terminal and executing:

```
python3 --version

```

If Python is installed, the command displays the installed version.

Open the project folder in VS Code and select **Terminal → New Terminal**.

No additional Python packages are required for these programs.

## 5. Public Parameters and Keys

The programs use the following Diffie–Hellman parameters:

| Parameter | Value |
|---|---:|
| Prime modulus (p) | 23 |
| Generator (g) | 5 |
| Alice's private key | 6 |
| Bob's private key | 15 |
| Darth's private key for Alice | 7 |
| Darth's private key for Bob | 10 |

The programs calculate public keys using modular exponentiation.

## 6. How to Run the Simulation

Run each program separately in the VS Code terminal. The programs communicate through manually entered values; they do not exchange keys automatically over a network.

### Step 1: Run Darth's Program

Execute:

```
python3 darth.py

```

When prompted, enter the real public keys calculated by Alice and Bob:

```
Enter Alice's REAL public key: 8
Enter Bob's REAL public key: 19

```

The program calculates two shared secrets:

- Secret shared with Alice: 12
- Secret shared with Bob: 6

Darth's public keys are 17 for Alice and 9 for Bob.

### Step 2: Run Alice's Program

Execute:

```
python3 alice.py

```

When prompted for the public key received by Alice, enter Darth's public key for Alice:

```
Enter the public key received by Alice: 17

```

Alice calculates the shared secret:

```
Alice's Shared Secret: 12

```

### Step 3: Run Bob's Program

Execute:

```
python3 bob.py

```

When prompted for the public key received by Bob, enter Darth's public key for Bob:

```
Enter the public key received by Bob: 9

```

Bob calculates the shared secret:

```
Bob's Shared Secret: 6

```

## 7. Expected Results

The simulation produces the following results:

| Participant | Public key | Received key | Shared secret |
|---|---:|---:|---:|
| Alice | 8 | 17 | 12 |
| Darth, Alice's side | 17 | Alice's real key: 8 | 12 |
| Darth, Bob's side | 9 | Bob's real key: 19 | 6 |
| Bob | 19 | 9 | 6 |

The results show that Alice and Darth independently calculate the shared secret 12, while Bob and Darth independently calculate the shared secret 6.

The two shared secrets are different. This demonstrates how an attacker can establish separate key relationships with Alice and Bob when public keys are not authenticated.

## 8. Important Note About the Simulation

This project demonstrates the key-exchange stage of a MITM attack through manual public-key substitution.

The current programs do not perform live network interception or implement message encryption, decryption, modification, or re-encryption. The simulation is intended for educational purposes and illustrates why authentication is important in secure key exchange.

## 9. Author and Repository

**Project:** Diffie–Hellman Man-in-the-Middle Attack Simulation

**Repository:** Add the URL of your GitHub repository here.
