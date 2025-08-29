#for loop
for i in range(5):
    print("hello",i)
    for i in range(1,11):
        print(i)
        i = 1
        #while loop
        while i<=5:
            print("hello",i)
            i=i+1
            #break
            for j in range(6):
                if j==4:
                    break
                print(j)
                #continue
                for k in range(1,4):
                    if k==2:
                        continue
                    print(k)
