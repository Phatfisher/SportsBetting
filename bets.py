import sys
#do plus/minus unskilled


#plus/minus


#unskilled

d1_offE_avg = 103.8
d1_pace_avg = 67.3

def predict(team1:list, team2:list):
	team1_offEff = team1[1] * 100 / team1[17]# PTS*100/Pace
	team1_pace = team1[17]# Pace

	team2_offEff = team2[1] * 100 / team2[17]# PTS*100/Pace
	team2_pace = team2[17]# Pace

	adjusted_pace = team1_pace + team2_pace - d1_pace_avg

	return f'{team1[0]}: {round(team1_offEff * adjusted_pace / 100)}\n{team2[0]}: {round(team2_offEff * adjusted_pace / 100)}'

def getTeamStats():
	team = f.readline()

	team = team.split(', ')
	team[len(team) - 1] = team[len(team) - 1].split('\n')[0]

	for i in range(1, len(team)):
		team[i] = float(team[i])
	return team


if __name__ == '__main__':

	f = open('championship_teams_stats.txt', 'r')
	f.readline()

	team1 = getTeamStats()
	team2 = getTeamStats()

	print(team1)
	print(team2)

	print(predict(team1, team2))