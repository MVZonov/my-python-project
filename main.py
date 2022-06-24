def how_many_keks_in_one_drego(number_of_keks):
    print(f"You chose the {number_of_keks > 0} option!")
    if number_of_keks > 0:
        return f"{number_of_keks} Keka consists of {number_of_keks * 2} drego\nKek is great!"
    else:
        return "Kek is greater than zero! Please try again!"
users_kek_input = input("Hey Ebo, enter a number of Kek: ")
users_kek_input_number = int(users_kek_input)

calculated_value = how_many_keks_in_one_drego(users_kek_input_number)
print(calculated_value)