def matrix_dot_vector(a:list[list[int|float]],b:list[int|float])-> list[int|float]:
	c = []
	for sub_a in a:
		len_ = len(sub_a)
		if len_ != len(b):
			return -1
		sum_ = 0
		for i in range(len_):
			sum_ += sub_a[i] * b[i]
		c.append(sum_)
	return c

print(matrix_dot_vector([[1,2,3],[2,4,5],[6,8,9]],[1,2,3])) # [14, 25, 49]
print(matrix_dot_vector([[1,2],[2,4],[6,8],[12,4]],[1,2,3])) # -1