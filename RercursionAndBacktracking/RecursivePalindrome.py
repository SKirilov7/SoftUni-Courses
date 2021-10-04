def palindrome(word,index=0,reversed_word=''):
    if index == len(word) and word == reversed_word:
        return f'{word} is a palindrome'
    if index == len(word) and not word == reversed_word:
        return f'{word} is not a palindrome'

    return palindrome(word,index + 1, reversed_word + word[-index - 1])


print(palindrome("abcba", 0))
print(palindrome("peter", 0))