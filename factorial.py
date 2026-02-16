num=int(input("enter a number"))
fact=1

if num<0:
    print("negative number-No factorial")
else:
    for i in range(1,num+1):
        fact=fact*i

    print(fact)