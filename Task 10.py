user_str_1 = input("Input String 1: ")
user_str_2 = input("Input String 2: ")
s1 = set(user_str_1)
s2 = set(user_str_2)
lst  = list(s1 & s2)
print(" Common letters: {}" .format(lst))

