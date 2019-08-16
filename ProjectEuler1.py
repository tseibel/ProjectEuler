count = 0
total = 0
while count <= 999:
    if count//3 == count/3:
        print(count, "three")
        total = total + count
    else:
        if count//5 == count/5:
            print(count, "five")
            total = total + count
    count = count + 1
print(total)

