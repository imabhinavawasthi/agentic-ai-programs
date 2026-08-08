list1 = ["hello", 100, 10.2321, 1000, "world", 10.2321, 1000]

for i in list1:
    print(i)

for i in range(len(list1)):
    print(i, list1[i])

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

for index, fruit in enumerate(fruits):
    print(index, fruit)

rollNo = [1, 2, 3, 4]
names = ["Abhinav", "Aman", "Ankit", "Sachin"]

# create a dictionary: { 1: "Abhinav", 2: "Aman", 3: "Ankit", 4: "Sachin" }
student_info = dict(zip(rollNo, names))
print(student_info)
