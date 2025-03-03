'''
Task_03 :
Take any sentence from the user as input and reverse the order of words without using any predefined function.
'''
sentence = input("Enter a sentence: ")
words = sentence.split()  # Split sentence into words
reversed_sentence = ' '.join(reversed(words))  # Reverse the order of words and join them back into a string
print(reversed_sentence)