import string
def palindrome_string(s):
    cleaned = (s.translate(str.maketrans('', '', string.punctuation)).replace(" ", "")).lower()
    if(cleaned == cleaned[::-1]):
        print("Palindrome!")
    else:
        print("Not Palindrome!")

def palindrome_number(number):
    number_str = str(number)
    if(number_str == number_str[::-1]):
        print("Palindrome!")
    else:
        print("Not Palindrome!")

user_input = input("Enter number or sentence to check for palindrome: ")
if(user_input.isalpha()):
    palindrome_string(user_input)
else:
    palindrome_number(user_input)
