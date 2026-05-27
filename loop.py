# pattern printing using nested loops
outer_loop = int(input("Enter the number of iterations for the outer loop:" ))

for i in range (outer_loop):
    for j in range (i+1):
        print("*",end="")
    print()    