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

user_string = input("Enter a sentence to check for palindrome: ")
palindrome_string(user_string)

user_number = input("Enter a number to check for palindrome: ")
palindrome_number(user_number)
