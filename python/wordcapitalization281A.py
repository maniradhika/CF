"""Capitalization is writing a word with its first letter as a capital letter. Your task is to capitalize the given word.

Note, that during capitalization all the letters except the first one remains unchanged.

Input
A single line contains a non-empty word. This word consists of lowercase and uppercase English letters. The length of the word will not exceed 103.

Output
Output the given word after capitalization."""

#solution:

a = input("")
b = list(a)
c = b[0]
if c.islower():
    d = ord(a[0:1])
    e = d-32
    f = chr(e)
    print(f + a[1:])
else:
    print(a)