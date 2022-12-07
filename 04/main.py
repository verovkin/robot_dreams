"""
Home Work 04
Dmytro Verovkin
robot_dreams
"""


def main():
    user_input = input("Please enter text: ")

    # check for integer
    try:
        if int(user_input) % 2 == 0:
            print("You entered EVEN number")
        else:
            print("You entered ODD number")
    except ValueError:

        # check if it's float
        try:
            if float(user_input):
                print("You entered a float number, it can't be ODD or EVEN")
        except ValueError:

            # check if it's a word
            if user_input.isalpha():
                print(f"You entered a WORD with {len(user_input)} letters")
            else:
                print("You entered something mysterious")


if __name__ == "__main__":
    main()
