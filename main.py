import sys

from stats import split_text, count_each_letter, dictionary_sorter

def get_book_text(path_to_file):
    
    with open(path_to_file) as f:
        file_content = f.read()
        
    return(file_content)


def main():
    
    try: 
        path = sys.argv[1]
        file_content = get_book_text(path)
        words = split_text(file_content)
        letterDictionary = count_each_letter(words)
        sortedLetterDictionary = dictionary_sorter(letterDictionary)
        
        letterCount = 0
        
        for letter in words:
            letterCount += 1
        
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {path}...")
        
        print("----------- Word Count ----------")
        print(f"Found {letterCount} total words")
        
        print("--------- Character Count -------")
        for letterPair in sortedLetterDictionary:
            print(f"{letterPair['char']}: {letterPair['num']}")
        
        print("============= END ===============")
        
    except Exception:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

main()