# File: primePantryMDF.py
# Great Python Race: Prime Pantry Problem
# Author: Maddy Fox

#import random

def prime_pantry(itemDict, nItems, totalWt):
    #invDict = {v:k for k,v in itemDict.items()}
    knownResults = [ "" for e in range(totalWt+1)]

    for key in itemDict:
      knownResults[itemDict[key]] = key
    
    # Loop over all weight values, in order
    for wt in range(1, totalWt+1):
      #print("weight: ", wt)
        
      # Check against each item weight
      for item in [key for key in itemDict if itemDict[key] <= wt]:
        #print("item: ", item)
            
        # If using the current item lets us
        # reuse a prior result, just update!
        if knownResults[wt-itemDict[item]] != "":
          print("last result for ", wt, " - ", item, " : ", knownResults[wt-itemDict[item]])

          #only update if no items repeated
          if item not in knownResults[wt-itemDict[item]]:
            print("no repeats")
            knownResults[wt] = item
            #once solution found, don't need to check others
            break
            
        #print("known result for ", wt, " : ", knownResults[wt])
        
    finalLst = []
    n = totalWt
    while n > 0:
      finalLst.append(knownResults[n])
      n -= itemDict[knownResults[n]]

    return finalLst

def main():
  items = {"pepsi":55,"detergent":30, "chips":25, "cereal":15}
  print(prime_pantry(items, len(items), 100))

main()
