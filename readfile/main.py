# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
    with open(filename) as f:
        contents = f.read()
        # print(contents)
        return contents

# print(read_file_content('story.txt'))


def count_words():
    text = read_file_content('story.txt')
    wrds = text.split()
    count = dict()
    for words in wrds:
        if words in count:
            count[words] += 1
        else:
            count[words] = 1

    return count