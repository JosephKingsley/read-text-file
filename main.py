# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
    with open(filename, 'r') as f:
        file = f.read()
    
    return file


output = read_file_content('story.txt')
print(output)

    
def count_words():

    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    words = text.split()
    word_count = {}
    for word in words:
        word.lower()
        if word in word_count:
             word_count[word] +=1
        else:
            word_count[word] = 1

    print(word_count)

    return{"as":10, "would": 20}
count_words()

