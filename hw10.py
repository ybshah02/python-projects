#A
#==========================================
# Purpose: The function returns the score of a word in accordance to the rules of scrabble
# Input Parameter(s): word = string word 
# Return Value(s): total score of each tile in accordance to the rules of scrabble
#==========================================

def scrabble_score(word):

    scores = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1,
              'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1,
              'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1,
              't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10}

    score = 0
    if word == '':
        return 0
    else:
        score += scores[word[0]] + scrabble_score(word[1:])
        return score

#B-part 1
#==========================================
# Purpose: The function finds the greatest common denominator of two numbers
# Input Parameter(s): x = first integer, y = second integer, i = iterator value, temp = temporary greatest common denominator
# Return Value(s): returns the integer number of the greatest common denominator
#==========================================

def gcd(x,y,i,temp):
    num_gcd = temp
    if not i <= x or not i <= y:
        return num_gcd
    else:
        if x%i == 0 and y%i == 0:
            num_gcd = i
        return gcd(x,y,i+1, num_gcd)
#B-part 2
#==========================================
# Purpose: the function determines whether two numbers are relatively prime or not
# Input Parameter(s): x = first integer, y = second integer
# Return Value(s): returns True if the two numbers are relatively prime, returns False if they are not 
#==========================================
      
def relatively_prime(x,y):

    if gcd(x,y,1,0) == 1:
        return True     
    else:
        return False

#C
#==========================================
# Purpose: The function returns a filepath of a file in a directory
# Input Parameter(s): directory = a list of folders, subfolders (represented using nested lists), and files
# Return Value(s): returns the string of the filepath separated by '/' if the file is found; if not, returns False
#==========================================

def find_filepath(directory, filename):
    filepath = ''
    
    for file in directory:
        if file == directory[0] and filename in directory:
            filepath += directory[0] + '/' + filename
            return filepath
    
        elif type(file) == list and filename in find_filepath(file,filename):
            filepath += directory[0] + '/' + find_filepath(file, filename)

    return filepath
