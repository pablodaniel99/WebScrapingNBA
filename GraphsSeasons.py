from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np
import seaborn as sns

plt.style.use('_mpl-gallery')

# Make data
X =  [2001, 2002, 2003, 2004,
        2005, 2006, 2007, 2008, 2009,
        2010, 2011, 2012, 2013, 2014,
        2015, 2016, 2017, 2018, 2019,
        2020, 2021]

"""
X = years
Y = victories mean each year 
Z = Simple Rating System (SRS)
"""

df = pd.read_csv('nba_team_data.csv')

newdf = 0
cont = 0

listPointsGame = []
listSRS = []
listGamesBehind = []
listPointsAgainst = []
newdf = pd.DataFrame()

for year in X:

    temporada = df.loc[df['Year'] == year]

    pointsGame = temporada['PS/G']
    simpleRatSys = temporada['SRS']

    gamesBehind = []
    cont = 0
    for elements in temporada['GB']:

        if len(elements) > 1:
            gamesBehind.append(float(elements))

        cont = cont + 1
    

    meanGamesBehind = sum(gamesBehind) / len(gamesBehind)
    meanPointsGame = sum(pointsGame) / len(pointsGame)
    meanSRS = sum(simpleRatSys) / len(simpleRatSys)


    print("MEDIA: " + str(meanGamesBehind))

    contIndex = 0

    data = {'SRS': meanSRS, 'GB': meanGamesBehind, 'PS/G': meanPointsGame}
    newdf = pd.DataFrame(data, index = [contIndex])

    contIndex = contIndex + 1

    simpleRatSys = newdf['SRS'].tolist()
    listSRS.append(simpleRatSys[0])

    gamesBehind = newdf['GB'].tolist()
    listGamesBehind.append(gamesBehind[0])

    pointsGame = newdf['PS/G'].tolist()
    listPointsGame.append(pointsGame[0])


print(newdf)
print(listGamesBehind)
print(listSRS)
print(listPointsGame)

diction = {'SRS': listSRS, 'GamesBehind': listGamesBehind, 'PointsGame': listPointsGame}

df = pd.DataFrame(diction)

print(df.corr())

well_data = df.corr()

sns.heatmap(well_data, cmap="RdBu", vmax= 1, vmin= -1, annot=True,
            annot_kws = {'fontsize': 11, 'fontweight': 'bold'})

plt.show()

# YA ESTÁ HECHA CORRELACIÓN ENTRE TODAS LAS TEMPORADAS, AHORA LA HACEMOS UNA A UNA DESDE