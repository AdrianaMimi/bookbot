def number_of_letters(file_contents):
    split_contents = file_contents.split()
    list_of_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'æ', 'â', 'ê', 'ë', 'ô']
    return_dictionary = {}    
    for letter in list_of_letters:
        letter_number = 0
        for word in split_contents:
            for character in word:
                if character.isalpha() == True:
                    if letter == character.lower():
                        letter_number +=1
            return_dictionary[letter] = letter_number                 
    return return_dictionary

def number_of_words(file_contents):
    split_contents = file_contents.split()             
    return len(split_contents)



