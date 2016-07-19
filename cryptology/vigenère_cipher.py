#!/usr/bin/env python2.7

alpha = " ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789!#$%&\'()*+,-./:;<=>?_~`{}"

'''
~~~~~~~~~~~~~ TEST ~~~~~~~~~~~~~~~~~~~~~~~
Will you [E]ncrypt or [D]ecrypt to/from a Vigenere Cipher? [E/D]e

Enter Text (plain or cipher): Charlie is the #1 Best guy 4ever!?!
Enter Cipher Key: abc123
Results:c93JEC5 #K N86 cT b6-L A-< V`P5+Duc

Would you like to play again? [Y/N]y

Will you [E]ncrypt or [D]ecrypt to/from a Ceasar Cipher? [E/D]d

Enter Text (plain or cipher): c93JEC5 #K N86 cT b6-L A-< V`P5+Duc
Enter Cipher Key: abc123
Results:Charlie is the #1 Best guy 4ever!?!
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''

def get_user_input():
    """ Get the user's input """

    method = None
    while not method:
            method = raw_input('\nWill you [E]ncrypt or [D]ecrypt to/from a Vigenere Cipher? [E/D]').lower()
            if method in ("e","d"):
                continue
            else:
                    print ('\n!!!Not a vaild input, please use a "E" for encrypt or a "D" for decrypt ')
                    method = None

    text = raw_input('\nEnter Text (plain or cipher): ')

    key = None
    while not key:
        key = raw_input('Enter Cipher Key: ')
        for i in key:
            if i in alpha:
                continue
            else:
                print "Bad symbol used in key: %s" % i
                key = None

    return method, text, key
    

def build_tabula_recta():
    """ Builds a list of lists representing a tabula recta
    https://en.wikipedia.org/wiki/Vigenere_cipher """

    tabula = []
    for i in range(len(alpha)):
        tabula_row = []
        for n in range(len(alpha)):
            letter = alpha[(n+i)%(len(alpha))]
            tabula_row.append(letter)
        tabula.append(tabula_row)

    return tabula

def encypt(keyLetter, textLetter, tabula):
    """ Access the right letter in the list of lists (tabula) using index numbers  """
    tabula_row = alpha.index(keyLetter) #select the alphabet to use with the key letter
    tabula_column = alpha.index(textLetter) #select the letter of that alphabet with the text letter

    encypted_letter = tabula[tabula_row][tabula_column]
    return encypted_letter

def decrypt(keyLetter, cipherLetter, tabula):
    """ blah """
    tabula_row = alpha.index(keyLetter) #the key letter will still be used to select the correctly shifted alphabet
    alpha_index = tabula[tabula_row].index(cipherLetter) #but instead of getting the index of alpha we need the index of the cipher row

    decrypted_letter = alpha[alpha_index]
    return decrypted_letter


def main():
    method, plainText, key = get_user_input()
    
    n = len(key)
    results = str()
    tabula = build_tabula_recta()

    plainText_chunks = [(plainText[i:i+n]) for i in range(0, len(plainText), n)]
    for chunk in plainText_chunks:
        for i in range(len(chunk)):
            textLetter, keyLetter = chunk[i], key[i]
            if textLetter in alpha:
                if method=='e':
                    results += encypt(keyLetter, textLetter, tabula)
                else:
                    results += decrypt(keyLetter, textLetter, tabula)
            else:
                results += textLetter

    print "Results:%s" % results

    again = raw_input('\nWould you like to play again? [Y/N]').lower()
    if again == 'y':
        main()
    else:
        print "Goodbye"

main()
            
        
    
    
    



