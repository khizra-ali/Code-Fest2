'''QUESTION NO 2 :
The Farm Problem
You've got chickens (2 legs), cows (4 legs) and pigs (4 legs) on your farm. Return the total
number of legs on your farm.
Examples :
1) animals(2, 3, 5) ➞ 36
 2) animals(1, 2, 3) ➞ 22
 3) animals(5, 2, 8) ➞ 50'''

chicken=int(input("Enter number of chickens: "))
legs1 = chicken*int(2)
print(legs1)
cows=int(input("Enter number of cows: "))
legs2 = cows*int(4)
print(legs2)
pigs=int(input("Enter number of pigs: "))
legs3 = pigs*int(4)
print(legs3)
total_legs=legs1+legs2+legs3
legs= print("Total number of legs: ", total_legs)