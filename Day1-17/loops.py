n = 1
while n <= 10:
    print(n)
    n += 1
print("----------------------------")
n1 = 10
while n1 >= 1:
    print(n1)
    n1 -= 1

print("----------------------------")
word = "python"
for letter in word:
    print(letter)

print("----------------------------")

start = 2 
for i in range(start, 21, 2):
    print(i)

print("----------------------------")

n = 5
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")

print("----------------------------")

#print the total sim of nums
nums = [4, 9, 2]
total = 0
for num in nums:
    total += num
print(f"Total: {total}")