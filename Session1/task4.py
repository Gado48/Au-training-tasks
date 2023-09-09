def is_valid_credit_card(number):
    reversed_number = number[::-1]
    total = 0

    for i in range(len(reversed_number)):
        digit = int(reversed_number[i])
        if i % 2 == 1:
            digit *= 2
            if digit > 9:
                digit -= 9
        total += digit

    return total % 10 == 0


def determine_card_type(number):
    if number.startswith("34") or number.startswith("37"):
        return "American Express"
    elif (
        number.startswith("51")
        or number.startswith("52")
        or number.startswith("53")
        or number.startswith("54")
        or number.startswith("55")
    ):
        return "MasterCard"
    elif number.startswith("4"):
        return "Visa"
    else:
        return "Unknown"


def main():
    try:
        credit_card_number = input("Enter a credit card number: ")
        credit_card_number = credit_card_number.replace(" ", "")  # Remove any spaces

        if not credit_card_number.isdigit():
            print("Invalid input. Please enter a numeric credit card number.")
            return

        if is_valid_credit_card(credit_card_number):
            card_type = determine_card_type(credit_card_number)
            if card_type != "Unknown":
                print(f"Valid {card_type} card")
            else:
                print("Valid credit card (unknown type)")
        else:
            print("Invalid credit card")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
