# Wordle Solver without Selenium
# Mainly for testing logic

import ast
import random
import requests

class WordleSolver():

    def initialize_wordlist():
        wordlist = []
        with open("wordlist.txt", "r") as f:
            for line in f:
                wordlist.extend(line.split())

        return wordlist

    def body():      
        # Answer for testing purposes
        ans = "story"
        # Test cases: STORY, RAPID, ARBOR, SWISS

        # Initialize wordlist
        wordlist = initialize_wordlist()
        updated = []
        

        # Will always be first word
        guess = "soare"
        
        # Status for printing purposes
        status_map = {"correct" : 2,
                    "present" : 1,
                    "absent" : 0}
        
        # Arrays for correct/present letters
        correct = []
        present = []
        absent = []
        
        # TODO: eventually loop and change print to "Guess #(number)"
        print("First Guess: " + guess.upper())
        for word in wordlist:
            for pos in range(len(guess)):
                if guess[0:pos+1] == ans[0:pos+1]:
                    print(f"Guess So Far: {guess[0:pos]} - Word So Far: {word[0:pos]}")
                    correct.append(word)
                #elif 
    
        print(f"Correct: {correct}")
        print(f"Present: {present}")
        print(f"Absent: {absent}")
        print(f"Updated List: {updated}")


