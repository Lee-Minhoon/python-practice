def intplus(a):
    b = []
    for i in range(0, a, 1):
        c = float(input("정수를 입력하시오 : "))
        b.append(c)
    return b

def ave(a, b):
    c = 0
    for i in range(0, b, 1):
        c = c + a[i]
    c = c / b
    return c

#=======================================================

enterint = int(input("몇개의 정수를 입력하실래요? : "))

ints = intplus(enterint)
ints2 = len(ints)
answer = (ave(ints, ints2))

print("%.2f" %(answer))
