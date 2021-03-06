#compare the cube lengths and size of the lists themselves to determine the cube to attempt to stack
#leftLen = length/size of left_lengths list
#rightLen = length/size of right_lengths list
#leftElement = current element from left_lengths list
#rightElement = current element from right_lengths list
def compareCubeLengths(leftElement,leftLen,rightElement,rightLen):
	if(leftLen == rightLen):
		if(leftElement > rightElement):
			return "leftElement"
		elif (rightElement > leftElement):
			return "rightElement"
		else:
			return "leftElement"
	#since cube lengths are equal take the cube from the larger list
	else:
		if(leftLen > rightLen):
			return "leftElement"
		elif(rightLen > leftLen):
			return "rightElement"
		else:
			return "leftElement"

def checkCube(top_cube,new_cube):
	if(new_cube < top_cube):
		return True
	else:
		return False

#split side_lengths into two lists
#left side pointer increments, right side decrements
#find the largest block on either end and append to one of the new stacks
#argment cube_stats is the num_cubes and side_lengths list for the current list of cubes
def stackCubes(cube_stats):
	num_cubes = int(cube_stats[0])
	side_lengths = cube_stats[1]
	left_lengths = [] #left half of side_lengths
	right_lengths = [] #right half of side_lengths
	middle = num_cubes // 2

	#add side_lengths to left_lengths
	for i in range(0,middle):
		left_lengths.append(side_lengths[i])

	#add side_lengths to right_lengths
	for i in range(middle,num_cubes):
		right_lengths.append(side_lengths[i])

	#cubes are stacked into two vertical piles
	left_stack = [] 							#represents left vertical pile
	right_stack = []							#represents right vertical pile
	left_lengths_i = 0 							#current index in left_lengths, moving left to right
	right_lengths_i = len(right_lengths) - 1 	#current index in right_lengths, moving right to left
	left_top_cube = 0 							#pointer to current / top cube in stack (left)
	right_top_cube = 0 							#pointer to current / top cube in stack (right)

	canStack = True

	#iterate over each cube, first determine the largest cube from either lengths
	#list, the largest will be the cube added to the stack
	#next, check for empty stacks and add cubeToStack to either empty stacks
	#then check for the shortest stack and if the top_cube is larger than cubeToStack, add it
	#else, check the other stack, since stacks can be unequal heights, if the top_cube is
	#larger than cubeToStack, add it. else, return canStack status as false
	for i in range(0,num_cubes):

		print("left_lengths_i", left_lengths_i)
		print("right_lengths_i", right_lengths_i)

		#left and right lengths lists are unempty
		if(left_lengths_i <= len(left_lengths)-1 and right_lengths_i >= 0):
			leftElement = left_lengths[left_lengths_i]
			rightElement = right_lengths[right_lengths_i]
			cubeToStack = compareCubeLengths(leftElement,len(left_lengths),rightElement,len(right_lengths))
			print(cubeToStack)

		else:
			#left lengths list is unempty
			if(left_lengths_i <=len(left_lengths)-1):
				leftElement = left_lengths[left_lengths_i]
				cubeToStack = leftElement

			#right lengths list is unempty
			elif(right_lengths_i >= middle):
				rightElement = right_lengths[right_lengths_i]
				cubeToStack = rightElement

		#remove the cubeToStack from its respective list
		if(cubeToStack == "leftElement"):
			cubeToStack = leftElement
			left_lengths_i +=1
			#left_lengths.remove(leftElement)
		elif(cubeToStack == "rightElement"):
			cubeToStack = rightElement
			#right_lengths.remove(rightElement)
			right_lengths_i -= 1

		#check for empty stacks
		if not left_stack:
			left_stack.append(cubeToStack)
		elif not right_stack:
			right_stack.append(cubeToStack)

		#add element to smaller stacks after checking top
		#cubes length, cube can only be added if top_cube is large than cubeToStack
		else:
			#if left_stack is shorter
			if(len(left_stack) <= len(right_stack)):
				#if cubeToStack is smaller than the current topCube
				if(checkCube(left_stack[left_top_cube],cubeToStack)):
					left_stack.append(cubeToStack)
					left_top_cube += 1
				else:
					#if cubeToStack is smaller than the current topCube
					if(checkCube(right_stack[right_top_cube],cubeToStack)):
						right_stack.append(cubeToStack)
						right_top_cube += 1
					else:
						canStack = False
						return canStack
			#if right_stack is shorter than left_stack
			else:
				if(checkCube(right_stack[right_top_cube],cubeToStack)):
					right_stack.append(cubeToStack)
					right_top_cube += 1
				else:
					if(checkCube(left_stack[left_top_cube],cubeToStack)):
						left_stack.append(cubeToStack)
						left_top_cube += 1
					else:
						canStack = False
						return canStack
		print("left_stack",left_stack)
		print("right_stack",right_stack)
		print(" ")
	return canStack
if __name__ == "__main__":
	t = int(raw_input()) # number of test cases
	i = 0
	cube_list = []
	while i < t:
		cube_stats = []
		num_cubes = raw_input()
		side_lengths = raw_input()
		side_lengths = side_lengths.split(" ")
		cube_stats.append(num_cubes)
		cube_stats.append(side_lengths)
		cube_list.append(cube_stats)
		i+=1

	i = 0
	while i < t:
		canStack = stackCubes(cube_list[i])
		if canStack:
			print("Yes")
		else:
			print("No")
		i+=1
