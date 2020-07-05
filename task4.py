#!/usr/bin/python3
def check_cred_card(credit_card_number):
    counter = 0

    if (len(credit_card_number) != 16 and
        len(credit_card_number) != 19):
        return False

    if (credit_card_number[0] != '4' and
        credit_card_number[0] != '5' and
        credit_card_number[0] != '6'):
        return False
    
    for index, value in enumerate(credit_card_number):

        if value.isdigit():
            if (int(value) > 9 and
                int(value) < 0):
                return False
        elif value != '-':
            return False
        elif index%5 != 4:
            return False
        
        if index == 0:
            counter += 1
        elif value == credit_card_number[index-1]:
            counter += 1
            if counter == 4:
                return False
        else:
            counter = 0
    
    return True