def kkk (x,y):
    li = [False for i in range(len(x))]
    l2 = [False for i in range(len(x))]
    c = 0
    for i in  range(len(x)) :
        for i in range(len(y)) :
            if x[i] == y[i] :
                c += 1
                break
    if c == len(x):
        print ( "true")
    else :
        print ("false")
x = list (input())
y = list(input())
print (kkk(x,y))