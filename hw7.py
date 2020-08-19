#==========================================
# Purpose: Ecrypts a message using the baconian cipher
# Input Parameter(s):
# message = the message one wants to encode
# encoding = 130-character long encrypter in which each sequence of 5 characters encrypts each letter of the alphabet
# Return Value(s): returns the message following encryption
#==========================================

def encrypt(message, encoding):
    message_to_encode = ''
    for char in message:
        if char.isalpha() == True:
            message_to_encode+=char
            
    message_to_encode = message_to_encode.lower()
    encoded_message = ''
    letters = []
    x = 0
    y = 5
    while y < len(encoding):
        letters.append(encoding[x:y])
        x+=5
        y+=5
    for char in message_to_encode:
        pos = ord(char) - 97
        encoded_message += letters[pos]
    return encoded_message

#==========================================
# Purpose: Decrypts a message that has been encrypted by the baconian cipher
# Input Parameter(s):
# message = the message one wants to decrypt
# encoding = 130-character long encrypter in which each sequence of 5 characters encrypts each letter of the alphabet
# Return Value(s): returns the decrypted message
#==========================================

def decrypt(message, encoding):
    decoded_message = ''
    letters = []
    x = 0
    y = 5
    while y < len(encoding):
        letters.append(encoding[x:y])
        x+=5
        y+=5
    a = 0
    b = 5
    while b <= len(message):
        code = message[a:b]
        for i in range(len(letters)):
            if code == letters[i]:
                pos = i + 97
                decoded_message += chr(pos)
        a+=5
        b+=5
    return decoded_message

#==========================================
# Purpose: The function finds the longest common substring of two DNA sequences
# Input Parameter(s):
# first = first DNA sequence
# second = second DNA sequence
# Return Value(s): returns the longest common substring between the two DNA sequences
#==========================================

def longest_common(first, second):
    list_of_commons = []
    for x in range(len(first)+1):
        for y in range(len(first)+1):
            for a in range(len(second)+1):
                for b in range(len(second)+1):
                    if first[x:y] == second[a:b]:
                        list_of_commons.append(first[x:y])
    
    longest_com = ''
    for elem in list_of_commons:
        if len(elem) > len(longest_com):
            longest_com = elem
    return longest_com

#==========================================
# Purpose: Helper function for igpay that finds the index at which the first vowel occurs
# Input Parameter(s): word = a single string (word), in English
# Return Value(s): returns the index of the vowel
#==========================================


def find_vowel(word):
    word = word.lower()
    for i in range(len(word)):
        if word[i] == 'a' or word[i] == 'e' or word[i] == 'i' or word[i] == 'o' or word[i] == 'u':
            return i

#==========================================
# Purpose: Helper function that defines the translation for English to Pig Latin
# Input Parameter(s): word = a single string (word), in English
# Return Value(s): returns a translated word, WITHOUT capitalization and punctuation, of a word in English to Pig Latin
#==========================================

def half_translate(word):
    translated_word = ''
    if find_vowel(word) == None:
        translated_word = word + 'ay'
    elif find_vowel(word) == 0:
        translated_word = word + 'way'
    elif find_vowel(word) > 0:
        translated_word = word[find_vowel(word):] + word[0:find_vowel(word)] + 'ay'
    translated_word = translated_word.lower()
    return translated_word

#==========================================
# Purpose: Helper function that conducts translation of a word from English to Pig Latin 
# Input Parameter(s):  word = a single string (word), in English
# Return Value(s): returns translation of a word from english to pig latin, WITH capitalization and puncutation
#==========================================


def full_translate(word):
    translated_word = ''
    if word[0].isupper() == True and word[-1].isalpha() == False:
        translated_word += half_translate(word[0:-1])
        translated_word += word[-1]
        translated_word = translated_word.capitalize()
    elif word[0].isupper() == True:
        translated_word += half_translate(word)
        translated_word = translated_word.capitalize()
    elif word[-1].isalpha() == False:
        translated_word += half_translate(word[0:-1])
        translated_word += word[-1]
    else:
        translated_word += half_translate(word)
    return translated_word

#==========================================
# Purpose: function that conducts translation of a phrase from English to Pig Latin 
# Input Parameter(s):  phrase = a group of strings (words), in English
# Return Value(s): returns translation of a phrase from English to Pig Latin, WITH capitalization and puncutation
#==========================================

def igpay(phrase):
    new_phrase = phrase.split()
    for i in range(len(new_phrase)):
        new_phrase[i] = full_translate(new_phrase[i])
    translated_phrase = ' '.join(new_phrase)
    return translated_phrase
