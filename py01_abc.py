print("Hello, world!")

x: int = 1
y = 2
z = x + y

s1 = "Hello"
s2 = "World!"
s3 = s1 + ", " + s2
print(s3)

# Comment
# message = str(x) + "+" + str(y) + "=" + str(z)
message = f"{x}+{y}={z}"
print(message)

full_name = "Yuri Andrienko"
space_position = full_name.find(" ")
if space_position > 0:
    first_name = full_name[0:space_position]
    print(first_name)
    last_name = full_name[space_position + 1:]
    print(last_name)
    name_with_initial = first_name[0] + "." + last_name
    print(name_with_initial)
else:
    print(f"No space in input data {full_name}")
    
nums = [1, 2, 3, 4]
print(nums[1])
nums.append(777)
nums.pop(1)
print(nums)

people = ["Yuri", "Vasya", "Masha"]
print(people[1:])

for person in people:
    print(person)
    
    
full_name = "Yuri Andrienko"
splitted = full_name.split(" ")
print(splitted)
first_name = splitted[0]
last_name = splitted[1]
print(f"{last_name}, {first_name}")
