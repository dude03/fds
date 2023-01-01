def main():
    r1 = int(input("Enter number of rows of first matrix: "))
    c1 = int(input("Enter number of columns of first matrix: "))
    r2 = int(input("Enter number of rows of second matrix: "))
    c2 = int(input("Enter number of columns of second matrix: "))

    mat1=[]
    mat2=[]
    matt1=[]
    matt2=[]

    read(r1,c1,mat1)
    display(r1,c1,mat1)

    read(r2,c2,mat2)
    display(r2,c2,mat2)

    addition(r1,c1,mat1,r2,c2,mat2)
    subtraction(r1,c1,mat1,r2,c2,mat2)
    transpose(r1,c1,mat1,matt1,r2,c2,mat2,matt2)
    multiplication(r1,c1,mat1,r2,c2,mat2)


def read(r1,c1,mat1):
    print("")
    for i in range(r1):
        a = []
        for j in range(c1):
            a.append(int(input("Enter elements of matrix: ")))

        mat1.append(a)

def display(r1,c1,mat1):
    print("")
    for i in range(r1):
        for j in range(c1):
            print(mat1[i][j],end = " ")

        print("")

def addition(r1,c1,mat1,r2,c2,mat2):
    if r1 != r2 and c1 != c2:
        print("Addition is not possible")
    else:
        print("")
        print("Addition matrix: ")
        for i in range(r1):
            for j in range(c1):
                print(mat1[i][j] + mat2[i][j],end = " ")
        print("")

def subtraction(r1,c1,mat1,r2,c2,mat2):
    if r1 != r2 and c1 != c2:
        print("Subtraction is not possible")
    else:
        print("")
        print("Subtraction matrix: ")
        for i in range(r1):
            for j in range(c1):
                print(mat1[i][j] - mat2[i][j],end = " ")
        print("")

def transpose(r1,c1,mat1,matt1,r2,c2,mat2,matt2):
    print("")
    print("Transpose of first matrix : ")
    for i in range(r1):
        for j in range(c1):
            matt1.append(mat1[j][i])

    print(matt1,end= " ")
    print("")

    print("")
    print("Transpose of second matrix : ")
    for i in range(r2):
        for j in range(c2):
            matt2.append(mat2[j][i])

    print(matt2,end= " ")
    print("")

def multiplication(r1,c1,mat1,r2,c2,mat2):
    res = []

    for i in range(r1):
        a = []
        for j in range(c1):
            a.append(0)

        res.append(a)

    if r1 == c2:
        print("")
        print("Multiplication of matrix is: ")
        for i in range(r1):
            for j in range(c2):
                for k in range(c1):
                    res[i][j] = res[i][j] + mat1[i][k] * mat2[k][j]
        display(r1,c1,res)

    else:
        print("Multiplication is not possible")               

main()
    






