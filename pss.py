# Python 

import re

# String to modify
ncsa = "National Center for Supercomputers Applications"

# alpha list
alpha = "abcdefgjijklmnopqrstuvwxyz"

# vowels and consonants
vowels = "aeiou"
vowels_pattern = re.compile('['+vowels+']', re.IGNORECASE)
consonants = re.sub(vowels_pattern, "", alpha)
consonants_pattern = re.compile('[^'+consonants+']', re.IGNORECASE)

# get vowel's numeric value from the alpha list (and add 1 to the index)
def vowel_to_number(vowel):
  number = alpha.index(vowel.lower())
  return str(number + 1) if number >= 0 else 0

# modify the string
def modify_string(mstring):
  return "".join([vowel_to_number(character) if re.match(vowels_pattern, character) else character for character in mstring])

# count the consonants
def consonant_count(cstring):
  return len(re.sub(consonants_pattern, "", cstring))

# show the modified string
print(modify_string(ncsa))

# show the number of consonants
print(consonant_count(ncsa))

