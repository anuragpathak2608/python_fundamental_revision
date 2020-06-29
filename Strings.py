string = "Go Corona GO"

print(string)

print(string[-1:])
print(string[-9:])   #[included:excluded ]

print(string[-9:-5])

print(string[3:])

print(string[3:9])

string2 = string + "Go Fast"

print(string2)

string2 = string + "1"
print(string2)

string = "\nGo Corona GO"
print(string*5)

multiline_string = """
Line1
Line2
line3
"""

print(multiline_string)

str1 = string.split(' ')
print(str1)

str2 = "My Name is {1} and my age is {0}"

print(str2.format('Anurag', 25))