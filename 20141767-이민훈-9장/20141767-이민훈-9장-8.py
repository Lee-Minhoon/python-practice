problem = {}
problem["최근에 가장 떠오르는 프로그래밍 언어"] = "파이썬"
problem["데이터를 저장하는 메모리 공간"] = "변수"
problem["작업을 수행하는 문장들의 집합에 이름을 붙인것"] = "함수"
problem["서로 관련이 없는 항목들의 모임"] = "리스트"
point = 0

for a in problem.keys():
    inter = 1
    print(a)
    for b in problem.values():
        print("(%d)"%(inter), end="")
        print(b, end=" ")
        inter += 1
    answer = str(input("\n답을 입력하시오: "))
    if answer == problem[a]:
        print("정답입니다!\n")
        point += 1
    else:
        print("오답입니다!\n")

print("당신의 점수는 %d점 입니다."%(point))
