#!/usr/bin/env python2.7

alphabet = "abcdefghijklmnopqrstuvwxyz"

def choice():
        """ Ask the user for an input, only allow the vaules of 'e' of 'd'
        My changes show how to put a description in a function, how to use
        a 'while' loop, and to initialize a variable (userInput) """
        userInput = None
        while not userInput:
                choice = raw_input('\nWill you [E]ncrypt or [D]ecrypt to/from a Ceasar Cipher? [E/D]').lower()
                if choice in ("e","d"): 
                        return choice
                else:
                        print ('\n!!!Not a vaild input, please use a "E" for encrypt or a "D" for decrypt ')
                        userInput = None
        
def encrypt():
        plaintext = raw_input("Enter Plain Text here: ")
        key = raw_input('Enter Cipher Key: ')

        cipher = str()
        n = len(key)
        plaintext_chunks = [plaintext[i:i+n] for i in range(0, len(plaintext), n)]
        
        for chunk in plaintext_chunks:
                for i in range(len(chunk)):
                        plainLetter = chunk[i]
                        keyLetter = key[i]
                        
                        if plainLetter.isalpha() and keyLetter.isdigit():
                                cipher += alphabet[(alphabet.index(plainLetter.lower())+int(keyLetter))%(len(alphabet))]
                        elif plainLetter.isalpha() and keyLetter.isalpha():
                                cipher += alphabet[(alphabet.index(plainLetter.lower())+alphabet.index(keyLetter.lower()))%(len(alphabet))]
                        else:
                                cipher += plainLetter
                                                                
        print "The encrypted Text is: %s" % cipher
        print "Your Cipher Key is: %s" % key

def decrypt():
        plaintext = raw_input("Enter Cipher Text here: ")
        key = raw_input('Enter Cipher Key: ')
        
        ciphertext = str()
        n = len(key)
        cipher_chunks = [plaintext[i:i+n] for i in range(0, len(plaintext), n)]
        
        for chunk in cipher_chunks:
                for i in range(len(chunk)):
                        cipherLetter = chunk[i]
                        keyLetter = key[i]
                        
                        if cipherLetter.isalpha() and keyLetter.isdigit():
                                ciphertext += alphabet[(alphabet.index(cipherLetter.lower())-int(keyLetter))%(len(alphabet))]
                        elif cipherLetter.isalpha() and keyLetter.isalpha():
                                ciphertext += alphabet[(alphabet.index(cipherLetter.lower())-alphabet.index(keyLetter.lower()))%(len(alphabet))]
                        else:
                                ciphertext += cipherLetter

        print "The encrypted Cipher Text is: %s" % ciphertext
        print "Your Cipher Key is: %s" % key

if __name__ == "__main__":
        print ('\nWelcome to TessCipher v.0.1')

        while True:
                userInput = choice()

                #part of the user input handling is in the Choice() function, part is below.
                #if the logic was very complex, the input handling could be its own function
                if userInput == 'e':
                        encrypt()
                else:
                        decrypt()
                
