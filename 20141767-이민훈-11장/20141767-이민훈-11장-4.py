import pickle

a1 = 12
a2 = 3.14
a3 = []

for i in range(1, 6, 1):
    a3.append(i)

b = open("4.dat", "wb")

pickle.dump(a1, b)
pickle.dump(a2, b)
pickle.dump(a3, b)

b.close()
b = open("4.dat", "rb")

while True:
    try:
        c = pickle.load(b)
        print(c)
    except EOFError:
        break

b.close()
