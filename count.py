import string

def function1(filename):
    with open(filename, 'r')as file:
        text = file.read()
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    return len(words)

filename = 'example.txt'
total_words = function1(filename)
print(f'Total words: {total_words}')
