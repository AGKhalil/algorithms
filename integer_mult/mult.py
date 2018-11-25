import math

def digit_n(x):
	if x == 0:
		return 1;

	count = 0
	while x != 0:
		x /= 10
		count += 1
	return count;

def pieces(x):
	if digit_n(x) == 1:
		return 0, x;

	digits = digit_n(x)
	xstr = str(x)
	large = int(xstr[:digits/2])
	small = int(xstr[digits/2:])

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

def karatsuba(x, y):
	digits = digit_n(x)

	xh, xl = pieces(x)
	yh, yl = pieces(y)
	print(digits)
	print(pieces(x))
	print(pieces(y))

	if digit_n(xh) == 1 & digit_n(yh) == 1:
		a = xh * yh
		print("a in ", a)
	else:
		a = karatsuba(xh, yh)
		print("a out ", a)

	if digit_n(xl) == 1 & digit_n(yl) == 1:
		d = xl * yl
		print("d in ", d)
	else:
		d = karatsuba(xl, yl)
		print("a out ", d)

	if digit_n(xh + xl) == 1 & digit_n(yh + yl) == 1:
		e = (xh + xl) * (yh + yl) - a - d
		print("e in ", e)
	else:
		e = karatsuba((xh + xl), (yh + yl)) - a - d
		print("e out ", e)

	return a * (10**digits) + e * (10**math.ceil(float(digits)/2.0)) + d;

# print(karatsuba(11225, 1234))
# print(11225*1234)
# print(pieces(12345))
print(digit_n(12345))
print(karatsuba(123444,123444))
print(123444*123444)
# print(math.ceil(float(digit_n(111))/2.0))
# print(digit_n(111))
print(pieces(1224))

