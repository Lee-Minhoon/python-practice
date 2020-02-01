count = 0
filename = input("파일 이름을 입력하시오 : ")
infile = open(filename, "r")
for line in infile:
   count += len(line.rstrip())


print("파일 안에는 총 %d 개의 글자가 있습니다." %(count))
    
