# Write a program to enter a sentence .From a word by joining all the first characters of each word of the sentence .Display the word

sentence=input('Enter a sentence:')
words= sentence.split()
word="".join(word[0] for word in words)
print("Word is:",word)