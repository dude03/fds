
def partition(A,l,r):
    p = A[r]
    i = l - 1
    for j in range(l,r):
        if A[j] < p:
            i += 1
            A[i] , A[j] = A[j] , A[i]
    A[i+1] , A[r] = A[r] , A[i+1]
    return i+1

def quick_sort(A,l,r):
    if(l<r):
        pi = partition(A,l,r)
        quick_sort(A,l,pi-1)
        quick_sort(A,pi+1,r)

def toppers(A):
    n = len(A)
    if n >= 5:
        for i in range(n-1,n-6,-1):
            print("\n",A[i],end=" ")
    else:
        print("\n",A,end=" ")
    print("")

def main():
    n = int(input("Enter Number of Students: "))
    A = []

    for i in range(n):
        print("Enter the percentage : ")
        A.append(int(input()))

    print("\n",A,end=" ")
    print("")

    quick_sort(A,0,n-1)
    print("\n\n Sorted array is : ",A,end=" ")


    print("\n\n Top 5 Scorers : ")
    toppers(A)

main()
    