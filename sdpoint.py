def input_m(M):
    print("\n Enter the order of matrix(row, col)")
    r = int(input("\t\t Enter Number of rows: "))
    c = int(input("\t\t Enter Number of Columns: "))
    for i in range(r):
        A = []
        for j in range(c):
            e = int(input("enter elements: "))
            A.append(e)
        M.append(A)
    print("\n Matrix accepted succesfully")

def display(M,r,c):
    print("Enter Matrix of order (%d,%d) is : "%(r,c))
    for i in range(r):
        print("\t\t ",end = " ")
        for j in range(c):
            print(M[i][j],end = " ")
        print("")

def find_saddle_point(M,r,c):
    count = 0
    for i in range(r):
        min = M[i][0]
        ci = 0
        for j in range(1,c):
            if min > M[i][j]:
                min = M[i][j]
                ci = j

        flag = 1
        for ri in range(r):
            if (min<M[ri][ci]):
                flag = 0
                break

        if(flag == 1):
            count += 1
            print("\n %d is saddle point in row(%d) and column(%d)"%(min,i+1,ci+1))

    if(count == 0):
        print("\n No saddle point")
    else:
        print("\n %d saddle point found"%count)

def main():
    while True:
        print("\t\t\t 1. Input Matrix")
        print("\t\t\t 2. Display Matrix")
        print("\t\t\t 3. Find Saddle Point")
        print("\t\t\t 4. Exit")

        ch = int(input("\n Enter Your Choice: "))
        if(ch == 4):
            print("\n End of Program")
            break
        elif(ch == 1):
            Mat = []
            input_m(Mat)
            r = len(Mat)
            c = len(Mat[0])
        elif(ch == 2):
            display(Mat,r,c)
        elif(ch == 3):
            display(Mat,r,c)
            find_saddle_point(Mat,r,c)

main()
quit()