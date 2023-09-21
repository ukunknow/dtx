def int_to_roman(num):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syms = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    result = ""
    
    i = 0
    while num > 0:
        if num >= val[i]:
            result += syms[i]
            num -= val[i]
        else:
            i += 1
    
    return result

