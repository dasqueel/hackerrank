'''
def  factorial(n):
    prod = 1
    while n > 0:
        prod = prod * n
        n -= 1
    return prod

print factorial(3)



from itertools import permutations

def  checkDivisibility(arr):
    answerList = ['NO'] * len(arr)
    for idx, val in enumerate(arr):
        perms = [''.join(p) for p in permutations(val)]
        for perm in perms:
            if int(perm) % 8 == 0:
                answerList[idx] = 'YES'
                break

    return answerList

print checkDivisibility(['25','140'])


def  maxDifference(a):
	maxDif = 0
	for idx, val in enumerate(a):
		i = 0
		#currentIdx = idx
		while i < idx:
			try:
				dif = a[idx] - a[i]
				if dif > maxDif:
					maxDif = dif
			except:
				pass
			i += 1
	if maxDif > 0:
		return maxDif
	else:
		return -1

print maxDifference([4,1,2,3])

alpha = 'abcdefghijklmnopqrstuvwxyz'
alList = list(alpha)
def mystery(letter):
    operations = 0
    i = 0
    while i < len(letter)/2:
        ops = abs(alList.index(letter[i]) - alList.index(letter[-i-1]))
        operations = operations + ops
        i += 1
    return operations
mystery('abcd')
'''
