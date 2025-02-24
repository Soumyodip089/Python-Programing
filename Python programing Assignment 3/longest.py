#7.Write a program to enter a sentence and display the longest word present in the sentence along with its lenght

sentence = input("Enter a sentence: ")
words = sentence.split()
longest_word = max(words, key=len)
print("Longest word:", longest_word)
print("Length of longest word:", len(longest_word))