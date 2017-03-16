arr = [396285104, 573261094, 759641832, 819230764, 364801279]
arr.sort

smallest = min(arr)
greatest = max(arr)
print arr[:4], arr[1:]

#print sum(list(set(arr) - set([greatest]))), sum(list(set(arr) - set([smallest])))
#print sum(arr[:4]), sum(arr[1:])