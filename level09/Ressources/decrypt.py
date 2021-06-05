import  sys

aa = sys.argv[1]
f = open(sys.argv[1], "r")
i = 0
book = f.readline()
while i < len(book) - 1:
    sys.stdout.write(chr(ord(book[i]) - i))
    i += 1

# The chr() method returns a character (a string) from an integer (represents unicode code point of the character).
# The ord() function returns an integer representing the Unicode character.
