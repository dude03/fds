def input_m(A):
    n = int(input("\n Enter the number of students: "))
    for i in range(n):
        marks = []
        print("\n Enter the percentage scored by student: ")
        marks = float(input())
        A.append(marks)
    print("\n Marks Accepted Successfully")

def display(A):
    print("")
    n = len(A)
    if(n == 0):
        print("Percentages scored by student : { }")
    else:
        print("\n Marks Scored : ")
        print(A,end = " ")
    print("")

def Selection_Sort(A):
    n = len(A)
    for i in range(n):
        min = i
        for j in range(i+1,n):
            if(A[j]<A[min]):
                min = j

        temp = A[i]
        A[i] = A[min]
        A[min] = temp

    print("\n Sorted array using Selection Sort: ",A,end=" ")
    print("")

def Bubble_Sort(A):
    n = len(A)
    i = 0
    for i in range(n-1):
        for j in range(0,n-i-1):
            if(A[j]>A[j+1]):
                temp = A[j]
                A[j] = A[j+1]
                A[j+1] = temp

    print("\n Sorted array using Bubble Sort: ",A,end=" ")
    print("")

def Insertion_Sort(A):
    n = len(A)
    for i in range(1,n):
        element = A[i]
        j = i - 1
        while(j>=0):
            if(A[j]<=element):
                break
            else:
                A[j+1] = A[j]
                j = j - 1
        A[j+1] = element
    print("\n",A,end=" ")
    print("")

def Shell_Sort(A):
    n = len(A)
    gap = n // 2
    while gap>0:
        for i in range(gap,n):
            temp = A[i]
            j = i
            while j>=0 and A[j-gap] > temp:
                A[j] = A[j-gap]
                j = j - gap
            A[j] = temp
        gap = gap // 2
    
    print("\n",A,end=" ")
    print("")
        
def main():
    A = []

    while True:
        print("\n ************************ MENU ****************************")
        print("\n \t\t\t 1. Accept Marks")
        print("\n \t\t\t 2. Display Marks")
        print("\n \t\t\t 3. Sort using Selection Sort")
        print("\n \t\t\t 4. Sort using Bubble Sort")
        print("\n \t\t\t 5. Sort using Insertion Sort")
        print("\n \t\t\t 6. Sort using Shell Sort")
        print("\n \t\t\t 8. Exit")

        ch = int(input("\n Enter your Choice: "))

        if(ch == 8):
            print("\n End of Program")
            break
        elif(ch == 1):
            input_m(A)
        elif(ch == 2):
            display(A)
        elif(ch == 3):
            Selection_Sort(A)
        elif(ch == 4):
            Bubble_Sort(A)
        elif(ch == 5):
            Insertion_Sort(A)
        elif(ch == 6):
            Shell_Sort(A)
main()
quit()
    
