# Check if a string is a palindrome.

# Description: Determine if a given string is a palindrome (reads the same backward as forward). Ignore case and non-alphanumeric characters.

# Input: "A man, a plan, a canal: Panama"
# Output: True

def is_palindrome(str):
    # convert to lowercase and filter alphanumeric characters
    filtered_s = ''.join(char.lower() for char in str if char.isalnum())
    print(filtered_s)
    left, right = 0, len(filtered_s)-1
    while left<right:
        if filtered_s[left] != filtered_s[right]:
            return False
        left+=1
        right-=1
    return True

print(is_palindrome("A man, a plan, a canal: Panama"))

def is_palindrome_inplace_checking(str):
    left, right = 0, len(str)-1
    while left<right:
        if str[left].lower() == str[right].lower():
            if not(str[left].isalnum()):
                left+=1
            else:
                right-=1
    return str

# is_palindrome_inplace_checking("A man, a plan, a canal: Panama")

print(len("A man, a plan, a canal: Panama"))