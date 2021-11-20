import re

def find_number_division(s):
    regex_division = re.compile('([0-9]*)[ ]*([0-9]+)[ ]*/[ ]*([0-9]+)')
    match = regex_division.match(s)
    if match != None:
        a, b, c = match.group(1,2,3)
        if a == '' or a == None:
            a = 0
        else:
            a = int(a)
        b, c = int(b), int(c)
        return a + (b/c)
    return None

def find_number_normal(s):
    regex_number = re.compile('\d+\.?\d*')
    match = regex_number.match(s)
    if match != None:
        return float(match.group(0))
    return None

def find_number_range(s):
    regex_division = re.compile('(\d+\.?\d*)[ ]*-[ ]*(\d+\.?\d*)')
    match = regex_division.match(s)
    if match != None:
        a, b = match.group(1,2)
        a, b = float(a), float(b)
        return (a+b)/2
    return None

def find_number_range_div(s):
    regex_division = re.compile('(?:([0-9]+) )?([0-9]+)/([0-9]+)[ ]*-[ ]*([0-9]+)[ ]*([0-9]+)/([0-9]+)')
    match = regex_division.match(s)
    if match != None:
        a,b,c,d,e,f = match.group(1,2,3,4,5,6)
        a = int(a) if (a != None) else 0
        d = int(d) if (d != None) else 0
        b, c, e, f = int(b), int(c), int(e), int(f)
        number_1 = a+(b/c)
        number_2 = d+(e/f)
        return (number_1 + number_2) / 2
    return None

def find_number_special(s):
    if s.find("½") != -1:
        return 1/2
    if s.find("¼") != -1:
        return 1/4
    if s.find("¾") != -1:
        return 3/4
    if s.find("⅓") != -1:
        return 1/3
    if s.find("⅔") != -1:
        return 2/3
    if s.find("⅕") != -1:
        return 1/5
    if s.find("⅗") != -1:
        return 3/5
    if s.find("⅘") != -1:
        return 4/5
    if s.find("⅙") != -1:
        return 1/6
    if s.find("⅚") != -1:
        return 5/6
    if s.find("⅛") != -1:
        return 1/8
    if s.find("⅜") != -1:
        return 3/8
    if s.find("⅝") != -1:
        return 5/8
    if s.find("⅞") != -1:
        return 7/8
    return None
    

def text2int(textnum):
    units = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen",
    ]

    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    scales = ["hundred", "thousand", "million", "billion", "trillion"]
    numwords = {}
    numwords["and"] = (1, 0)
    for idx, word in enumerate(units):
        numwords[word] = (1, idx)
    for idx, word in enumerate(tens):
        numwords[word] = (1, idx * 10)
    for idx, word in enumerate(scales):
        numwords[word] = (10 ** (idx * 3 or 2), 0)

    current = 0
    result = 0
    for word in textnum.replace('-', ' ').split(' '):
        if word not in numwords:
            continue

        scale, increment = numwords[word]
        current = current * scale + increment
        if scale > 100:
            result += current
            current = 0
    ret = result + current
    if ret == 0:
        return None
    return ret

def get_numbers(ingredient):
    ret = find_number_special(ingredient)
    if ret:
        return ret

    ret = find_number_range_div(ingredient)
    if ret:
        return ret

    ret = find_number_range(ingredient)
    if ret:
        return ret

    ret = find_number_division(ingredient)
    if ret:
        return ret

    ret = find_number_normal(ingredient)
    if ret:
        return ret
    
    ret = text2int(ingredient)
    if ret:
        return ret

    return None

if __name__ == "__main__":
    test_ingredients = [
        "4/3",
        "35 - 4",
        "3",
        "5 3/4",
        "3/4", 
        "3/4 - 2 4/5", 
        "3.5 - 4",
        "3.43243",
        "my three hundred eighty-five eggs",
        "⅜",
    ]
    for ingredient in test_ingredients:
        print(ingredient, get_numbers(ingredient))
