is_male = False
is_tall = False

# if is_male or is_tall: 
#     print("You are a male or tall or both")
# else: 
#     print("You neither male nor tall")

# if is_male and is_tall: 
#     print("You are a male or tall")
# else: 
#     print("You either not male or not tall or both ")

# if is_male and is_tall: 
#     print("You are a male and tall")
# elif is_male and not(is_tall):
#     print("You are a short man")
# elif  not (is_male) and is_tall:
#     print("You are a not a mall, but are tall")
# else: 
#     print("You not male ant not tall")


# comparisons: 

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1 
    elif num2 >= num1 and num2 >= num3:
        return num2 
    else: 
        return num3 

print(max_num(3, 4, 5))
