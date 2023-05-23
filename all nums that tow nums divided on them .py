a = int(input("k "))
b = int(input("h  "))
if a > b :
    d = b
    c = a
elif a <= b :
    d = a
    c = b
count = 1
while count <= d :
    if d % count == 0 and c % count == 0  :
        print (count ) 
        count += 1 
    else :
        continue
print("hello ali")