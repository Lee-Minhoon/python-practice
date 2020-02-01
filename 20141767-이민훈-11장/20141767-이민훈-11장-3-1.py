import random

char = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "\n"]

t = open("3.txt", "w")
s = ""
for i in range(0, 500000, 1):
    r = random.randint(0, 26)
    s = s + char[r]
t.write(s)      
t.close()
