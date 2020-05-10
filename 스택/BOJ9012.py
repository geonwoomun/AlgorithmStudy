N = int(input())

while N > 0:
    par = list(input())
    stack = []
    check = True
    for data in par:
        if data == "(":
            stack.append(data)
        else:
            if len(stack) != 0:
                stack.pop()
            else:
                check = False
                break
    if(check and len(stack) == 0):
        print("YES")
    else:
        print("NO")

    N -= 1