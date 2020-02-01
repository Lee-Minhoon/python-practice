import pickle

sum1 = 0
cnt1 = 0

a = open("5-1.txt", "r")

for line in a:
    sum1 += float(line.rstrip())
    cnt1 += 1

a.close()

avg1 = sum1 / cnt1

b = open("5-2.txt", "w")

b.write("합계 : " + str(sum1) + "\n" + "평균 : " + str(avg1))

b.close()
