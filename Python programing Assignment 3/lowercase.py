#8.Write a program  to accept a sentence in lowercase. Find the frequency of vowels in each word and display the words along with frequency of vowels.

sentence = input("Enter a sentence in lowercase: ")
words = sentence.split()
for word in words:
    vowel_count = sum(1 for char in word if char in 'aeiou')
    print(f"Word: {word}, Vowel Frequency: {vowel_count}")
