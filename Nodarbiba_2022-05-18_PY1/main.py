def get_guessed_letters(word, letters):
    word_with_guessed = ''
    
    for letter in word:
        if letter in letters:
            word_with_guessed += letter
        
        else:
            word_with_guessed += '-'
            
    return word_with_guessed


a = get_guessed_letters("csharp", "r")
print(a)