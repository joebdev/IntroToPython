# 1. 
def multiply(a, b):
    return a * b

# 2.
def bruce_eckel_quote():
    print('Python is exectuable pseudocode.')

# 3. 
def cite(author, quote):
    print(f'{author} said: {quote}')

# 4. 
def squared_number(num):
    return num * num

# 5. 
# dividend will raise by 3 each time, divisor will raise by one each time, BUT, it won't do anything, because the function isn't invoked
def multiples_of_three():
    divisor = 1

    for dividend in range(3, 31, 3):
        print(f'{dividend} / {divisor} = 3')
        divisor += 1

multiples_of_three()

# 6.
def compare_by_length(str1, str2):
    if len(str1) < len(str2):
        return -1
    elif len(str1) > len(str2):
        return 1
    else:
        return 0
compare_by_length('patience', 'perseverance') # -1
compare_by_length('strength', 'dignity')      #  1
compare_by_length('humor', 'grace')           #  0

# 7. 
str = 'Captain Ruby'
str = str.replace('Ruby', 'Python')
print(str)

# 8. 
def greet(lang):
    match lang:
        case 'us':
            print("Hi!")
        case 'fr':
            print('Salut!')
        case 'pt':
            print('Olá!')
        case 'de':
            print('Hallo!')
        case 'sv':
            print('Hej!')
        case 'af':
            print('Haai!')
        case 'au':
            print('Howdy!')
        case 'gb':
            print('Hello!')


# 9. 
def extract_language(str):
    return str.split('_')[0]

# 10. 
def extract_region(str):
    return str.split('.')[0].split('_')[1]

# 11.
def local_greet(locale):
    language = extract_language(locale)
    region = extract_region(locale)
    match (language, region):
        case ('en', 'US'):
            return 'Hey!'
        case ('en', 'GB'):
            return 'Hello!'
        case ('en', 'AU'):
            return 'Howdy'
        case _:
            greet(language)

local_greet('fr_FR.UTF-8')
