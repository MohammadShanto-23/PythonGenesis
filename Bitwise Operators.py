
a = 10  # Binary: 1010
b = 4   # Binary: 0100

print("a =", a, "Binary:", bin(a))
print("b =", b, "Binary:", bin(b))

# AND Operator
print("a & b =", a & b)  # 1010 & 0100 = 0000 0100 = 4

# OR Operator
print("a | b =", a | b)  # 1010 | 0100 = 1110 = 14

# XOR Operator
print("a ^ b =", a ^ b)  # 1010 ^ 0100 = 1110 = 14

# NOT Operator
print("~a =", ~a)        # ~1010 = -(a+1) = -11

# Left Shift Operator
print("a << 1 =", a << 1)  # 1010 << 1 = 10100 = 20

# Right Shift Operator
print("a >> 1 =", a >> 1)  # 1010 >> 1 = 0101 = 5