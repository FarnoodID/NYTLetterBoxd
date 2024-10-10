import os
# cwd =  os.getcwd()
cwd = os.path.dirname(os.path.abspath(__file__))
cwd = cwd + '\\'
print("Opening file at \'"+cwd+"\'")
with open(cwd+'words.txt','r') as f:
    words = f.readlines()

def checkSide(side,word):
    n = len(side)
    for numLetter1 in range(0,n):
        for numLetter2 in range(numLetter1,n):
            sub1 = side[numLetter1]+side[numLetter2]
            sub2 = side[numLetter2]+side[numLetter1]
            # print("sub1:",sub1,"sub2:",sub2)
            if sub1 in word or sub2 in word:
                return False
    return True

def remainOfLetters(rowOfWords,letters):
    for word in rowOfWords:
        for letter in word:
            if letter in letters:
                letters.remove(letter)
    return len (letters)

print("Enter letters of each side in a seperate line:")
side1 = list(input())
side2 = list(input())
side3 = list(input())
side4 = list(input())
letters = []
for i in side1:
    letters.append(i)
for i in side2:
    letters.append(i)
for i in side3:
    letters.append(i)
for i in side4:
    letters.append(i)
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for letter in letters:
    if letter in alphabet:
        alphabet.remove(letter)

for i, word in enumerate (words):
    if (i+1 != len(words)):
        words[i] = word[:-1]
    
tempWords =[]    
for word in words:
    has_other_letters = False
    for letter in alphabet:
        if letter in word:
            has_other_letters = True
            break
    if has_other_letters == False:
        tempWords.append(word)
words = tempWords.copy()

newWords = []
for word in words:
    if len(word)>2 and checkSide(side1,word) and checkSide(side2,word) and checkSide(side3,word) and checkSide(side4,word):
        newWords.append(word)
words = newWords.copy()

counter=0
print("Available words are:")
for lineOfWords in words:
    counter+=1
    print(str(counter)+". "+lineOfWords)


while True:
    counter=0
    searchFor = input('Enter the letter to search for: ')
    for lineOfWords in words:
        if lineOfWords[0] == searchFor:
            counter+=1
            print(str(counter)+". "+lineOfWords)