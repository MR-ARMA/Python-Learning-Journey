def is_Palindrome(word):
    word = word.lower()
    return word == word[::-1]

word = input("Enter your word: ")
is_it = is_Palindrome(word)

if is_it:
    print("yes!")
else:
    print("no!")
