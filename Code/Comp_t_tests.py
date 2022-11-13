import numpy as np
import matplotlib.pyplot as plt
import csv
from scipy import stats
import statistics

readNBA = []
with open("NBA_Combined.csv", 'r') as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        readNBA.append(row)
        
readWNBA = []
with open("WNBA_Combined.csv", 'r') as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        readWNBA.append(row)

# WNBAheader = ['Player_Salaryy','Player','year_ID','Age','Tm','tm_gms','Tm_Net_Rtg','Pos','G','MP','MP_pct','PER',
#           'TS_pct','ThrPAr','FTr','ORB_pct','TRB_pct','AST_pct','STL_pct','BLK_pct','TOV_pct','USG_pct','OWS',
#           'DWS','WS','WS40','Composite_Rating','Wins_Generated']

# NBAheader = ['Salary','Player','Pos','Age','Tm','G','MP','PER','TS%','3PAr','FTr','ORB%','DRB%','TRB%','AST%',
#           'STL%','BLK%','TOV%','USG%','OWS','DWS','WS','WS/48','OBPM','DBPM','BPM','VORP']

wnba_sal = []
nba_sal = []
for player in readWNBA[1:]:
    wnba_sal.append(float(player[0]))
for player in readNBA[1:]:
    nba_sal.append(float(player[0]))
avg_wnba = sum(wnba_sal)/len(wnba_sal)
median_wnba = statistics.median(wnba_sal)
avg_nba = sum(nba_sal)/len(nba_sal)
median_nba = statistics.median(nba_sal)
# print(avg_wnba)
# print(avg_nba)
base_result = stats.ttest_ind(nba_sal, wnba_sal)
print("Independent T-Test result for comparing base NBA and WNBA salaries: ")
print(base_result[0])

prop_wnba_sal = []
prop_nba_sal = []
for salary in wnba_sal:
    sal = salary / 60000000
    prop_wnba_sal.append(sal)
for salary in nba_sal:
    salary = salary / 8010000000
    prop_nba_sal.append(sal)

# print(prop_wnba_sal[0:10])
# print(prop_nba_sal[0:10])
prop_result = stats.ttest_ind(prop_nba_sal, prop_wnba_sal)
print("Independent T-Test result for comparing proportional NBA and WNBA salaries: ")
print(prop_result[0])



## Bootstrapping section
## Thinking comparing statistics against league salary?
## find average player for each statistic, compare their salary to average?
## top 10 players in each statistic, compare their salaries to average?


WNBA_header = readWNBA[0]
NBA_header = readNBA[0]
# print(header)
x = np.array([0])
y = np.array([0])
for stat in WNBA_header[9:]:
    sorted_nba = readNBA[1:]
    sorted_wnba = readWNBA[1:]
    nbasum = 0
    wnbasum = 0
    wnba_ind = WNBA_header.index(stat)
    if stat in NBA_header:
        nba_ind = NBA_header.index(stat)
#         print(float(player[wnba_ind]))
        sorted_wnba.sort(key=lambda x: float(x[wnba_ind]))
        sorted_nba.sort(key=lambda x: float(x[nba_ind]))
#         print(top10wnba)
#         print(sorted_nba)
#         print(sorted_wnba)
#         print(median_nba)
        for player in sorted_wnba[-10:]:
#             print(float(player[0]))
            wnbasum += float(player[0]) / median_wnba
#             print(wnbasum)
        for player in sorted_nba[-10:]:
            nbasum += float(player[0]) / median_nba
#             print(float(player[0]) / median_nba)
        wnba_stat_sal_avg = wnbasum / 10
        nba_stat_sal_avg = nbasum / 10
        print("WNBA players in the top 10 in " + str(stat) + " are paid on average " + str(wnba_stat_sal_avg) + " more than league average.")
        print("NBA players in the top 10 in " + str(stat) + " are paid on average " + str(nba_stat_sal_avg) + " more than league average.")

            



