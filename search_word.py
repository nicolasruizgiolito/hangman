def search_word(word_to_add):
    word_found = False
    with open('words_list.txt', 'r') as f:
        words = f.read().splitlines()
    
    for i in words:
        if i == word_to_add:
            word_found = True

    return word_found
            

