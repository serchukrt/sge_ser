s = input("Introduce una cadena codificada RLE: ")
rs = ""
i = 0
while i < len(s):
    char = s[i]
    i += 1
    num = ""

    while i < len(s) and s[i].isdigit():
        num += s[i]
        i += 1
    rs += char * int(num) if num else char

print(rs)

