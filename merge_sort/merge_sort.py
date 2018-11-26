import pytest
import math

# this function sorts the elements in a given list and then merges them, recursively
def merge_sort(x,y = None):
	# this conditional accounts for the very first input, which is one list only. It
	# also accounts for when the input list is one element, which occurs only when 
	# the list has an odd number of elements
	if y is None:
		if len(x) >= 2:
			return merge_sort(merge_sort(x[:len(x)/2]), merge_sort(x[len(x)/2:]));
		elif len(x) == 1:
			return x;	

	# the output and loop values are initiated
	output = []
	i, j = 0, 0

	# loop iterates for twice the length of the longest array
	for k in range(0, 2 * max(len(x), len(y))):

		# the lesser element is appended to the output list
		if x[i] <= y[j]:
			output.append(x[i])

			# checks if we reached the element edge in which case
			# we just add the remainder of the other list and break
			if i == len(x) - 1:
				output.extend(y[j:])
				break
			else:
				i += 1
		elif y[j] < x[i]: 
			output.append(y[j])
			if j == len(y) - 1:
				output.extend(x[i:])
				break
			else:
				j += 1

	return output;

def test_answer():
	# even number of elements
	assert(merge_sort([4,2,1,5,8,6,3,7])) == sorted([4,2,1,5,8,6,3,7])
	# already sorted array
	assert(merge_sort([1,2,3,4,5,6,7,8])) == sorted([1,2,3,4,5,6,7,8])
	# descennding order
	assert(merge_sort([8,7,6,5,4,3,2,1])) == sorted([8,7,6,5,4,3,2,1])
	# two elements
	assert(merge_sort([2,1])) == sorted([2,1])
	# odd number of elements
	assert(merge_sort([4,2,1,5,8,6,3])) == sorted([4,2,1,5,8,6,3])
	# negative numbers
	assert(merge_sort([12,15,-23,-4,6,10,-35,28])) == sorted([12,15,-23,-4,6,10,-35,28])
	# one element
	assert(merge_sort([2])) == sorted([2])
	# duplicate elements
	assert(merge_sort([4,2,1,5,8,8,3,7])) == sorted([4,2,1,5,8,8,3,7])
	# same elements
	assert(merge_sort([4,4,4,4,4,4])) == sorted([4,4,4,4,4,4])
	# large even number of elements
	assert(merge_sort([12, 15, 23, 4 , 6, 10, 35, 28, 100, 130, 500, 1000, 235, 554, 75, 345, 800, 222, 333, 888, 444, 111, 666, 777])) == sorted([12, 15, 23, 4 , 6, 10, 35, 28, 100, 130, 500, 1000, 235, 554, 75, 345, 800, 222, 333, 888, 444, 111, 666, 777])
