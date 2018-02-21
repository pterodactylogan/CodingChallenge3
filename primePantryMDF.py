# File: primepantryMDF.py
# Challenge 3: Prime Pantry v2
# Authors: Maddy Fox, Miriam Hodas, Logan Swanson
# Date Due: February 22, 2018

def prime_pantry(itemDict, nItems, totalWt):
    """Given a dictionary of items and their prices, size of that dictionary,
    and a weight value, returns a list of items that adds up to that weight if
    possible or a message notifying the user that the weight isn't achievable"""
    
    #check validity of input
    if type(itemDict)!=dict: raise TypeError
    if type(nItems)!=int: raise TypeError
    if type(totalWt)!=int: raise TypeError
    if nItems!=len(itemDict): raise ValueError
    
    for key in itemDict:
        if type(key)!=str: raise TypeError
        if key=="": raise ValueError
        if type(itemDict[key])!=int: raise TypeError
        if itemDict[key]<0: raise ValueError
    
    knownResults = [ "" for e in range(totalWt+1)]
    best_weight=-1

    # Loop over all weight values, in order
    for wt in range(1, totalWt+1):
        
      # Check against each item weight
      for item in [key for key in itemDict if itemDict[key] <= wt]:
            
        # If using the current item lets us reuse a prior result, just update!
        if knownResults[wt-itemDict[item]] != "" or wt-itemDict[item] == 0:

          # Only update if no items repeated
          if item not in get_items(itemDict, knownResults, wt-itemDict[item]):
            knownResults[wt] = item
            best_weight=wt
            
            # Once one solution found, don't need to find others
            break
        
    result=get_items(itemDict,knownResults,best_weight)
    if not result=="": 
        print("Items adding to "+str(best_weight))
        return result
    else: 
        print()
        return []

def get_items(itemDict, knownResults, n):
    """Given a weight, returns a list of the items that add up to the weight"""
    lst = []
    
    while n > 0:
      lst.append(knownResults[n])
      n -= itemDict[knownResults[n]]
      
    return lst

def main():
    items = ast.literal_eval(sys.argv[1])
    nItems = sys.argv[2]
    total = sys.argv[3]
    print(prime_pantry(items, nItems, total))
  
main()
