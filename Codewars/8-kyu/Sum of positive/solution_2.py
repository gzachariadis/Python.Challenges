def positive_sum(arr):
	if arr:
		return sum([i for i in arr if i >= 0])
	return 0
