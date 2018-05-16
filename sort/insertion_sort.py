def insertion_sort(list):
	for i in range(1, len(list)):
		key = list[i]
		k = i - 1

		while k >= 0 and key < list[k]:
			list[k + 1] = list[k]
			k -= 1

		list[k + 1] = key

array = [20, 1, 4, 3,-3, 5, 7, 17, 2, 8, 6, 10, 9, 0]
insertion_sort(array)

print(array)

