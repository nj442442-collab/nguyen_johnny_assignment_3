text = "Cats and dogs are fun, but cats are definitely funnier than dogs."

def main():
    lower_case = text.lower() #convert letter to lower case
    
    for punctuation in ".,!?;:":
        lower_case = lower_case.replace(punctuation," ") # remove puctuation and space
    
    words = lower_case.split() #split a hold sentence into each word


if __name__ == "__main__":
    main()