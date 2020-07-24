'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

# we want to figure out the occurences of "th"
# .count method?
# FIRST TRY - .count method works counts all instances of lowercase "th" in (word)
def count_th(word):
    target = "th"

    if len(word) < 2:
        return 0
    # check to see if the beginning of the word is a "th"
    if word[:2] == target:
        return count_th(word[1:]) + 1

    # if not, Iterate over next letter of (word) recursively
    return count_th(word[1:])
    # return word.count("th")
    
    
    
