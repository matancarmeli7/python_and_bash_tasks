#!/usr/bin/python3
import re
# Check if there is  4 or more consecutive repeated digits in the credit card
def check_if_there_is_4_consecutive_repeated_digits(credit_card):
    counter = 0
    for index, value in list(enumerate(credit_card[:-1])):
        
        if value == credit_card[index+1]:
            counter += 1
            if counter == 4:
                print(credit_card)
                return False
        else:
            counter = 0
    return True

# Get list of credit cards and checks if all of them are valide
def check_cred_card(credit_cards):

    for credit_card in credit_cards:

        if re.match(r'[4-6][0-9]{15}$', credit_card):
            if not check_if_there_is_4_consecutive_repeated_digits(credit_card):
                return False
        elif re.match(r'[4-6][0-9]{3}\-[0-9]{4}\-[0-9]{4}\-[0-9]{4}$', credit_card):
            if not check_if_there_is_4_consecutive_repeated_digits(credit_card):
                return False
        else:
            return False
    return True