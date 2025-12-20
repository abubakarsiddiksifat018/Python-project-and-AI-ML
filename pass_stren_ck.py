while True:
    password = input("Enter your password: ")

    length = len(password)
    count = 0

# ==== CHECKS WITH ERROR MESSAGES ====

    if length >= 8:
        count += 1
    else:
        print("Password must be at least 8 characters long")

    if any(char.isdigit() for char in password):
        count += 1
    else:
        print("Password must contain at least one digit")

    if any(char.isupper() for char in password):
        count += 1
    else:
        print("Password must contain at least one uppercase letter")

    if any(char.islower() for char in password):
        count += 1
    else:
        print("Password must contain at least one lowercase letter")

    if any(char in "@#$%&*!" for char in password):
        count += 1
    else:
        print("Password must contain at least one special character (@, #, $, %, &, *, !)")

# ==== FINAL RATING ====

    if count == 5:
        print("Strength: STRONG")
        break
    elif count >= 3:
        print("Strength: MODERATE")
    else:
        print("Strength: WEAK")

