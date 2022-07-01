# make up language:

# vowels -> yhc 

# ----------------

# dog -> dyhc
# cat -> cyhct 

# def translate(phrase):
#     translation = ""
#     for letter in phrase: 
#         if letter in "AEIOUaeiou":
#             translation = translation + "yhc"
#         else: 
#             translation = translation + letter

#     return translation

def translate(phrase):
    translation = ""
    for letter in phrase: 
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "YHC"
            else: 
                translation = translation + "yhc"
        else: 
            translation = translation + letter

    return translation

print(translate(input("Enter a phrase: ")))