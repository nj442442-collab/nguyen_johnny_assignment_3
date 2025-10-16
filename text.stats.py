text = "Cats and dogs are fun, but cats are definitely funnier than dogs."

def main():
    lower_case = text.lower()
    for punctuation in ".,!?;:":
        lower_case.replace(punctuation," ")
    split_words = lower_case.split()


if __name__ == "__main__":
    main()