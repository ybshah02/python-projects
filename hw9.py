import random

#==========================================
# Purpose: The function combines two dictionaries
# Input Parameter(s):
# d1 = dictionary with a string key, and integer value
# d2 = another dictionary with a string key, and integer value
# Return Value(s): returns a NEW dictionary with the combination of dictionary 1 and 2
#==========================================

def combine(d1,d2):
    
    dSum = {}
    dSum.update(d1)
    
    for key in d2:
        if key in dSum:
            dSum[key] += d2[key]
        else:
            dSum.update({key: d2[key]})

    return dSum

#==========================================
# Purpose: Creates a dictionary of all the first words in a text file, and records the frequency of those first words
# Input Parameter(s): fname = a text file filled with strings of single-lined sentences
# Return Value(s): returns a dictionary with keys as the first words, and frequency of those words as the value
#==========================================

def first_words(fname):

    fp = open(fname, 'r')
    all_first_words = {}
    
    for line in fp:
        line = line.split(' ')
        if line[0] not in all_first_words:
            all_first_words.update({line[0]:1})
        else:
            all_first_words[line[0]]+=1
        line = ' '.join(line)
    fp.close()
    return all_first_words

#==========================================
# Purpose: Creates a nested dictionary of all the words in the file, with another dictionary for each word representing each possible following word, and its frequency
# Input Parameter(s): fname = a text file filled with strings of single-lined sentences
# Return Value(s): returns a nested dictionary with keys as each word, and for each word, there are keys representing its following words, and its frequency in the
#==========================================

def next_words(fname):

    fp = open(fname, 'r')
    all_words = {}

    for line in fp:
        line = line.split(' ')
        for i in range(len(line)-1):
            
            if line[i] not in all_words:
                if line[i+1] == line[-1]:
                    all_words.update({line[i]: {'.': 1}})
                else:
                    all_words.update({line[i]: {line[i+1]: 1}})
            elif line[i] in all_words and line[i+1] not in all_words[line[i]]:
                if line[i+1] == line[-1]:
                    all_words[line[i]].update({'.': 1})
                else:
                    all_words[line[i]].update({line[i+1]: 1})
            else:
                all_words[line[i]][line[i+1]]+=1
        line = ' '.join(line)
    fp.close()
    return all_words

#==========================================
# Purpose: Creates a random fanfiction based upon a text file
# Input Parameter(s): fname = a text file filled with strings of single-lined sentences
# Return Value(s): none
#==========================================

def fanfic(fname):

    fp = open(fname, 'r')
    all_first_words = first_words(fname)
    all_next_words = next_words(fname)
    list_of_first_words = []
    
    for key in all_first_words:
        for i in range(all_first_words[key]):
            list_of_first_words.append(key)

    for j in range(10):
        sentence = ''
        next_word = ''
        list_of_next_words = []
        first = random.choice(list_of_first_words)
        sentence += first + ' '
        for key in all_next_words[first]:
            for i in range(all_next_words[first][key]):
                list_of_next_words.append(key)
        next_word = random.choice(list_of_next_words)
        sentence += next_word + ' '

        while next_word != '.':
            list_of_next_words = []
            for key in all_next_words[next_word]:
                for i in range(all_next_words[next_word][key]):
                    list_of_next_words.append(key)
            next_word = random.choice(list_of_next_words)
            sentence += next_word + ' '
        
        print(sentence)
    fp.close()
