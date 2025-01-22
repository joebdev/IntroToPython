# 1.
starwars = "These aren't the droids you're looking for."
len(starwars)

# 2. 
caps_str = 'confetti floating everywhere'
caps_str.upper()

# 3. 
name = 'Roger'

name.casefold() == 'RoGeR'.casefold()
name.casefold() == 'DAVE'.casefold()

# 4. 
rhyme = """A pirate I was meant to be!
Trim the sails and roam the sea!
"""

# 5.
char_sequence = 'TXkgaG92ZXJjcmFmdCBpcyBmdWxsIG9mIGVlbHMu'
print('x' in char_sequence)

# 6. 
def is_empty(str):
    if len(str) == 0:
        print(True)
    else:
        print(False)

is_empty('mars') # False
is_empty('  ') # False
is_empty('') # True

# 7. 
def is_empty_or_blank(str):
    if len(str) == 0 or ' ' in str:
        print(True)
    else:
        print(False)

is_empty_or_blank('mars') # False
is_empty_or_blank('  ') # False
is_empty_or_blank('') # True

# 8. 
launch_str = 'launch school tech & talk'
launch_str.title()

# 9. 
def starts_with(str, pre):
    get_str_start = str[0: len(pre)]
    if get_str_start == pre:
        return True
    
    return False

print(starts_with('launch', 'la'))
print(starts_with("school", "sah"))

# 10. 
def count_substrings(str, str2):
    return str.count(str2)

print(count_substrings('lemon lemon lemon', 'lemon'))