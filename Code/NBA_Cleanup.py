import csv

## Player,Pos,Age,Tm,G,MP,PER,TS%,3PAr,FTr,ORB%,DRB%,TRB%,AST%,STL%,BLK%,TOV%,USG%,OWS,DWS,WS,WS/48,OBPM,DBPM,BPM,VORP

lst = []
with open("nba.csv", 'r') as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        lst.append(row)

# players_2018 = []
# for player in lst:
#     if player[2] == "2019":
#         players_2018.append(player)
# # print(players_2018)

for row in lst:
    row[1] = row[1].split('\\')[0]
#     print(row[1])
salary_lst = []
with open("nba-salaries.csv", 'r') as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        if row[-1] == "2019":
            salary_lst.append(row)
# print(salary_lst)

apended_list = []
for player in lst:
    for salary in salary_lst:
        if player[1] == salary[1]:
            player[0] = salary[-2]
            apended_list.append(player)
# print(apended_list)
# my_str = "Alex Abrines\abrinal01"
# result = my_str.split('\\')
# print(result)

i = 0
while i < len(apended_list):
    if apended_list[i][4] == "TOT":
        name = apended_list[i][1]
        j = 0
        while j < 4:
            if apended_list[i+j][1] == name:
                del apended_list[i+j]
            j += 1
    i += 1
            
print(apended_list)

header = ['Salary','Player','Pos','Age','Tm','G','MP','PER','TS%','3PAr','FTr','ORB%','DRB%','TRB%','AST%',
          'STL%','BLK%','TOV%','USG%','OWS','DWS','WS','WS/48','OBPM','DBPM','BPM','VORP']

for player in apended_list:
    while("" in player):
        player.remove("")
          
for player in apended_list:
    if int(player[5]) < 10:
        apended_list.remove(player)     
          
with open('NBA_Combined.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for row in apended_list:
        writer.writerow(row)

# header = ['Player_Salary','Player','year_ID','Age','Tm','tm_gms','Tm_Net_Rtg','Pos','G','MP','MP_pct','PER',
#           'TS_pct','ThrPAr','FTr','ORB_pct','TRB_pct','AST_pct','STL_pct','BLK_pct','TOV_pct','USG_pct','OWS',
#           'DWS','WS','WS40','Composite_Rating','Wins_Generated']
