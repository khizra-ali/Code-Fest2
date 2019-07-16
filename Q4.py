lst =[]

N=int(input("Total contestants: "))
for i in range(0,N):
    score=input("Enter score of all the contestants: ")
    lst.append(score)
print(lst)
lst.sort()
print(lst)
winner = max(lst)
print("Winner score: ", winner)
runner_up= print("Runner Up score is:", lst[len(lst)-2])