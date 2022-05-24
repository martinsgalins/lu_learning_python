import random
error_count_0 = (f"-+-----+\n"
                    f" |     |\n"
                    f"       |\n"
                    f"       |\n"
                    f"       |\n"
                    f"       |\n"
                    f"===========")
error_count_1 = (f"-+-----+\n"
                    f" |     |\n"
                    f" O     |\n"
                    f"       |\n"
                    f"       |\n"
                    f"       |\n"
                    f"===========")
error_count_2 = (f"-+-----+\n"
                    f" |     |\n"
                    f" O     |\n"
                    f" |     |\n"
                    f"       |\n"
                    f"       |\n"
                    f"===========")
error_count_3 = (f"-+-----+\n"
                    f" |     |\n"
                    f" O     |\n"
                    f"/|     |\n"
                    f"       |\n"
                    f"       |\n"
                    f"===========")
error_count_4 = (f"-+-----+\n"
                    f" |     |\n"
                    f" O     |\n"
                    f"/|\    |\n"
                    f"       |\n"
                    f"       |\n"
                    f"===========")
error_count_5 = (f"-+-----+\n"
                    f" |     |\n"
                    f" O     |\n"
                    f"/|\    |\n"
                    f"/      |\n"
                    f"       |\n"
                    f"===========")
error_count_6 = (f"-+-----+\n"
                    f" |     |\n"
                    f" O     |\n"
                    f"/|\    |\n"
                    f"/ \    |\n"
                    f"       |\n"
                    f"===========")


def get_guessed_letters(word, letters):
    word_with_guessed = ''
    
    for letter in word:
        if letter in letters:
            word_with_guessed += letter
        else:
            word_with_guessed += '-'       
    return word_with_guessed


words = ["lemon", "smartphone"]
lenght  = len(words)
random_number = random.randint(0,lenght-1)
word = words[random_number]

x = 0
while x != 3:
    print("Enter 1 to play hangman, 2 to add a new word, 3 to quit program.")
    a = int(input("Enter number:"))

    if a == 1:
        error_count = 0
        guessed_letters = []
        print(error_count_0)
        print("Guessed letters:", guessed_letters)
        print(get_guessed_letters(word, guessed_letters))
        while error_count < 6:
            output_image = lambda: str('error_count_') + str(error_count)
            d = str(input("Enter letter:"))
            if d in word:
                guessed_letters.append(d)
                display_image = output_image()
                print(f"{str(display_image)}")
                print("Guessed letters:",guessed_letters)
                print(get_guessed_letters(word, guessed_letters))
            else:
                error_count += 1
                guessed_letters.append(d)
                print(output_image())
                print("Guessed letters:",guessed_letters) 
                print(get_guessed_letters(word, guessed_letters)) 
    elif a == 2:
        new_word = int(input("Enter word:"))
        words.append(new_word)
        print("Word added to list!")
    elif a == 3:
        x = a
        quit  
    else:
        print("Choise out of range!")
        continue  

       