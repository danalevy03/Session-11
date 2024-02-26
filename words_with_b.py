#write a function that takes the name of a text file as a parameter
#print out the 3-letter words that start with "b"

def print_b_words(file_name):

    punctuation = ",.!?'\n\t"
    with open(file_name, "r") as file:
        for line in file:
            for p in punctuation:
                line = line.replace(p,"")
            words = line.split(" ")
            for word in words:
                if (word.startswith("b") or word.startswith("B")) and len(word) == 3:
                    print(word)

print_b_words("bet.txt")