import random

def yahtzeeMonteCarlo(numTrials):
    die = [1,2,3,4,5,6]

    yahtzeeCnt = 0;
    
    for i in xrange(numTrials):
        sequence = []
        yahtzee = True
        for j in xrange(5):
            roll = random.choice(die)
            sequence.append(roll)
            if j > 0 and sequence[j] != sequence[j-1]:
                yahtzee = False
                break;
        if yahtzee:
            yahtzeeCnt +=1
    return float(yahtzeeCnt)/numTrials

print yahtzeeMonteCarlo(1000000)
        
        
        
    
    
