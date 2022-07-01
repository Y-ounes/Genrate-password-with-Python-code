import random
##choose the length of your password
s = int(input("choose the length of your password"))
##string of numbers, uppercase, lowercase and characters
p = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWYXZ123456789@*#%&^£$?"
jn = "".join(random.sample(p, s))
print(jn)