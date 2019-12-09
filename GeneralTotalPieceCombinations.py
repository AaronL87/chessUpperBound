# This algorithm is the first and main expression from my paper "Of Games Greater than Ours:..."

from scipy.special import comb

# A type refers to a kind of piece, including color, with a fixed number of elements.
# For example, if chess had 5 bishops per side for both colors instead of 2.
# This function works for any number of types and number of players (colors).
# "sampleDict" is a dictionary of the form {number of pieces in a type:count of that type,...}

# Choose which "sampleDict" you want to use and comment out the other
# sampleDict = {5:2,3:3,1:5}
sampleDict = {2:6,1:2}

def chessExpress(inputDict):
    num = max(inputDict)
    
    # Computes the sum of a_j for each binom coef
    # This fills in missing a_j values
    # {5:2,3:3,1:5} becomes {5: 2, 3: 5, 1: 10, 4: 2, 2: 5}
    for val in range(num-1,0,-1):
        try:
            inputDict[val] += inputDict[val+1]
        except:
            inputDict[val] = inputDict[val+1]
    print(inputDict)
    
    # Sorts items of dictionary in descending order by the largest key (number of type)
    sortDict = sorted(inputDict.items(),reverse=True,key=lambda a:a[0])
    print(sortDict)

    # A recursive function that goes down the binom coefs taking the product
    # Once it hits the last binom coef, it keeps a sum tally
    # Each series is limited by the indices, i, of the series before it
    counter, combSum = recurFunc(sortDict)
    print("Answer:", combSum)

# "counter" determines which binom coef we are at
# "k" is the sum of the previous indices, i, of the previous series 
# "comProd" keeps a tally of the product of one iteration of all binom coefs
# "combSum" keeps a tally of the sums of each iteration through all binomail coefficients
def recurFunc(sortDict,counter=0,k=0,combProd=1,combSum=0):       
    reset = combProd # Keeps track of product from previous binom coef
    for i in range(sortDict[counter][1]+1-k): # "k" is subtracted here for speed
        
        # "k" is subtracted here because each binom coef is limited by the indices of all prior series 
        combProd *= comb(sortDict[counter][1]-k,i) 
        
        # Counts all the way down to the last binomial coeffienct
        if counter < len(sortDict)-1:
            counter += 1
            counter, combSum = recurFunc(sortDict,counter=counter,k=i,combProd=combProd,combSum=combSum)
        
        # only keeps track of sum when at last binom coef
        else:
            combSum += combProd
        
        # resets product after reaching last binom coef and adding that product to sum tally
        combProd = reset

    # The counter keeps track of which binom coef we are at, so we need to subtract 1 before returning
    counter -= 1        
    return counter, combSum


chessExpress(sampleDict)

'''
Output:
{2: 6, 1: 8}
[(2, 6), (1, 8)]
Answer: 2916.0
'''

# To test this function, I compared its output to the corresponding part from upperBound.py:

def sumChecker():
    total = 0
    for z in range(0,6+1):
        for y in range(0,8-z+1):                
            pieceCount = comb(6,z)*comb(8-z,y)
            total += pieceCount     
    print("Answer:",total)

sumChecker()

'''
Output:
Answer: 2916
'''

