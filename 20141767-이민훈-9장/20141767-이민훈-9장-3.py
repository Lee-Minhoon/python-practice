tell = {}
while True:
    name = input("(입력모드)이름을 입력하시오: ")
    if not name:
        name2 = input("(검색모드)이름을 입력하시오: ")
        print(tell[name2])
    else:
        tel = input("전화번호를 입력하시오: ")
        tell[name] = tel
