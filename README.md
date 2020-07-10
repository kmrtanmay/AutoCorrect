# AutoCorrection
Autocorrection is a technique to give auto-suggestions to the users for the corrections of the mispelled word. **Autocorrection**, also known as **text replacement**, **replace-as-you-type** or simply **autocorrect**, is an automatic [data validation function](https://en.wikipedia.org/wiki/Data_validation "Data validation") commonly found in [word processors](https://en.wikipedia.org/wiki/Word_processor "Word processor") and text editing interfaces for [smartphones](https://en.wikipedia.org/wiki/Smartphone "Smartphone") and [tablet computers](https://en.wikipedia.org/wiki/Tablet_computer "Tablet computer"). Its principal purpose is as part of the [spell checker](https://en.wikipedia.org/wiki/Spell_checker "Spell checker") to correct common spelling or typing errors, saving time for the user. It is also used to automatically [format](https://en.wikipedia.org/wiki/Typesetting "Typesetting") text or insert special characters by recognizing particular character usage, saving the user from having to use more tedious function

![alt text](auto-correct.png)
### DataSet : Shakespeare literary text

### Model : 
- First, a vocabulary is constructed from the shakespeare text using python set for storing all the unique words.
- A dictionary is created for storing each frequency of each word in the corpus. Similarly, another dictionary is also created for storing the probablity of occurence of each word. Second dictionary is useful as it provides the best words on the basis of probablity of occurance.
- Then editing operations(deleting, inserting, replacing, switching) are performed on the word for extracting the similar words which are stored in the lists.
- Single Letter edit on the word as well as Two letters edit operations( Single letter edit on the modified words obtained from the list of single letter edit operation on a word) are done to get all words to be suggested.
- Some of the words which are not present in the vocabulary set are avoided.
- Now, on the basis of probablity of their occurences , N number of words are extracted from suggested list of words.