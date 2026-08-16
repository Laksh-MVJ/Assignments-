roll_no = input("Enter your roll number: ")
digits = []
for x in roll_no:
    digits.append(int(x))

L = []
for x in digits:
    L.append(x * 10)
print("i. L =", L)

L.append(50)
print("After append:", L)

L.insert(2, 70)
print("After insert:", L)

L.remove(50)
print("After remove:", L)

L.pop(2)
print("After pop:", L)

L.sort()
print("Ascending:", L)

L.sort(reverse=True)
print("Descending:", L)
print("First three:", L[:3])
print("Last three:", L[-3:])

average = sum(L) / len(L)
new_list = []
for x in L:
    if x > average:
        new_list.append(x)
print("Average =", average)
print("Greater than average:", new_list)

