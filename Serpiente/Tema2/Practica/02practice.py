def isPalindrome(word, inverted_word):
    palindromable_word = ""
    palindromable_inverted_word = ""
    
    for char in word:
        if char != " ":
            palindromable_word = palindromable_word + char
    for char in inverted_word:
        if char != " ":
            palindromable_inverted_word = palindromable_inverted_word + char
    
    if palindromable_inverted_word.lower() == palindromable_word.lower():
        return True
    else:
        return False


user_input = input("Introduzca una palabra: ")
palabra_invertida = ""

for char in user_input:
    palabra_invertida = char + palabra_invertida

print(palabra_invertida)

isWordPalindrome = isPalindrome(user_input, palabra_invertida)
print(isWordPalindrome)

