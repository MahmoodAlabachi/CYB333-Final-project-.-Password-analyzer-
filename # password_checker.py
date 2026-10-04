while True:
    password = input("\nEnter your password: ")
    missing = []
    Score = 0

    if len(password) < 8:
        missing.append("Password must be at least 8 characters long")

    if not any(char.isupper() for char in password):
        missing.append("Password must contain at least one uppercase letter")

    if not any(char.isdigit() for char in password):
        missing.append("Password must contain at least one number")

    if not any(char.islower() for char in password):
        missing.append("Password must contain at least one lowercase letter")

    if not any(not char.isalnum() for char in password):
        missing.append("Password must contain at least one special character")


    # SCORE
    if len(password) >= 8:
        Score += 1

    if any(char.isupper() for char in password):
        Score += 1

    if any(char.islower() for char in password):
        Score += 1

    if any(not char.isalnum() for char in password):
        Score += 1

    if any(char.isdigit() for char in password):
        Score += 1


    # STRENGTH
    if Score <= 2:
        print("\nPassword Strength: Weak")

    elif Score <= 4:
        print("\nPassword Strength: Medium")

    else:
        print("\nPassword Strength: Strong")

    print("Score:", Score, "/5")


    # MISSING REQUIREMENTS
    if missing:
        print("\nYour password is missing:")

        for requirement in missing:
            print("-", requirement)

        continue

    else:
        print("\nPassword meets all requirements!")
        break
   
