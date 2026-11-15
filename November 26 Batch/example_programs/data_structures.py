list1 = [12, "abhinav", 763, 14502]
print(list1)
print(list1[2])
print(list1[-3])

dict1 = {
    "name": "abhinav",
    "subject": "python",
    "rollNo": 3029754,
    "hello": None
}

print(dict1["name"])
print(dict1["rollNo"])

list1 = [34,65,67,54,23,34,65]

for i,val in enumerate(list1, start=1):
    print(i,val)

rollNo = [1,2,3,4,5]
names = ["Abhinav", "Aman", "Rahul", "Yash", "Yuvraj"]

print(dict(zip(rollNo, names)))

# {
#     1: "Abhinav",
#     2: "Aman",
#     3: "Rahul",
#     4: "Yash",
#     5: "Yuvraj"
# }