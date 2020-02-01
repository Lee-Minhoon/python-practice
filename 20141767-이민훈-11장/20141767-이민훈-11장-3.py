char = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
num = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
filename = input("파일 이름을 입력하시오 : ")
t = open(filename, "r+")
for line in t:
    for ch in line:
        for i in range(0, 26, 1):
            if char[i] == ch:
                num[i] = num[i] + 1

for i in range(0, 26, 1):
    print(char[i] + ":" + str(num[i]))
                
t.close()
