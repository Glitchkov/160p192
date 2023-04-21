def mef(a, x1, x2, y1, y2, b):
    msg = "\"" + a + "\" -> (" + str(x1) + ";" + str(x2) + ") -> (" + str(y1) + ";" + str(y2) + ") -> \"" + b + "\""
    return msg

def code(a):
    x1 = list.index(a[0])
    x2 = list.index(a[1])
    y1 = (11*x1+3*x2)%26
    y2 = (7*x1+4*x2)%26
    b = list[y1] + list[y2]
    msg = mef(a, x1, x2, y1, y2, b)
    print(msg)

def decode(b):
    y1 = list.index(b[0])
    y2 = list.index(b[1])
    x1 = (16*y1+y2)%26
    x2 = (11*y1+5*y2)%26
    a = list[x1] + list[x2]
    msg = mef(b, y1, y2, x1, x2, a)
    print(msg)

input = input("Entrer les deux caractères à coder, précédés de % pour coder ou de $ pour décoder : ")
list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
input = input.upper()
if len(input) == 3 and input[1] in list and input[2] in list :
    if input[0] == "%":
        input = input[1:]
        code(input)
    elif input[0] == "$":
        input = input[1:]
        decode(input)