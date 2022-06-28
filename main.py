def how_many_drego_in_one_kek(number_of_keks):
    print(f"You chose the {number_of_keks > 0} option!")
    if number_of_keks > 0:
        return f"{number_of_keks} Keka consists of {number_of_keks * 2} drego\nKek is great!"
    elif number_of_keks == 0:
        return "Kek is greater than zero! Please try again!"
    else:
        return "Kek can't be a negative! Please try again!"

def validate_and_execute():
    if users_kek_input.isdigit():
        users_kek_input_number = int(users_kek_input)
        calculated_value = how_many_drego_in_one_kek(users_kek_input_number)
        print(calculated_value)
    else:
        print("Your input is not a number! Please don't try to ruin Kek's program!")

users_kek_input = input("Hey Ebo, enter a number of Kek: ")
validate_and_execute()

