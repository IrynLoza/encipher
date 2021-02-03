"""Write a function that encrypts a string with a variable rotary cipher.

The function should take in a number and string and shift the string's
characters by that number:

>>> rot_encode(1, 'abcxyz')
'bcdyza'

It should be able to shift characters by any number:

>>> rot_encode(3, 'abcxyz')
'defabc'

It should preserve capitalization, whitespace, and any special characters:

>>> rot_encode(1, 'wow! this is 100% amazing.')
'xpx! uijt jt 100% bnbajoh.'
"""


def rot_encode(shift, txt):
    """Encode `txt` by shifting its characters to the right."""
    txt = txt.lower()
    
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g','h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 
    'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    cipher = {
        'a': 'a',
        'b': 'b',
        'c': 'c',
        'd': 'd',
        'e': 'e',
        'f': 'f',
        'g': 'g',
        'h': 'h',
        'i': 'i',
        'j': 'j',
        'k': 'k',
        'l': 'l',
        'm': 'm',
        'n': 'n',
        'o': 'o',
        'p': 'p',
        'q': 'q',
        'r': 'r',
        's': 's',
        't': 't',
        'u': 'u',
        'v': 'v',
        'w': 'w',
        'x': 'x',
        'y': 'y',
        'z': 'z'
    }

    start = 0
    for char in cipher:
        if shift < len(alpha):
            cipher[char] = alpha[shift]
            shift+= 1
        if char == cipher[char]:
            cipher[char] =  alpha[start]  
            start+= 1    
      

    result = ''
    for char in txt:
        if char in cipher:
            result = f'{result}{cipher[char]}'
        else:    
            result = f'{result}{char}'   

    return result     
   


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')
