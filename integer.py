def roman_to_int(s):
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    total = 0
    prev_value = 0
    
    for symbol in s[::-1]:
        value = roman_values[symbol]
        
        if value < prev_value:
            total -= value
        else:
            total += value
        
        prev_value = value
    
    return total

s1 = "III"
print(roman_to_int(s1))  

s2 = "LVIII"
print(roman_to_int(s2))  

s3 = "MCMXCIV"
print(roman_to_int(s3)) 
