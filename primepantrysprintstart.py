# File: primePantry.py
# Great Python Race: Prime Pantry Problem
# Author: Maddy Fox

import random

def prime_pantry(itemLst, nItems, totalWt):
    itemLst.sort()
    
    # Loop over all wght values, in order
    for wt in range(nItems+1):
        
        # Worst case: no solution
        possible = False
        
        # Check against each item weight
        for j in [i for i in itemLst if c <= wt]:
            
            # If using the current item lets us
            # reuse a prior result, just update!
            if knownResults[wt-j] + i == totalWt:
                possible = False
                
        # Store for use in future computation
        knownResults[wt] = possible
        
    return knownResults[totalWt]

def mod_sort(itemLst, nItems, totalWt):

def main():
  lst = [random.randint(1, 100) for i in range(random.randint(0, 100))]
  print(lst)
  #print(str(prime_pantry(lst, len(lst), 100)))

main()
