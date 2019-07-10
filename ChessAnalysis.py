import datetime as dt
import pandas as pd

f=open('E:\ChessData.pgn')

dict={'Event':['Blitz'],'Date':[dt.date(2000,1,1)],'White':['eins'],'Black':['zwei'],'Result':[0],'UTCTime':[0],'WhiteElo':[1500],'BlackElo':[1500],'WhiteRatingDiff':[0],'BlackRatingDiff':[0],'TimeControl':['180+0'],'ECO':['A0'],'Termination':['Normal'],'Epoch2000':[0],'RatingMe':[0],'RatingOp':[0]}

for line in f:
    s=line.split()
    try:
        if s[0][1:] in dict.keys():
                if s[0][1:]=='Event':
                    dict['Event'].append(s[1][1:]+s[2])
                    if s[1][1:]=='Casual':
                        dict['WhiteRatingDiff'].append(0.1)
                        dict['BlackRatingDiff'].append(0.1)
                elif s[0][1:]=='Date':
                    dict['Date'].append(dt.date(int(s[1][1:5]),int(s[1][6:8]),int(s[1][9:11])))
                elif s[0][1:]=='WhiteElo' or s[0][1:]=='BlackElo' or s[0][1:]=='WhiteRatingDiff' or s[0][1:]=='BlackRatingDiff':
                    if s[1][1:-2]=='?':
                        dict[s[0][1:]].append(0)
                    else:
                        dict[s[0][1:]].append(int(s[1][1:-2]))
                elif s[0][1:]=='Result':
                    dict[s[0][1:]].append(int(s[1][1]))
                elif s[0][1:]=='UTCTime':
                    dict[s[0][1:]].append(int(s[1][1:3])*60*60+int(s[1][4:6])*60+int(s[1][7:9]))
                    dict['Epoch2000'].append((dict['Date'][-1]-dt.date(2000,1,1)).days+dict['UTCTime'][-1]*1./24/60/60)
                else:
                    dict[s[0][1:]].append(s[1][1:-2])
        else:        
                pass                
                #print(s[0][1:])
    except: 
        pass
        #print(s)

for index,value in enumerate(dict['White'][1:]):
    #Replacew with own name.
    if value == "gezburger":
        dict['RatingMe'].append(dict['WhiteElo'][index+1])
        dict['RatingOp'].append(dict['BlackElo'][index+1])
    else:
        dict['RatingMe'].append(dict['BlackElo'][index+1])
        dict['RatingOp'].append(dict['WhiteElo'][index+1])
        
for i in dict.keys():
    dict[i]=dict[i][1:]

df=pd.DataFrame(dict)
df.to_csv('ChessData.csv')
