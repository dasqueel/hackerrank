from itertools import permutations

def checkDivisibility(arr):
    answerList = ['NO'] * len(arr)
    for idx, val in enumerate(arr):
        perms = [''.join(p) for p in permutations(val)]
        for perm in perms:
            if int(perm) % 8 == 0:
                answerList[idx] = 'YES'
                break

    return answerList

print checkDivisibility(['25','140'])