list1 =  [1,2,3,4,20,340,50,60,70,80,90,100]
value1 = 20;
for li in list1:
    if li == value1:
        print("Value found:", li)
        break

print("===========================================")

list2 =  [1,2,3,4,20,340,50,60,70,80,90,100]
for li in list2:
    if li > 30:
        print("Value greater than 30 found:", li)
        break

print("===========================================")    

list3 =  ["hi","hello","what","wow","welcome", "to", "python"]
for li in list3:
    if len(li) > 5:
        print("Value found:", li)
        break

print("===========================================")
for i in range(5):
    if i == 3:
        print(i)
        continue
    print(i)

print("===========================================")
for i in range(5):
    if i == 3:
        
        continue
        print(i)
    print(i)

print("===================ITERATION========================")

string = ["10", "20", "abc", "30", "xyz", "40"]
for st in string:
    if st.isdigit():
        print(int(st))
    else:
        print(f"'{st}' is not a number, skipping...")
        continue
print("==================V2=========================")

    # try:
    #     for st in string:
    #         if st.isdigit():
    #             print(int(st))
    #         else:
    #             raise ValueError(f"'{st}' is not a number, skipping...")
    #             continue
    # except ValueError as e:
    #     print(e)
        

print("===========================================")

# import random
# guess_number = int(input("Enter a number between 1 and 100 for the guessing game: "))
# attempts = 0

# while attempts < 5:
#     user_input = input("Guess a number between 1 and 100 (or type 'exit' to quit): ")
#     attempts += 1
#     if user_input.lower() == 'exit':
#         print("Exiting the game. Goodbye!")
#         break
    
#     try:
#         guess = int(user_input)
        
#         if guess < 1 or guess > 100:
#             print("Please enter a number between 1 and 100.")
#             continue
        
#         if guess < guess_number:
#             print("Too low! Try again.")
#         elif guess > guess_number:
#             print("Too high! Try again.")
#         else:
#             print("Congratulations! You've guessed the correct number:", guess_number)
#             break
            
#     except ValueError:
#         print("Invalid input. Please enter a valid number.")

# print("====================CLASS WORK========================")

# print("================== 1 =============================================================================")

# n =int(input("enter a num to find its sum from 1 to n: "))
# sum = 0
# for i in range(1, n + 1):
   
#     sum += i

# print(f"Sum of numbers from 1 to {n}: {sum}")

# print("=================== 2 ===========================================================================")

# word = input("Enter a word to reverse: ")
# reverse_word = word[::-1]
# print("Reversed word:", reverse_word)

# print("=================== 3 ===========================================================================")

# text = input("Enter a text to see number of vowels: ")
# no_vowels =0
# for txt in text:
#     if txt.lower() in 'aeiou':
#         no_vowels += 1
# print(f"Number of vowels in '{text}': {no_vowels}")

# print("=================== 4 ===========================================================================")

# n = int(input("Enter a number to find its factorial: "))
# factorial = 1
# for i in range(1, n + 1):
#     factorial *= i
# print(f"Factorial of {n} is: {factorial}")

# print("=================== 5 ===========================================================================")

# pw = input("Enter a password to check if it is django123: ")
# while True:
#     if pw == "django123":
#         print("Password is correct.")
#         break
#     else:
#         print("Password is incorrect.")
#         pw = input("Enter a password to check if it is django123: ")

# print("=================== 6 ===========================================================================")

# #find max without max()
# nums =[8,3,12,5]
# max_num = nums[0]
# for n in nums:
#     if n > max_num:
#         max_num = n
# print(f"Maximum number in the list is: {max_num}")


#HW
print("=================== 7 ===========================================================================")
#hw
guess = int(input("Guess the secret number between 1 and 10: "))
secret_number = 7
tries = 0

while guess != secret_number:
  tries += 1
  if guess < secret_number:
    print("Too low! Try again.")
  elif guess > secret_number:
    print("Too high! Try again.")

  # Ask for a new guess inside the loop
  guess = int(input("Guess the secret number between 1 and 10: "))

tries += 1  # Count the final correct guess
print( f"Congratulations! You've guessed the secret number {secret_number} in {tries} tries.")