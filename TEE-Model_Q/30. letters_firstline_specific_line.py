def program():
    cnt = 0
    n = int(input("Enter no. characters to read:"))
    with open("merge.txt","r") as f1:
       line1=f1.readline()
       print("The first line of file:",line1)
       nchar=f1.read(n)
       print("First n no. of characters:", nchar)
       nline=f1.readlines()
       print("Line n:",nline[n])
program()