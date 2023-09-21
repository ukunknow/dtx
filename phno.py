def is_valid_phone_number(phone_number):
    phone_number = phone_number.replace(' ', '').lstrip('+')

    if len(phone_number) != 10:
        return False

    first_digit = phone_number[0]
    if first_digit not in ['0', '7', '8', '9']:
        return False

    if not phone_number[1:].isdigit():
        return False

    if first_digit == '0':
        if phone_number[6] != ' ':
            return False

    if first_digit in ['7', '8', '9']:
        if phone_number[2] != ' ' or phone_number[7] != ' ':
            return False

    return True

n = int(input())
phone_numbers = [input().strip() for _ in range(n)]

for number in phone_numbers:
    valid = is_valid_phone_number(number)
    print(valid)
