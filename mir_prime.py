# primepantry.py
# Authors: Logan Swanson, Maddy Fox, Miriam Hodas
# Due: February 22 2018
# Takes in a list of items and their positive integer weights,
# number of items, and total weight
# Returns a subset of items with weight equal to total weight

def primePantry(itemDict, numItems, totalWeight):
    # Loop over all weights up to totalWeight, in order
    knownResults = [""]*(totalWeight+1)
##    accumWt = 0
    for weight in range(totalWeight+1):
##        print(weight)
        # Check each value that is not greater than weight
        for j in [key for key in itemDict if itemDict[key]<= weight]:
  ##          print("key: ", j)
            if itemDict[j] == weight:
                knownResults[weight] = j
  ##              accumWt = weight
    ##            print("Updated knownResults: ", knownResults[weight])
            elif j not in knownResults[weight-itemDict[j]] and knownResults[weight-itemDict[j]] != "":
                knownResults[weight] = knownResults[weight-itemDict[j]]+j
    ##            accumWt = weight
      ##          print("Updated knownResults: ", knownResults[weight])
    return knownResults[totalWeight]

def main():
    itemDict = {"pepsi":55, "detergent":30, "chips":25, "cereal":15}
    itDict = {"twenty":20, "twenty2":20, "forty":40, "eighty":80}
    numItems = len(itDict)
    totalWeight = 100
    print(primePantry(itDict, numItems, totalWeight))


main()
