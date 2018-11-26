import pytest
import math

# this function returns the length of a number. The input can be string or int
def digit_n(x):
	# converts input to string
	x = str(x)
	# checks if the input is zero and returns a length of 1
	if int(x) == 0:
		return 1;
	
	return len(x);

# this function breaks a number into upper and lower pieces
def pieces(x):
	digits = digit_n(x)

	# if input is of length 1, returns two pieces '0' and 'number'
	if digits == 1:
		return '0', str(x);

	# breaks number into upper and lower pieces
	large = x[:digits/2]
	small = x[digits/2:]

	return large, small;

def karatsuba(xin, yin):
	x = str(xin)
	y = str(yin)

	# the base case. If inputs are single digits, multipl them
	if digit_n(xin) == 1 and digit_n(yin) == 1:
		return int(xin) * int(yin);
	else: 
		digits_x = digit_n(x)
		digits_y = digit_n(y)
		
		# increments x and y when they are of odd number lengths
		if (digit_n(x) % 2 != 0):
			digits_x += 1
		elif (digit_n(y) % 2 != 0):
			digits_y += 1

		# pads x or y appropriately when they are of unequal lengths
		diff = digits_x - digits_y
		if (diff > 0):
			y = '0' * abs(diff) + y
		elif (diff < 0):
			x = '0' * abs(diff) + x

		# breaks x and y into upper and lower pieces
		xh, xl = pieces(x)
		yh, yl = pieces(y)

		# performs the karatsuba multiplication
		a = karatsuba(xh, yh)
		d = karatsuba(xl, yl)
		e = karatsuba((int(xh) + int(xl)), (int(yh) + int(yl))) - a - d

		# chooses the final digits number to be the higher of digits_x and digits_y
		digits = max(digits_x, digits_y)

		return int(a * (10**(digits)) + e * (10**(digits/2)) + d);

def test_answer():
	# test the output when the input size changes
	# this also tests odd multiplication and odd-length multiplication
	assert karatsuba(2,9) == 2*9
	assert karatsuba(23,93) == 23*93
	assert karatsuba(234,934) == 234*934
	assert karatsuba(23455,93455) == 23455*93455
	assert karatsuba(2345566,9345566) == 2345566*9345566
	assert karatsuba(234556677,934556677) == 234556677*934556677
	assert karatsuba(23455667788,93455667788) == 23455667788*93455667788
	assert karatsuba(2345566778899,9345566778899) == 2345566778899*9345566778899

	# test unequal length multiplication
	assert karatsuba(12,1234) == 12*1234
	assert karatsuba(123,1234) == 123*1234

	# test 64-bit multiplication
	assert karatsuba(3141592653589793238462643383279502884197169399375105820974944592,2718281828459045235360287471352662497757247093699959574966967627) == 3141592653589793238462643383279502884197169399375105820974944592*2718281828459045235360287471352662497757247093699959574966967627

