def main():
    while True:
        try:
            card = input("Number: ")
            print(is_valid_card(card))
        except ValueError:
            print("Not a number.")
            continue
        else:
            break


# check the Luhn's algorithm
def checksum(card):
    sum = 0
    reversed = card[::-1]
    for i in reversed[1::2]:
        digits = int(i) * 2
        digits = str(digits)
        if len(digits) == 1:
            sum += int(digits)
        else:
            sum += (int(digits[0]) + int(digits[1]))
    for i in reversed[::2]:
        sum += int(i)
    if sum % 10 == 0:
        return True
    else:
        return False


# check card type if Luhn's algorithm passes
def card_type(card):
    if len(card) == 15 and (card[:2] in ["34", "37"]):
        return "AMEX"
    elif len(card) == 16 and (card[:2] in ["51", "52", "53", "54", "55"]):
        return "MASTERCARD"
    elif len(card) in [13, 16] and card[0] == "4":
        return "VISA"
    else:
        return "INVALID"


# check if card is valid and returns its type
def is_valid_card(card):
    if checksum(card):
        return card_type(card)
    else:
        return "INVALID"

main()
