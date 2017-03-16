# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

spots = None
ops = []

with open("crush.txt", "r") as myfile:
	for idx, line in enumerate(myfile):
	    line = line.split(' ')
	    if idx == 0:
	        spots = int(line[0])
	    else:
	        ops.append([int(line[0]),int(line[1]),int(line[2])])

smallest = []
greatest = []
for op in ops:
	smallest.append(op[0])
	greatest.append(op[1])
print min(smallest), max(greatest)

'''
with open("crush.txt", "r") as myfile:
	for idx, line in enumerate(myfile):
	    line = line.split(' ')
	    if idx == 0:
	        spots = int(line[0])
	        opsNum = int(line[1])
	    else:
	        ops.append([int(line[0]),int(line[1]),int(line[2])])

	answerArr = [0]*spots
	for op in ops:
	    for idx in range(op[0]-1,op[1]):
	            answerArr[idx] =  answerArr[idx] + op[2]
	print max(answerArr)
'''
'''
#read STDIN and turn into variables
for idx, line in enumerate(sys.stdin):
    line = line.split(' ')
    if idx == 0:
        spots = int(line[0])
        opsNum = int(line[1])
    else:
        ops.append([int(line[0]),int(line[1]),int(line[2])])
print spots

answerArr = [0]*spots
for op in ops:
    for idx,val in enumerate(answerArr):
        if op[1] >= idx+1 >= op[0]:
            answerArr[idx] =  answerArr[idx] + op[2]
print max(answerArr)
'''