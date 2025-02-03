import ast
import random
import requests
# from SeleniumBase import BaseCase

# wordlist from Schlotes: https://gist.github.com/scholtes/94f3c0303ba6a7768b47583aff36654d

# Inherit BaseCase to gain SeleniumBase functionality
class WordleSolver():   

    def init_words():
        wordlist = []
        with open("wordlist.txt", "r") as f:
            for line in f:
                    wordlist.extend(line.split())
    




# Executes script when ran & prints output in terminal
# if __name__ == "__main__":
    # from pytest import main
    # main([__file__, "-s"])