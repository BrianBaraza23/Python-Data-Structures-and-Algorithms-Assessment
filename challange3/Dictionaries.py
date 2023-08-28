def word_frequency(sentence):
    sentence = sentence.lower()
    
    cleaned_sentence = ""
    for char in sentence:
        if char.isalpha() or char.isspace():
            cleaned_sentence += char
    
    words = cleaned_sentence.split()
    
    frequency_dict = {}
    
    for word in words:
        if word in frequency_dict:
            frequency_dict[word] = frequency_dict[word] + 1
        else:
            frequency_dict[word] = 1
    
    return frequency_dict

sentence = "This is a test sentence. This sentence is a test."

result = word_frequency(sentence)

print(result)
