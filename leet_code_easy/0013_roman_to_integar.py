def romanToInt(roman):
    '''
    Symbol       Value
    I             1
    V             5
    X             10
    L             50
    C             100
    D             500
    M             1000
    e.g.
    Input: "IX"
    Output: 9
    '''
    roman_dict = {'I': 1,  'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,
                    'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
    roman_int = 0
    i = 0
    while i < len(roman):
        if roman[i: i+2] in list(roman_dict):
            roman_int += roman_dict[roman[i: i+2]]
            i += 2
        elif roman [i] in list(roman_dict):
            roman_int += roman_dict[roman[i]]
            i += 1
        else:
            return None
    return roman_int

#test_a = "LVIII"
#print(romanToInt(test_a))
