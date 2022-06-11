# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
    read_file = open("./story.txt", "r")
    file_content = read_file.read()
    print("This file is valid")
    return file_content

def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    textsplit = text.split()

    textcount = {}
    for i in textsplit:
        if i in textcount:
            textcount[i] +=1
        else:
            textcount[i] =1
    return textcount

  #  return {"as": 10, "would": 20}
print(count_words())
