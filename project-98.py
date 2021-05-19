def swap():
    f1 = input("Enter first file location to swap: ")
    f2 = input("Enter second file location to swap: ")
    with open(f1,"r") as a:
        data_a=a.read()

    with open(f2,"r") as b:
        data_b = b.read()

    with open(f1,"w") as a:
        a.write(data_b)

    with open(f2,"w") as b:
        b.write(data_a)
            
swap()