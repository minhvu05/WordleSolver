def filter_words(word_list, guess, feedback):
    # word_list: list of possible words
    # guess: the word you guessed
    # feedback: feedback string from Wordle, where:
    #   - 'g' = green (correct letter, correct position)
    #   - 'y' = yellow (correct letter, wrong position)
    #   - 'b' = gray (incorrect letter)
    
    filtered_words = []
    
    for word in word_list:
        valid = True
        for i in range(len(guess)):
            if feedback[i] == 'g':  # Correct letter, correct position
                if word[i] != guess[i]:
                    valid = False
                    break
            elif feedback[i] == 'y':  # Correct letter, wrong position
                if word[i] == guess[i] or guess[i] not in word:
                    valid = False
                    break
            elif feedback[i] == 'b':  # Incorrect letter
                if guess[i] in word:
                    valid = False
                    break
        
        if valid:
            filtered_words.append(word)
    
    return filtered_words


word_list = ["CRATE", "SLATE", "PLANE", "GRATE", "BRAVE"]
guess = "CRANE"
feedback = "bbybb"

filtered_list = filter_words(word_list, guess, feedback)
print(filtered_list)