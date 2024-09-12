import re

def is_palindrome(string):
  forwardString = []
  reverseString = []

  forwardString = ''.join(re.findall(r'[a-z]+', string.lower()))
 
  reverseString = forwardString[::-1]
  
  return (forwardString == reverseString)

print(is_palindrome('hello world'))
print(is_palindrome("Go hang a salami, I'm a lasagna hog"))
    