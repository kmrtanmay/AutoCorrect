import re
from collections import Counter
import numpy as np
import pandas as pd
import string

from data_preprocessing import process_data
from utils import vocabulary, get_count, get_probs, get_corrections
from edit_letters import delete_letter, insert_letter, replace_letter, switch_letter, edit_one_letter, edit_two_letters

# Data Preprocessing
word_l = process_data('shakespeare.txt')

# Building the vocabulary set having unique words
vocab = vocabulary(word_l)

# Building a dictionary where
# The dictionary's keys are words
# The value for each word is the number of times that word appears in the corpus.
word_count_dict = get_count(word_l)

# Building a dictionary
# The dictionary's keys are words
# The value for each word is the probablity of occurence of each word in the corpus.
probs = get_probs(word_count_dict)

# Test your implementation 
print('enter a word')
my_word = input()
Num_suggestions = int(input()) 
tmp_corrections = get_corrections(my_word, probs, vocab,Num_suggestions, verbose=True)
for i, word_prob in enumerate(tmp_corrections):
	print(word_prob[1])
	print(f"word {i}: {word_prob[0]}, probability {word_prob[1]:.6f}")
    
print(f"data type of corrections {type(tmp_corrections)}")

