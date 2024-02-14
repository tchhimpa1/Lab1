def calculate_age():
    try:
        birth_year = int(input("Enter your birth year: "))
        current_year = 2024  
        age = current_year - birth_year

        if age >= 0:
            print(f"You are {age} years old.")
        else:
            print("Invalid birth year. Please enter a valid year.")
    except ValueError:
        print("Invalid input. Please enter a valid year.")

calculate_age()
