def mergeSort(list):
	print("Splitting ", list)

	if len(list) > 1:
		mid = len(list) // 2
		left_half = list[:mid]
		right_half = list[mid:]

		mergeSort(left_half)
		mergeSort(right_half)

		i = 0
		j = 0
		k = 0

		while i < len(left_half) and j < len(right_half):
			if left_half[i] < right_half[j]:
				list[k] = left_half[i]
				i += 1
			else:
				list[k] = right_half[j]
				j += 1
			k += 1

		while i < len(left_half):
			list[k] = left_half[i]
			i += 1
			k += 1

		while j < len(right_half):
			list[k] = right_half[j]
			j += 1
			k += 1

	print("Merging ", list)

list = [54,26,93,17,77,31,44,55,20]
mergeSort(list)
print(list)