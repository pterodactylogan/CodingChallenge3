# File: primepantryMDF.py
# Challenge 3: Prime Pantry v2
# Authors: Maddy Fox, Miriam Hodas, Logan Swanson

def prime_pantry(itemDict, nItems, totalWt):
    """Given a dictionary of items and their prices, size of that dictionary,
    and a weight value, returns a list of items that adds up to that weight if
    possible or a message notifying the user that the weight isn't achievable"""
    knownResults = [ "" for e in range(totalWt+1)]

    # Loop over all weight values, in order
    for wt in range(1, totalWt+1):
        
      # Check against each item weight
      for item in [key for key in itemDict if itemDict[key] <= wt]:
            
        # If using the current item lets us reuse a prior result, just update!
        if knownResults[wt-itemDict[item]] != "" or wt-itemDict[item] == 0:

          # Only update if no items repeated
          if item not in get_items(itemDict, knownResults, wt-itemDict[item]):
            knownResults[wt] = item
            
            # Once one solution found, don't need to find others
            break

    if knownResults[totalWt]:
        return get_items(itemDict, knownResults, totalWt)
    else:
        return "No combination of items adds up to ", totalWt

def get_items(itemDict, knownResults, n):
    """Given a weight, returns a list of the items that add up to the weight"""
    lst = []
    
    while n > 0:
      lst.append(knownResults[n])
      n -= itemDict[knownResults[n]]
      
    return lst

def main():
  items = {"pepsi":55,"detergent":30, "chips":25, "cereal":15}
  wt = 100
  #print(prime_pantry(sys.argv[0], sys.argv[1], sys.argv[2]))
  print(prime_pantry(items, len(items), wt))
  
main()
