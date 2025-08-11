def split_text(textFile):
    words = []
    counter = 0
    
    words = textFile.split()
    
    # for word in words:
    #     counter += 1
    
    # print(f"{counter} words found in the document")
    
    return(words)
    
def count_each_letter(words):
    lowerCaseWords = []
    letterList = []
    cleanedLetters = []
    uniqueLetters = []
    
    letterCounter = 0
    letterDictionary = {}
    
    # Split Words into letters
    for word in words:
        lowerCaseWords.append(word.lower())
        
    # Make each letter a lower casr
    for word in lowerCaseWords:
        for letter in word:
            letterList.append(letter)
    
    # Remove all non-letter characters from the list
    for letter in letterList:
        if(letter.isalpha()):
            cleanedLetters.append(letter)
    
    # Find all unique letters in the text
    uniqueLetters = list(dict.fromkeys(cleanedLetters))
    
    # Count occurance of each letter in the original text 
    for uniqueLetter in uniqueLetters:
        for cleanLetter in cleanedLetters:
            if(cleanLetter == uniqueLetter):
                letterCounter += 1
        
        letterDictionary[uniqueLetter] = letterCounter
        letterCounter = 0
        
    # Return letter dictionary
    return(letterDictionary)
    
def sort_on(items):
    return items["num"]

def dictionary_sorter(letterDictionary):
    sortedLetterDictionary = []
    
    # Create a Key Value pair for each letter and their count
    for letter in letterDictionary:
        sortedLetterDictionary.append({"char": letter, "num": letterDictionary[letter]})
        
    # Sort the letter dictionary
    sortedLetterDictionary.sort(reverse=True, key=sort_on)
    
    # Return the sorted letter dictionary
    return(sortedLetterDictionary)