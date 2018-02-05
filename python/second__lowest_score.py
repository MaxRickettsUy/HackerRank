#insertion sort students based on their score in increasing order
def sortScores(students):
	for j in range(1,len(students)):
    		key = students[j]
		i = j - 1
		while i >= 0 and students[i][1] > key[1]:
			students[i+1] = students[i]
			i = i - 1
		students[i+1]= key

#insertion sort students based on their name in alphabetical order
def sortNames(students):
	for j in range(1,len(students)):
		key = students[j]
		i = j - 1
		while i >= 0 and students[i][0] > key[0]:
			students[i+1] = students[i]
			i = i - 1
		students[i+1] = key

def findLowestScore(students):
	
	highest_score = students[len(students)-1][1]
	lowest_score = students[0][1]
	second_lowest_score = students[1][1];
	
	#since students is sorted, first score must be lowest
	#by default the second score is the second_lowest though this is not necessarily true
	#the loop searches for the first score greater than the lowest
	#theres no reason compare each score, so it breaks after the first occurence is found
	for i in range(1,len(students)):
		current = students[i]
		if(current[1] > lowest_score):
			if(current[1] >= second_lowest_score):
				second_lowest_score = current[1]
				break

	second_lowest_scores = []
	for i in range(1,len(students)):
		current = students[i]
		if(current[1] == second_lowest_score):
			second_lowest_scores.append(current)
	return second_lowest_scores

if __name__ == "__main__":
	students=[]
    	second_lowest_scores = []
	for _ in range(int(raw_input())):
       		name = raw_input()
       		score = float(raw_input())
        	student_info = [name,score]
    		students.append(student_info)
   
	sortScores(students)
	second_lowest_scores = findLowestScore(students) #find second lowest score
	i = 0
	sortNames(second_lowest_scores)	
	while i < len(second_lowest_scores):
		print(second_lowest_scores[i][0])
		i = i + 1
