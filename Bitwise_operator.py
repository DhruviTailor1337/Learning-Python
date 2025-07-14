#program of bitwise operator
a = 10  # Binary: 1010
b = 2   # Binary: 0010  
print("Bitwise AND:", a & b)  # 1010 & 0010 = 0010 (2)
print("Bitwise OR:", a | b)   # 1010 | 0010 = 1010 (10)
print("Bitwise XOR:", a ^ b)  # 1010 ^ 0010 = 1000 (8)
print("Bitwise NOT:", ~a)      # ~1010 = 0101 (-11)
print("Left Shift:", a << 1)   # 1010 << 1 = 10100 (20)
print("Right Shift:", a >> 1)  # 1010 >> 1 = 0101 (5)
print("Left Shift b:", b << 1) # 0010 << 1 = 0100 (4)
print("Right Shift b:", b >> 1) # 0010 >> 1 = 0001 (1)
print("Left Shift a by 2:", a << 2) # 1010 << 2 = 101000 (40)
print("Right Shift a by 2:", a >> 2) # 1010 >> 2 = 0010 (2)
print("Left Shift b by 2:", b << 2) # 0010 << 2 = 1000 (8)
print("Right Shift b by 2:", b >> 2) # 0010 >> 2 = 0000 (0)