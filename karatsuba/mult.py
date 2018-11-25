import pytest
import math

def digit_n(x):
	if x == 0 | long(x) == 0:
		return 1;

	if(isinstance(x, basestring)):
		return len(x);

	x = str(x)
	return len(x);

def pieces(x):
	if digit_n(x) == 1:
		return '0', str(x);

	digits = digit_n(x)
	xstr = str(x)
	large = xstr[:digits/2]
	small = xstr[digits/2:]

	# print(digit_n(small) % 2 != 0)
	# print(digit_n(small) != 1)

	if digit_n(small) != digit_n(large):
		# print("Im here")
		large = '0' + xstr[:digits/2]
		# print(large)

	# holder = x
	# small = 0
	# large = 0

	# large = x / pow(10, digits / 2)

	# count = 0
	# while count < digits / 2:
	# 	small = small + (holder % 10) * pow(10, count)
	# 	holder /= 10
	# 	count += 1

	return large, small;

def karatsuba(xin, yin):
	x = str(xin)
	y = str(yin)
	digits_x = digit_n(x)
	if (digit_n(x) % 2 != 0):
		digits_x += 1

	digits_y = digit_n(y)
	if (digit_n(y) % 2 != 0):
		digits_y += 1

	diff = digits_x - digits_y
	print("diff ", diff)

	if (diff > 0):
		y = '0' * abs(diff) + y
	elif (diff < 0):
		x = '0' * abs(diff) + x

	xh, xl = pieces(x)
	yh, yl = pieces(y)

	print("x is ", x)
	print("y is ", y)
	print("x pieces ", xh, xl)
	print("y pieces ", yh, yl)

	if digit_n(xh) == 1 and digit_n(yh) == 1:
		a = long(xh) * long(yh)
		print("a in ", a)
	else:
		a = karatsuba(xh, yh)
		print("a out ", a)

	if digit_n(xl) == 1 and digit_n(yl) == 1:
		d = long(xl) * long(yl)
		print("d in ", d)
	else:
		d = karatsuba(xl, yl)
		print("a out ", d)

	if digit_n(long(xh) + long(xl)) == 1 and digit_n(long(yh) + long(yl)) == 1:
		e = (long(xh) + long(xl)) * (long(yh) + long(yl)) - long(a) - long(d)
		print("e in ", e)
	else:
		e = karatsuba((long(xh) + long(xl)), (long(yh) + long(yl))) - a - d
		print("e out ", e)

	digits = digits_x/2 if digits_x >= digits_y else digits_y/2

	print(long(a * (10**(2*digits)) + e * (10**digits) + d))

	return long(a * (10**(2*digits)) + e * (10**digits) + d);

# def setup_function(function):
#     print("setting up %s" % function)

def test_answer():
    assert karatsuba(1,1) == 1
    assert karatsuba(1,2) == 2
    assert karatsuba(1,3) == 3
    assert karatsuba(1,4) == 4
    assert karatsuba(1,5) == 5
    assert karatsuba(1,6) == 6
    assert karatsuba(1,7) == 7
    assert karatsuba(1,8) == 8
    assert karatsuba(1,9) == 9

    assert karatsuba(2,2) == 4
    assert karatsuba(2,3) == 6
    assert karatsuba(2,4) == 8
    assert karatsuba(2,5) == 10
    assert karatsuba(2,6) == 12
    assert karatsuba(2,7) == 14
    assert karatsuba(2,8) == 16
    assert karatsuba(2,9) == 18

    assert karatsuba(3,5) == 15

    assert karatsuba(9,9) == 81

    assert karatsuba(19,19) == 19*19

    assert karatsuba(15,17) == 15*17

    assert karatsuba(151,175) == 151*175

    assert karatsuba(795,627) == 498465
    assert karatsuba(195,627) == 122265

    assert karatsuba(3141592653589793238462643383279502884197169399375105820974944592,2718281828459045235360287471352662497757247093699959574966967627) == 3141592653589793238462643383279502884197169399375105820974944592*2718281828459045235360287471352662497757247093699959574966967627
    assert karatsuba(1149444592,1166967627) == 1149444592*1166967627
    assert karatsuba(42, 100) == 100*42

print(karatsuba(3141592653589793238462643383279502884197169399375105820974944592,2718281828459045235360287471352662497757247093699959574966967627))
print(3141592653589793238462643383279502884197169399375105820974944592*2718281828459045235360287471352662497757247093699959574966967627)
