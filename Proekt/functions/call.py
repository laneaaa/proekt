from functions.drawStatistics import Drawing


winnerTeamName: str = input('Введите название победившей команды: ')
loserTeamName: str = input('Введите название проигравшей команды: ')

amountOfMaps: int = int(input('Введите количество сыгранных карт (2 или 3): '))

print('Введите кол-во выигранных раундов сначала команды победителей (в матче),',
      'затем команды проигравших, разделяя пробелом: ')

everyRound: list = []
mapsNames: list = []

for value in range(1, amountOfMaps+1):
    everyRound.append([int(inp) for inp in input(f'Для {value} карты: ').split()])
    mapsNames.append(input(f'Введите название {value} карты: '))

matches: list[list[str | list]] = list(zip(mapsNames, everyRound))

firstTeamTotal: int = sum(i[0] for i in everyRound)
secondTeamTotal: int = sum(i[1] for i in everyRound)

totalPerTeam: tuple = (firstTeamTotal, secondTeamTotal)
amountOfRounds: int = sum(totalPerTeam)

firstTeam: list = []
secondTeam: list = []

for firstTeamPlayer in range(1, 6):

    playerNickname: str = input(f'Ник {firstTeamPlayer} игрока команды победителей: ')
    playerKills: int = int(input(f'Убийства {firstTeamPlayer} игрока команды победителей: '))
    playerDeaths: int = int(input(f'Смерти {firstTeamPlayer} игрока команды победителей: '))
    playerSupports: int = int(input(f'Помощи {firstTeamPlayer} игрока команды победителей: '))

    firstTeam.append((playerNickname, playerKills, playerDeaths, playerSupports))


for secondTeamPlayer in range(1, 6):

    playerNickname: str = input(f'Ник {secondTeamPlayer} игрока команды проигравших: ')
    playerKills: int = int(input(f'Убийства {secondTeamPlayer} игрока команды проигравших: '))
    playerDeaths: int = int(input(f'Смерти {secondTeamPlayer} игрока команды проигравших: '))
    playerSupports: int = int(input(f'Помощи {secondTeamPlayer} игрока команды проигравших: '))

    secondTeam.append((playerNickname, playerKills, playerDeaths, playerSupports))


dataForDrawing: list[list[str | list]] = [[winnerTeamName, firstTeam], [loserTeamName, secondTeam]]

drawing: Drawing = Drawing(dataForDrawing)
drawing.start(rounds=amountOfRounds, matches=matches)
drawing.save()

print('\n----------------------\nУспешно!\n')
