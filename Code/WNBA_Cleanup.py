import csv

## player_ID,Player,year_ID,Age,Tm,tm_gms,Tm_Net_Rtg,Pos,G,MP,MP_pct,PER,TS_pct,ThrPAr,FTr,ORB_pct,TRB_pct,AST_pct,STL_pct,BLK_pct,TOV_pct,USG_pct,OWS,DWS,WS,WS40,Composite_Rating,Wins_Generated

lst = []
with open("wnba-player-stats.csv", 'r') as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        lst.append(row)

playerstat = []
for player in lst:
    if player[2] == "2018":
        playerstat.append(player)
# print(lst2)



lst_sal = []
with open("WNBA_Salaries.csv", 'r') as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        lst_sal.append(row)
# print(lst_sal)
del lst_sal[0]
lst_salaries = []
for player in lst_sal:
    newlist = []
    player[1] = player[1].replace('\xa0', ' ')
    newlist.append(player[1])
    salary = int(player[2])
    if salary > 0:
        newlist.append(player[2])
    lst_salaries.append(newlist)
# print(lst_salaries)
# print(playerstat[0])

for player in playerstat:
    for salary in lst_salaries:
        if salary[0] == player[1]:
#             print(salary)
            if len(salary) > 1:
                player[0] = salary[1]
#             print(player)
print(playerstat)
    