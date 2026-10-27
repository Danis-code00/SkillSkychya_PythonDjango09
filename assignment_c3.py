def calculator():
    s_name = input("Enter your name: ")
    score = int(input("Enter your score: "))

    while score < 0 or score > 100:
        print("Invalid score. Please enter a score between 0 and 100.")
        score = int(input("Enter your score: "))
    if score >= 90:
        print(f"{s_name}, you got an A!") 
    elif score >= 75:
        print(f"{s_name}, you got a B!")    
    elif score >= 60:
        print(f"{s_name}, you got a C!")
    else:
        print(f"{s_name}, you got an F!")

calculator()