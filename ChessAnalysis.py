import datetime as dt
import numpy as np

f=open('E:\ChessData.pgn')

dict={'Event':['Blitz'],'Date':[dt.date(2000,1,1)],'White':['eins'],'Black':['zwei'],'Result':[0],'UTCTime':[0],'WhiteElo':[1500],'BlackElo':[1500],'WhiteRatingDiff':[0],'BlackRatingDiff':[0],'TimeControl':['180+0'],'ECO':['A0'],'Termination':['Normal'],'Epoch2000':[0],'RatingMe':[0],'RatingOp':[0]}

for i in range(0,41*500):
    d=f.readline()
    s=d.split()
    try:
        if s[0][1:] in dict.keys():
                if s[0][1:]=='Event':
                    dict['Event'].append(s[2])
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
    except: print(s)

for index,value in enumerate(dict['White'][1:]):
    if value == "gezburger":
        dict['RatingMe'].append(dict['WhiteElo'][index])
        dict['RatingOp'].append(dict['BlackElo'][index])
    else:
        dict['RatingMe'].append(dict['BlackElo'][index])
        dict['RatingOp'].append(dict['WhiteElo'][index])
        
for i in dict.keys():
    dict[i]=dict[i][1:]