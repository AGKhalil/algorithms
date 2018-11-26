import pytest
import math

def take_input(xin):
	x = xin[:len(xin)/2]
	y = xin[len(xin)/2:]
	c = []
	sortm(x,y,c)

def sortm(xin):
	x = xin
	print('sortm ', x)
	if len(x) == 2:
		if x[0] > x[1]:
			return [x[1], x[0]];
		elif x[0] <= x[1]:
			return [x[0], x[1]];
	elif len(x) > 2:
		x = xin[:len(xin)/2]
		y = xin[len(xin)/2:]
		return merge(sortm(x), sortm(y));
	elif len(x) == 1:
		return x;

def merge(x,y):
	c = []
	print('merge ',x,y)
	i, j = 0, 0
	print('len ', 2*max(len(x),len(y)))
	for k in range(0,2*max(len(x),len(y))):
		print('k ', k, ' i ', i, ' j', j)
		if x[i] <= y[j]:
			c.append(x[i])
			if i == len(x) - 1:
				c.extend(y[j:])
				break
			else:
				i += 1
		elif y[j] < x[i]: 
			c.append(y[j])
			if j == len(y) - 1:
				c.extend(x[i:])
				break
			else:
				j += 1

	print('merged ', c)
	return c;

# print(sortm([12, 15, 23, 4 , 6, 10, 35, 28, 100, 130, 500, 1000, 235, 554, 75, 345, 800, 222, 333, 888, 444, 111, 666, 777]))
print(sortm([4,2,1,5,8,8,3,7]))
print(sorted([4,2,1,5,8,8,3,7]))
# print(7/2)

def test_answer():
	# even number of elements
	assert(sortm([4,2,1,5,8,6,3,7])) == sorted([4,2,1,5,8,6,3,7])
	# already sortmed array
	assert(sortm([1,2,3,4,5,6,7,8])) == sorted([1,2,3,4,5,6,7,8])
	# descennding order
	assert(sortm([8,7,6,5,4,3,2,1])) == sorted([8,7,6,5,4,3,2,1])
	# two elements
	assert(sortm([2,1])) == sorted([2,1])
	# odd number of elements
	assert(sortm([4,2,1,5,8,6,3])) == sorted([4,2,1,5,8,6,3])
	# negative numbers
	assert(sortm([12,15,-23,-4,6,10,-35,28])) == sorted([12,15,-23,-4,6,10,-35,28])
	# one element
	assert(sortm([2])) == sorted([2])
	# duplicate elements
	assert(sortm([4,2,1,5,8,8,3,7])) == sorted([4,2,1,5,8,8,3,7])
	# same elements
	assert(sortm([4,4,4,4,4,4])) == sorted([4,4,4,4,4,4])
	# large even number of elements
	assert(sortm([12, 15, 23, 4 , 6, 10, 35, 28, 100, 130, 500, 1000, 235, 554, 75, 345, 800, 222, 333, 888, 444, 111, 666, 777])) == sorted([12, 15, 23, 4 , 6, 10, 35, 28, 100, 130, 500, 1000, 235, 554, 75, 345, 800, 222, 333, 888, 444, 111, 666, 777])
