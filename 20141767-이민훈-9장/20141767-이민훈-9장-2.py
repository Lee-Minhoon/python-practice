import random

count = [0, 0, 0, 0, 0, 0]

a = (int(input("몇번 던져보실래요 ? : ")))

for i in range (0, a, 1):
    rand = random.randint(0, 5)
    count[rand] = count[rand] + 1

for i in range (0, 6, 1):
    print("주사위가 1인 경우는 %d" %(count[i]))
