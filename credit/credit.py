def main():
    # Ask user for card number
    get_card_number()


def get_card_number():
    while True:
        card = input("Number: ")

        # Ensure input is only digits
        if not card.isnumeric():
            print("Card number should only be digits.")
        else:
            validate_card(card)
            break


def checkSum(card) -> int:
    # Implements Luhn's algorithm
    total_sum = 0
    num_digits = len(card)
    is_second = False

    # Process digits from right to left
    for i in range(num_digits - 1, -1, -1):
        digit = int(card[i])
        if is_second:
            digit *= 2
            if digit > 9:
                digit -= 9
        total_sum += digit
        is_second = not is_second

    return total_sum

def validate_card(card):
    length = len(card)

    # Check if card passes Luhn's algorithm
    if checkSum(card) % 10 != 0:
        print("INVALID")
        return

    # Visa: starts with 4, length 13 or 16
    if (length == 13 or length == 16) and card[0] == "4":
        print("VISA")
        return

    # AMEX: starts with 34 or 37, length 15
    AMEX = int(card[:2])
    if length == 15 and (AMEX == 34 or AMEX == 37):
        print("AMEX")
        return

    # MasterCard: starts with 51–55, length 16
    MASTERCARD = int(card[:2])
    if length == 16 and (MASTERCARD >= 51 and MASTERCARD <= 55):
        print("MASTERCARD")
        return

    # If none match, card is invalid
    print("INVALID")

if __name__ == "__main__":
    main()