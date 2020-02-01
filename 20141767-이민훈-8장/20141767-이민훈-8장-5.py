plain_text = "Love will find a way."

encrypted_text = ""
for c in plain_text:
    x = ord(c)
    y = ord(c)
    z = ord(c)
    x = x + 1
    y = y + 1
    z = z + 1
    # 두개의 문자를 암호문에 더 추가하였습니다.
    xx = chr(x)
    yy = chr(y)
    zz = chr(z)
    encrypted_text = encrypted_text + xx + yy + zz
print("eni" + encrypted_text + "gma")
# 최종적으로 출력되는 암호문의 앞뒤에 문자를 추가하였습니다.
