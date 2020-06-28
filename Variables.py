a = 1
b = "string"
c = 5.5
d = True

print("Data Type of A", type(a), "\n", "Value of A: ", a)
print("Data Type of B", type(b), "\n", "Value of B: ", b)
print("Data Type of C", type(c), "\n", "Value of C: ", c)
print("Data Type of D", type(d), "\n", "Value of D: ", d)


#Type casting
#Converting one datatype to another

A = str(a)
C = int(c)
B = bool(b)
D = int(d)

print("int -- > str", A, "Data Type of A", type(A))
print("float -- > int", C, "Data Type of C", type(C))
print("str -- > bool", B, "Data Type of B", type(B))
print("bool -- > int", D, "Data Type of D", type(D))
