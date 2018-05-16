def selection_sort(list):
	for i in range(0, len(list)):
		min = list[i]
		for k in range(i + 1, len(list)):
			if (list[k] < min):
				min = list[k]
				# swap list[i] and list[k]
				list[i], list[k] = list[k], list[i]

array = [20, 1, 4, 3,-3, 5, 7, 17, 2, 8, 6, 10, 9, 0]
selection_sort(array)

print(array)