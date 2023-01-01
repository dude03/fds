def inputSet(A,Str):
    n = int(input("Enter Number of students who play %s : "%Str))
    for i in range(n):
        x = input("Enter Name of Student %d who play %s : "%((i+1),Str))
        A.append(x)

    print("Input accepted Successfully")

def display(A,Str):
    n = len(A)
    if(n ==0):
        print("\n Group of students who play %s : { } "%Str)
    else:
        print("\n Group of Students who play %s : {"%Str,end = ' ')
        for i in range(n-1):
            print("%s,"%A[i],end = ' ')
        print("%s } "%A[n-1])

def search_set(A,x):
    n = len(A)
    for i in range(n):
        if(A[i] == x):
            return 1
    return 0

def find_intersection_set(A,B,C):
    n = len(A)
    for i in range(n):
        flag = search_set(B,A[i])
        if(flag == 1):
            C.append(A[i])
    
def find_union_set(A,B,C):
    for i in range(len(A)):
        C.append(A[i])
    for i in range(len(B)):
        flag = search_set(A,B[i])
        if(flag == 1):
            C.append(B[i])

def find_difference_set(A,B,C):
    n = len(A)
    for i in range(n):
        flag = search_set(B,A[i])
        if(flag == 0):
            C.append(A[i])

def main():
    Group_A = []
    Group_B = []
    Group_C = []

    while True:
        print("\n ************************ MENU *****************************")
        print("\t 1. Accept Set")
        print("\t 2. Both Cricket and Badminton")
        print("\t 3. Either Cricket or Badminton")
        print("\t 4. Neither Cricket nor Badminton")
        print("\t 5. Cricket and Football but not Badminton")
        print("\t 6. Exit")

        ch = int(input("Enter Your CHoice: "))
        Group_R = []

        if(ch == 6):
            print("End of the Program")
            break
        elif(ch == 1):
            inputSet(Group_A,"Cricket")
            inputSet(Group_B,"Badminton")
            inputSet(Group_C,"Football")
            display(Group_A,"Cricket")
            display(Group_B,"Badminton")
            display(Group_C,"Football")
        elif(ch == 2):
            display(Group_A,"Cricket")
            display(Group_B,"Badminton")
            find_intersection_set(Group_A,Group_B,Group_R)
            display(Group_R,"BOth Cricket and Badminton")
        elif(ch == 3):
            display(Group_A,"Cricket")
            display(Group_B,"Badminton")
            R1 = []
            find_union_set(Group_A,Group_B,R1)
            R2 = []
            find_intersection_set(Group_A,Group_B,R2)
            find_difference_set(R1,R2,Group_R)
            display(Group_R,"Either Cricket or Badminton")
        elif(ch == 4):
            display(Group_A,"Cricket")
            display(Group_B,"Badminton")
            display(Group_C,"Football")
            R1 = []
            find_union_set(Group_A,Group_B,R1)
            find_difference_set(Group_C,R1,Group_R)
            display(Group_R,"Niether Cricket nor Badminton")
        elif(ch == 5):
            display(Group_A,"Cricket")
            display(Group_C,"Football")
            display(Group_B,"Badminton")
            R1 = []
            find_intersection_set(Group_A,Group_C,R1)
            find_difference_set(R1,Group_B,Group_R)
            display(Group_R,"Cricket and Football")

main()
quit()