#5.Write a program to accept a sentence. Display the sentence in reverse order of its words

Sen = input('Enter a sentence:')
words= Sen.split()
reversed_words = words[::-1]
reversed_sen = " ".join(reversed_words)
print('Reversed sentence:',reversed_sen)