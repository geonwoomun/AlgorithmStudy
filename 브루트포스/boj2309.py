dwarfs = []

for i in range(9):
    dwarfs.append(int(input()))

notDwarfHeight = sum(dwarfs) - 100

for i in range(9):
    check = True
    for j in range(i + 1, 9):
        if dwarfs[i] + dwarfs[j] == notDwarfHeight:
            dwarfs = dwarfs[:i] + dwarfs[i + 1 : j] + dwarfs[j + 1 :]
            check = False
            break
    if not check:
        break

dwarfs.sort()
for height in dwarfs:
    print(height)
