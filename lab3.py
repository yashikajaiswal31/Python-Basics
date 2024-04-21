import string

def remove_punctuation(sentence):
    cleaned_sentence1 = ''.join(char for char in sentence if char not in string.punctuation)
    
    return cleaned_sentence1
user_input1 = input("Enter a sentence: ")
result1 = remove_punctuation(user_input1)
print("Original Sentence:", user_input1)
print("Sentence without Punctuation:", result1)


def remove_punctuation_abbreviations(sentence):
    important_punctuation = {'.', '?', ''}
    cleaned_sentence2 = ''.join(char if char not in string.punctuation or char in important_punctuation else '' for char in sentence)
    
    return cleaned_sentence2
user_input2 = input("Enter a sentence: ")
result2 = remove_punctuation_abbreviations(user_input2)
print("Original Sentence:", user_input2)
print("Sentence without Punctuation (Preserving Some):", result2)

def sort_sentence_alphabetically(sentence):
    words = sentence.split()
    sorted_words = sorted(words)
    sorted_sentence = ' '.join(sorted_words)

    return sorted_sentence

user_input3 = input("Enter a sentence: ")
sorted_result = sort_sentence_alphabetically(user_input3)
print("Original Sentence:", user_input3)
print("Sorted Sentence (Alphabetically):", sorted_result)



