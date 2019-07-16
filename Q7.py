'''Majority Vote'''
from collections import Counter
def major_votes():
    votes = []
    num= int(input("Number of Voters: "))
    for i in range(0,num):
        vote=input("Cast Your Vote for A,B or C Candidate: ")
        votes.append(vote)
    print(votes)
    N=len(votes)
    print("Total Number of Votes are ", N)
    votes=Counter(votes)
    for i,j in votes.items():
        if j >= (N/2):
            print("winner is ", i)
        else:
            print("None")
major_votes()

# #Function to find majority element 
# from collections import Counter 

# def majority(): 

# 	# convert array into dictionary 
# 	VotesDict = Counter(arr) 

# 	# traverse dictionary and check majority element 
# 	size = len(arr) 
# 	for (key,val) in VotesDict.items(): 
# 		if (val > (size/2)): 
# 			print(key) 
# 			return
# 	print('None') 

# # Driver program 
# if __name__ == "__main__": 
# 	arr = ['A','B','B','B','C','C','A'] 
# 	majority(arr) 
