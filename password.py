import random
s = int(input("choose the length of your password"))
p = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWYXZ123456789@*#%&^£$?"
jn = "".join(random.sample(p, s))
print(jn)