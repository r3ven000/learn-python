x = int(input("enter num: "))
copy_x = int(str(x)[::-1])
if x == copy_x:
    print("num palindrom")

else:
    print("num no palindrom")
