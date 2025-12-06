# O(n) time and space
# link: https://www.codewars.com/kata/530e15517bc88ac656000716/


def rot13(message):
    def rotate(c):
        if c.isalpha():
            if c == c.upper():
                base = ord('A')
            else:
                base = ord('a')
            code = ord(c) - base
            code += 13
            code %= 26
            code += base
            c = chr(code)
        return c

    return ''.join([rotate(c) for c in message])
