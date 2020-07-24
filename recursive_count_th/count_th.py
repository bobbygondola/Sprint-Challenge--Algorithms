'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

# we want to figure out the occurences of "th"
# .count method?
# FIRST TRY - .count method works counts all instances of lowecase "th" in (word)
def count_th(word):
    # count = word.count("th")
    # if count > 0:
    #     return count
    # else:
    #     return count_th(word)
    return word.count("th")
    
    
    
