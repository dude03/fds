def linear_search(A,key):
    n = len(A)
    flag = 0
    for i in range(n):
        if(A[i] == key):
            flag = 1
            break

    if(flag == 0):
        print("\n Element Not Found")
    else:
        print("\n Element Found")

def binary_search(A,l,h,key):
    if(l<=h):
        m = int((l+h)/2)
        if(A[m] == key):
            print("\n Element is present")
        elif(A[m] > key):
            binary_search(A,l,m-1,key)
        else:
            binary_search(A,m+1,h,key)

    else:
        print("\n Element not Found")


def main():
    n = int(input("Enter Number of students: "))
    A = []
    for i in range(n):
        x = int(input("Enter the array: "))
        A.append(x)

    print("\n Entered array is : ",A,end=" ")
    print("")

    key = int(input("Enter the key to be searched: "))

    print("\n \t\t\t 1. Linear Search")
    print("\n \t\t\t 2. Binary Search")
    print("\n \t\t\t 3. Exit")

    ch = int(input("\n\n Enter Your Choice: "))
    while(ch != 3):
        if(ch == 3):
            print("\n End of the program")
            break
        elif(ch == 1):
            linear_search(A,key)
            break
        elif(ch == 2):
            binary_search(A,0,n-1,key)
            break

main()
quit()



