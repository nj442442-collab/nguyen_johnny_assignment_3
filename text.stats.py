text = "Cats and dogs are fun, but cats are definitely funnier than dogs."

def main():
    lower_case = text.lower() #convert letter to lower case
    
    for punctuation in ".,!?;:":
        lower_case = lower_case.replace(punctuation," ") # remove puctuation and space
    
    words = lower_case.split() #split a hold sentence into each word

    print(words)

    unique_word_count = get_unique_word_count(words)
    print(f"UNIQUE_WORDS: {unique_word_count}")

    longest_word = get_longest_word(words)
    print(f"LONGEST_WORD: {longest_word}")



def get_unique_word_count(words): #find how many unique words appear
    unique_word = set(words)
    return len(unique_word)

def get_longest_word(words): # function for determine the longest word
    longest_word = words[0]
    for word in words:
        if len(longest_word) < len(word):
            longest_word = word
    return longest_word
    


if __name__ == "__main__":
    main()