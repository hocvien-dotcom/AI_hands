matrix_len = int(input("matrix len: "))
max_int = int(input("max int: "))

a = matrix_len
b = matrix_len - max_int

for i in range(max_int - 1):
    a += 2 * b
    b -= max_int

print(a)