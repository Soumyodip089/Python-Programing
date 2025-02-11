# Write a program to enter a sentence and display the longest word present in the sentence along with its lenght

sentence = input('Enter a sentence:')
words=sentence.split()
longest_word= ""
max_length=0
for word in words:
    if len(word)>max_length:
        longest_word=word
        max_length=len(word)
        print('Longest word:',longest_word)
        print('Length of longest word',max_length)