def is_palindrome(word):
    #creates function
    if word == word[::-1]:
        #checks to the if the word is equal to the reverse of it
        return True
        #if it is it returns true
    else:
        #if it doesn't it returns false
        return False

print(is_palindrome("alala")) #prints true
print(is_palindrome("hi")) #prints false