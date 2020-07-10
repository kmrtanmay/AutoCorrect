import numpy as np

def delete_letter(word, verbose=False):
    '''
    Input:
        word: the string/word for which we will generate all possible words 
                in the vocabulary which have 1 missing character
    Output:
        delete_l: a list of all possible strings obtained by deleting 1 character from word
    '''
    
    delete_l = []
    split_l = []

    split_l = [(word[:i],word[i:]) for i in range(len(word)+1)]
    delete_l = [ L + R[1:] for L, R in split_l if R ]

    if verbose: print(f"input word {word}, \nsplit_l = {split_l}, \ndelete_l = {delete_l}")

    return delete_l

def switch_letter(word, verbose=False):
    '''
    Input:
        word: input string
     Output:
        switches: a list of all possible strings with one adjacent charater switched
    ''' 
    
    switch_l = []
    split_l = []
    
    split_l = [ (word[:i],word[i:]) for i in range(len(word) + 1) ]
    switch_l = [ L[:-1] + R[0] + L[-1] + R[1:] for L,R in split_l if L and R ]

    if verbose: print(f"Input word = {word} \nsplit_l = {split_l} \nswitch_l = {switch_l}") 

    return switch_l

def replace_letter(word, verbose=False):
    '''
    Input:
        word: the input string/word 
    Output:
        replaces: a list of all possible strings where we replaced one letter from the original word. 
    ''' 
    
    letters = 'abcdefghijklmnopqrstuvwxyz'
    replace_l = []
    split_l = []
    
    split_l = [ (word[:i],word[i:]) for i in range(len(word)+1) ]
    replace_set = [L + C + R[1:] for L,R in split_l if R for C in letters if C is not R[0]]
    
    # turn the set back into a list and sort it, for easier viewing
    replace_l = sorted(list(replace_set))
    
    if verbose: print(f"Input word = {word} \nsplit_l = {split_l} \nreplace_l {replace_l}")   
    
    return replace_l    


def insert_letter(word, verbose=False):
    '''
    Input:
        word: the input string/word 
    Output:
        inserts: a set of all possible strings with one new letter inserted at every offset
    ''' 
    letters = 'abcdefghijklmnopqrstuvwxyz'
    insert_l = []
    split_l = []
    
    split_l = [ (word[:i],word[i:]) for i in range(len(word)+1) ]
    insert_l = [ L + C + R for L,R in split_l for C in letters]

    if verbose: print(f"Input word {word} \nsplit_l = {split_l} \ninsert_l = {insert_l}")
    
    return insert_l    

def edit_one_letter(word, allow_switches = True):
    """
    Input:
        word: the string/word for which we will generate all possible wordsthat are one edit away.
    Output:
        edit_one_set: a set of words with one possible edit.
    """
    
    edit_one_set = set()
    
    if( allow_switches == True):
        edit_one_list = delete_letter(word) + insert_letter(word) + replace_letter(word) + switch_letter(word)
    else:
        edit_one_list = delete_letter(word) + insert_letter(word) + replace_letter(word)
    
    edit_one_set = set(edit_one_list)

    return edit_one_set    

def edit_two_letters(word, allow_switches = True):
    '''
    Input:
        word: the input string/word 
    Output:
        edit_two_set: a set of strings with all possible two edits
    '''
    edit_two_set = set()
    edit_one_list_M = []        
    
    edit_one_set = edit_one_letter(word,allow_switches)
    for word_M in edit_one_set:
        edit_two_set = set.union(edit_two_set,edit_one_letter(word_M,allow_switches))
        #edit_one_list_M += list(edit_one_letter(word_M,allow_switches))
    #edit_two_set = set(edit_one_list_M)
    
    return edit_two_set    