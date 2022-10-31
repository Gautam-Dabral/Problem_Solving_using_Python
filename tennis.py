

def ranking_gen (d, l):

    
    for items in l:
        
        ( winnersets, losersets, winnergames, losergames ) = ( 0, 0, 0, 0 )
        ( winner , loser, setscore ) = ( items[0] , items[1], items[2] )
        
        sets = setscore.split(',')
        for set in sets:
            ( wset, lset ) = ( set.split('-'))
            ( winset , loseset ) = ( int(wset), int(lset) )

            winnergames += winset
            losergames += loseset

            if winset > loseset:
                winnersets += 1
            else:
                losersets += 1
            
        if winnersets >= 3:
            d[winner][0] += 1         # best of 5 sets played, won by the winner
        else:
            d[winner][1] += 1         # best of 3 sets played, won by the winner

        d[winner][2] += winnersets    # sets won by winner of match
        d[winner][3] += winnergames   # games won by winner of match
        d[winner][4] += -losersets    # sets lost by the winner of a match are equal to sets won by the loser
        d[winner][5] += -losergames   # games lost by winner of a match are equal to games won by the loser

        d[loser][2] += losersets      # sets won by the loser of the match
        d[loser][3] += losergames     # games won by the loser of the match
        d[loser][4] += -winnersets    # sets lost by the loser of a match are equal to sets won by the winner
        d[loser][5] += -winnergames   # games lost by the loser of a match are equal to games won by the winner


    rankinglist = []
    for keys in d.keys():
        rankinglist.append( (d[keys][0], d[keys][1], d[keys][2], d[keys][3], d[keys][4], d[keys][5], keys) )
    

    rankinglist.sort(reverse=True)

    for item in rankinglist:
        print(item[-1], item[0], item[1], item[2], item[3], -item[4], -item[5])




def score (l):
    score_lst = {}

    for names in l:
        if names[0] not in score_lst.keys():
            score_lst[names[0]]= [0,0,0,0,0,0]
        elif names[1] not in score_lst.keys():
            score_lst[names[1]]= [0,0,0,0,0,0]

    #print(score_lst)

    return (score_lst)
    


def play_tennis ():
    
    inp_str = input()   #input as a string
    
    inp_lst = []

    while inp_str:
        
        inp_lst.append(inp_str.rstrip().split(':', 2))   #removing \n from the end and spliting :
        
        inp_str=input()

    #print(inp_lst)

    ranking_gen (score (inp_lst), inp_lst)
 

play_tennis()