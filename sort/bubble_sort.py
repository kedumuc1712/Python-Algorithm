def buble_sort(list):
	for i in range(0, len(list)):
		for k in range(0, len(list) - i - 1):
			if (list[k] > list[k + 1]):
				# swap list[k], list[k] + 1
				list[k], list[k + 1] = list[k + 1], list[k]

array = [1, 4, 3, 5, 7, 2, 8, 6, 10, 9, 0]
buble_sort(array)

print(array)