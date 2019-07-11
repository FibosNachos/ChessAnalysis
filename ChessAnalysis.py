import datetime as dt
import pandas as pd
import numpy as np

f=open('E:\ChessData.pgn')

dict={'Number':[],'GameData':[],'Event':[],'Date':[],'White':[],'Black':[],'Result':[],'UTCTime':[],'WhiteElo':[],'BlackElo':[],'WhiteRatingDiff':[],'BlackRatingDiff':[],'TimeControl':[],'ECO':[],'Termination':[],'Epoch2000':[],'RatingMe':[],'RatingOp':[],'RatingDiffMe':[],'RatingDiffOp':[]}

GD=True
for index,line in enumerate(f): 
    s=line.split()
    try:    
        if s[0][1:] in dict.keys():
                if s[0][1:]=='Event':
                    if not GD: dict['GameData'].append(np.nan)
                    dict['Event'].append(s[1][1:]+s[2])
                    dict['Number'].append(index)
                    GD=False
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
                if s[0][0] in ['1','2','3','4','5','6','7','8','9''0']:
                    dict['GameData'].append(line)
                    GD=True
                else: pass                   
    except: 
        pass        
        #print(s)

for index,value in enumerate(dict['White']):
    if value == "gezburger":
        dict['RatingMe'].append(dict['WhiteElo'][index])
        dict['RatingOp'].append(dict['BlackElo'][index])
        dict['RatingDiffMe'].append(dict['WhiteRatingDiff'][index])
        dict['RatingDiffOp'].append(dict['BlackRatingDiff'][index])
    else:
        dict['RatingMe'].append(dict['BlackElo'][index])
        dict['RatingOp'].append(dict['WhiteElo'][index])
        dict['RatingDiffMe'].append(dict['BlackRatingDiff'][index])
        dict['RatingDiffOp'].append(dict['WhiteRatingDiff'][index])
        

df=pd.DataFrame(dict)
df.to_csv('ChessData.csv')
