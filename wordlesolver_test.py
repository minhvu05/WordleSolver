# Wordle Solver without Selenium
# Mainly for testing logic

import ast
import random
import requests

class WordleSolver():
    # Answer for testing purposes
    answer = "surge"
    answer_arr = list(answer)
    # Test cases: All letters different, More than 1 same letter

    # Initialize wordlist
    wordlist = []
    with open("wordlist.txt", "r") as f:
        for line in f:
                wordlist.extend(line.split())

    # Will always be first word
    word = "soare"
    word_arr = list(word)
    
    # Status for printing purposes
    status_map = {"correct" : 2,
                  "present" : 1,
                  "absent" : 0} # find synonym so it aligns lol
    
    # Arrays for correct/present letters
    correct = []
    present = []
    absent = []
    
    # eventually loop and change print to "Guess #(number)"
    print("First Guess: " + word.upper())
    for i in range(len(word)):
        if(word_arr[i] == answer_arr[i]):
            correct.append(word[i])
        elif(word_arr[i] in answer_arr):
             present.append(word[i])
        else:
             absent.append(word[i])
    print(correct)
    print(present)
    print(absent)

            


