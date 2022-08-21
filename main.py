#!/usr/bin/python3
import csv
from sys import argv

csv_file = "/usr/local/bin/nato/nato_alphabet.csv"
nato_list = []

if len(argv)==1:
    print("Provide word")
    quit()

with open(csv_file, newline='') as f:
    reader = csv.reader(f)
    nato_list = list(reader)
    print(nato_list)

def find_letter_in_nato_alph(letter):
    found = False
    for l in nato_list:
        if l[0] == letter.upper():
            found = True
            return l[1]
    if not found:
        return letter

def word_spelled_in_nato_alph(word):
    word_nato = []
    letter_list = list(word)
   # word_nato.append()
    for letter in letter_list:
        letter_nato = find_letter_in_nato_alph(letter)
        word_nato.append(letter_nato)
    return word_nato

def nato_spell():
    for word in argv[1:]:
        print(word)
        word_nato = word_spelled_in_nato_alph(word)
        print(" , ".join(str(x) for x in word_nato))
        print()

nato_spell()
