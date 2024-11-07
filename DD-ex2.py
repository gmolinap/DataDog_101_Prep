"""

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Delete the blank spaces and the special caracters
"""

def es_palindromo(s):
    s = ''.join(e for e in s if e.isalnum()).lower()
    print(s)
    return s == s[::-1]

s = "A man, a plan, a canal: Panama"
print(es_palindromo(s))  # True