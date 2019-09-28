a = input()
for idx, value in enumerate(list(a)):
    if(idx == 0) :
        print('[{0:<05d}]'.format(int(value)))
    elif(idx == 1) :
        print('[{0:<04d}]'.format(int(value)))
    elif(idx == 2) :
        print('[{0:<03d}]'.format(int(value)))   
    elif(idx == 3) :
        print('[{0:<02d}]'.format(int(value)))
    elif(idx == 4) :
        print('[{0:<01d}]'.format(int(value))) 