a = input()
b = 'a'
while(ord(b) <= ord(a)):
    print(b, end=" ")
    b = chr(ord(b)+1)

