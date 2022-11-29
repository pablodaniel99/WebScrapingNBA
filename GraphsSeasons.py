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

cont = 0

listPointsGame = []
listSRS = []
listGamesBehind = []

#completeStats = 
yearStats = pd.DataFrame(columns=['SRS', 'GamesBehind', 'PointsGame', 'year'])

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

    contIndex = 0

    data = {'SRS': meanSRS, 'GamesBehind': meanGamesBehind, 'PointsGame': meanPointsGame, 'year': year}

    #yearStats.loc[year] = data
    yearStats = pd.DataFrame(data, index = [contIndex])

    contIndex = contIndex + 1

    simpleRatSys = yearStats['SRS'].tolist()
    listSRS.append(simpleRatSys[0])

    gamesBehind = yearStats['GamesBehind'].tolist()
    listGamesBehind.append(gamesBehind[0])

    pointsGame = yearStats['PointsGame'].tolist()
    listPointsGame.append(pointsGame[0])


print("Hola")
print(yearStats)
print(listGamesBehind)
print(listSRS)
print(listPointsGame)

diction = {'SRS': listSRS, 'GamesBehind': listGamesBehind, 'PointsGame': listPointsGame}

df = pd.DataFrame(diction)

print(df.corr())


## ALL SEASONS CORRELATION GRAPH
well_data = df.corr()

sns.heatmap(well_data, cmap="RdBu", vmax= 1, vmin= -1, annot=True,
            annot_kws = {'fontsize': 11, 'fontweight': 'bold'})

plt.show()

# MATRIX OF GRAPHS

