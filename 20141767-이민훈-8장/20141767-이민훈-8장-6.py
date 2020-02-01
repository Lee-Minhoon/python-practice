encrypted_text = "eniMMMpppwwwfff!!!xxxjjjmmmmmm!!!gggjjjoooeee!!!bbb!!!xxxbbbzzz///gma"
a = len(encrypted_text)
b = ""

for i in range(3, a-4, 1):
    b = b + encrypted_text[i]
# 반복문을 이용해 최종적으로 추가한 문자를 먼저 지우고 새로운 변수 b에 저장합니다.

plain_text = ""
for c in b:
    x = ord(c)
    y = ord(c)
    z = ord(c)
    x = x - 1
    y = y - 1
    z = z - 1
    xx = chr(x)
    yy = chr(y)
    zz = chr(z)
    plain_text = plain_text + xx + yy + zz

a = len(plain_text)
b = ""

for i in range(0, a-1, 1):
    if i % 9 + 1 == 1:
        b = b + plain_text[i]
# 암호화와 복호화가 너무 어려워 제대로된 이해를 전혀 하지 못했습니다..
# 다만 이렇게 b를 출력할시에 같은문자가 9번씩 반복되기에 위와같이
# 반복문을 이용해 1번째 칸으로부터 9칸뒤에있는 문자들을 차례로 더해 나머지를 소거하였습니다.
print(b)
