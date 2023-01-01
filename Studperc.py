p = []
n = int(input("Enter the Number of Students: "))

for i in range(n):
    perc = int(input("Enter the percentages of students: "))
    p.append(perc)

print("Percentages scored by Student: ",p)

def average():
    sum = 0
    count = 0
    for i in p:
        if i>0:
            sum = sum + i
            count = count + 1

    avg = sum / count
    print("Average Percentage scored by Student: ",avg)

def highest_score():
    hm = 0
    for i in p:
        if i>hm:
            hm = i
        else:
            hm = hm

    print("Highest percentage scored: ",hm)

def lowest_score():
    lm = max(p)
    for i in p:
        if i>0 and i<lm:
            lm = i

    print("Lowest Percentage scored: ",lm)

def absent_stud():
    ab = 0
    for i in p:
        if i<0:
            ab = ab + 1

    print("Number of Absent Students: ",ab)

def frequency():
    global p
    f = []
    for i in range(101):
        f.append(0)

    for i in p:
        if i>0:
            f[i]=f[i] + 1

    print("Highest Frequency",f.index(max(f)))

def main():
    average()
    highest_score()
    lowest_score()
    absent_stud()
    frequency()

main()


