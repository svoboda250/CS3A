"""CS 3A:
Lab Assignment 8: write a program that reads GoldenAge.txt and breaks it into words (strips the white spaces and new line characters).
convert all the words into lower case, count total number of unique words (regardless of the cases) in the poem, and how many times a word is used.
print out in separate lines each word and the number of times it's used. A sample output may look like this:
this : 2
you : 3 """
__author__ = 'Jenny Hamer'


def poem_analysis():
    my_words = dict()
    unique_words = 0
    with open('GoldenAge.txt', 'r') as my_poem:
        for line in my_poem:
            for word in line.split():
                word = word.lower()
                if word not in my_words:
                    my_words[word] = 0
                    unique_words += 1
                if word in my_words:
                    my_words[word] += 1

    for word in my_words:
        print(word, ': ', my_words[word])
    print("There are", unique_words, "unique words in this poem.")


def main():
    poem_analysis()

main()