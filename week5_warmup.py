# Problem Set 1: Indexing and Slicing Strings
# Basic Indexing:
# Given the string magic = 'abracadabra',
# a. Retrieve the 5th character.
text = 'abracadabra '
print(text[4])
# b. Retrieve the second to last character.
print(text[9])
# c. Find the first occurrence of the letter 'c'.
print(text.find('c'))


# Advanced Slicing:
# Given the string alphabet = 'abcdefghijklmnopqrstuvwxyz',
alphabet = 'abcdefghijklmnopqrstuvwxyz'
# a. Extract the letters 'hij'.
print(alphabet[7:10])
# b. Extract every second letter starting from 'a' to 'm'.
print(text[0:])
# c. Reverse the entire string using slicing.
print(alphabet[::-1])
# Problem Set 2: Extracting Information
# From Descriptions:
# Extract the name of the famous personality from the quote "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
quote = "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy" 
print(quote.find('John F. Kennedy'))
print(quote[83:98])
# Manipulating Words:
# Given the string info = "Python is fun. Fun is good. Good is subjective.",
# a. Extract the word 'subjective' without knowing its exact position.
print

# b. Extract every third word.
print(quote[::3])
# c. Reverse the positions of the words, but keep the characters in each word in the same order.
info = "Python is fun. Fun is good. Good is subjective."
words = info.split()

# Problem Set 3: String Methods
# Upper & Lower:
# Convert the following text to lowercase: "MAY THE FORCE BE WITH YOU."
sentence = "MAY THE FORCE BE WITH YOU."
print(sentence.lower()))
# String Joining and Splitting:
# Given the list motto = ["Make", "haste", "slowly."],
motto = ["Make", "haste", "slowly."]
# a. Convert the list into a single string.
joined_string = " ".join(motto)
print(joined_string)
# b. Now, split the string at every occurrence of the letter 'a'.
split_string = joined_string.split('a')
print(split_string)
# Replacing Words:
# Modify the sentence: "Life is what happens when you are busy making other plans."
sentence = "Life is what happens when you are busy making other plans."
# a. Replace "busy" with "distracted".
modified_sentence = sentence.replace("busy", "distracted")
print(modified_sentence)
# b. Replace "plans" with "mistakes".
modified_sentence = modified_sentence.replace("plans", "mistakes")
print(modified_sentence)
# Problem Set 4: String Properties and Advanced Operations
# Repetition:
# Concatenate the word "Iteration" 7 times.
repeated_word = "Iteration" * 7
print(repeated_word)
# Word Search:
quote = "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"
contains_moonlight = "moonlight" in quote
print(contains_moonlight)
# Check if the word "moonlight" appears in the quote: "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"

# Length and Count:
phrase = "Supercalifragilisticexpialidocious"
num_characters = len(phrase)
print(num_characters)
# a. Calculate the number of characters (including spaces and punctuation) in the word/phrase: "Supercalifragilisticexpialidocious".
count_i = phrase.count('i')
print(count_i)
# b. Count the number of times the letter 'i' appears in the same word/phrase.