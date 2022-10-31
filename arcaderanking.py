import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    
    answer = []
    ranked = list(sorted(set(ranked)))
    
    i , n = 0 , len(ranked)
    
    for p in player:
        while i < n and ranked[i] <= p:
            i += 1
        answer.append(n-i+1)
         
    return answer
        

def main():

    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #ranked_count = int(input().strip())

    ranked = [100 ,100 ,50 ,40 ,40 ,20 ,10]

    #player_count = int(input().strip())

    player = [5 ,25 ,50 ,120]

    result = climbingLeaderboard(ranked, player)

    print(result)

    
main()
