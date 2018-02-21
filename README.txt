# CodingChallenge3
# Authors: Logan Swanson, Maddy Fox, Miriam Hodas

primepantry.py runs with python3. It gets arguments from the command line.
To run:
> python3 primepantry.py "{'key':value,...,'key':value}" numItems total
where numItems is the integer length of the dictionary and total is the total weight 
you are trying to fill.

Our program is more efficient than enumerating all possible combinations.
We use dynamic programming to store the results for each combination of items that
adds to every weight smaller than total weight. By looping though each item less than weight
we test if we can build on previous combinations to meet the current weight.

Our program gives the closest combination of items if no combination adds to total weight.

We check that the function is passed a dictionary and two integers, and that dictionary has
string keys and integer values.
