def array_left_rotation(a, n, k):
	newArr = [None] * n
	for idx,val in enumerate(a):
		newArr[idx-k] = val
	return newArr

print array_left_rotation([1,2,3,4],4,1)