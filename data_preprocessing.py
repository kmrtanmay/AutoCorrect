import re
import numpy as np

#1) Reads in a corpus (text file)
#2) Changes everything to lowercase
#3) Returns a list of words.

def process_data(file_name):
    """
    Input: 
        A file_name which is found in your current directory. We just have to read it in. 
    Output: 
        words: a list containing all the words in the corpus (text file read) in lower case. 
    """
    words = [] 

    with open(file_name) as f:
        data = f.read()
        words = re.findall('\w+',data)
        words = [word.lower() for word in words]
    
    return words
