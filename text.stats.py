text = "Cats and dogs are fun, but cats are definitely funnier than dogs."

def main():
    lower_case = text.lower() #convert letter to lower case
    
    for punctuation in ".,!?;:":
        lower_case = lower_case.replace(punctuation," ") # remove puctuation and space
    
    words = lower_case.split() #split a hold sentence into each word

    print(words)

    unique_word_count = get_unique_word_count(words) #number of word appear without similar word
    print(f"UNIQUE_WORDS: {unique_word_count}")

    longest_word = get_longest_word(words) 
    print(f"LONGEST_WORD: {longest_word}") #print the longest word

    most_common_word = get_most_common_word(words)
    print(f"MOST_COMMON_WORD_COUNT: {most_common_word}")





def get_unique_word_count(words): #find how many unique words appear
    unique_word = set(words)
    return len(unique_word)

def get_longest_word(words): # function for determine the longest word
    longest_word = words[0]
    for word in words:
        if len(longest_word) < len(word):
            longest_word = word
    return longest_word
    
def get_most_common_word(words):
    
    word_count = {} 
    for word in words:#count the number of each word
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    #determine the most common word
    max_word = None
    max_count = 0
    for word, count in word_count.items():
        if count > max_count:
            max_word = word
            max_count = count
    return max_word

if __name__ == "__main__":
    main()