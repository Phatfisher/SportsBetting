
#plus/minus
#unskilled

# D1 Averages
d1_offE_avg = 103.8
d1_pace_avg = 67.3

# Takes in a list of team stats and outputs 4 score predictions, 2 for each team.
def predict(teams:list):
	team1_pace = teams[0][4] + (0.475 * teams[0][6]) - teams[0][13] + teams[0][15]# FGA+0.475*FTA-ORB+TOV
	team1_offEff = teams[0][1] * 100 / teams[0][17]# PTS*100/Pace
	team1_oppPace = teams[2][4] + (0.475 * teams[2][6]) - teams[2][13] + teams[2][15]# oppFGA+0.475*oppFTA-oppORB+oppTOV
	team1_defEff = teams[2][1] * 100 / team1_oppPace# oppPTS*100/oppPace

	team2_pace = teams[1][4] + (0.475 * teams[1][6]) - teams[1][13] + teams[1][15]# FGA+0.475*FTA-ORB+TOV
	team2_offEff = teams[1][1] * 100 / team2_pace# PTS*100/Pace
	team2_oppPace = teams[3][4] + (0.475 * teams[3][6]) - teams[3][13] + teams[3][15]# oppFGA+0.475*oppFTA-oppORB+oppTOV
	team2_defEff = teams[3][1] * 100 / team2_oppPace# oppPTS*100/oppPace

	adjusted_pace = team1_pace + team2_pace - d1_pace_avg

	team1_adjustedOffEff = team1_offEff + team2_defEff - d1_offE_avg
	team2_adjustedOffEff = team2_offEff + team1_defEff - d1_offE_avg
	
	team1_poss_prediction = team1_offEff * adjusted_pace / 100
	team2_poss_prediction = team2_offEff * adjusted_pace / 100

	team1_offEff_prediction = team1_adjustedOffEff * adjusted_pace / 100
	team2_offEff_prediction = team2_adjustedOffEff * adjusted_pace / 100

	return [team1_poss_prediction, team1_offEff_prediction, team2_poss_prediction, team2_offEff_prediction]

# Creates a list of stats for a given team. Uses format from championship_teams_stats.txt
def getTeamStats(file):
	team = file.readline()

	team = team.split(', ')
	team[len(team) - 1] = team[len(team) - 1].split('\n')[0]

	for i in range(1, len(team)):
		team[i] = float(team[i])
	return team


if __name__ == '__main__':

	f = open('championship_teams_stats.txt', 'r')
	# blank line
	f.readline()
	# ----------

	# Championship Teams
	team1 = getTeamStats(f)
	team2 = getTeamStats(f)

	# blank line
	f.readline()
	f.readline()
	# ----------

	# Stats from opposing teams
	opp_team1 = getTeamStats(f)
	opp_team2 = getTeamStats(f)

	# Gives 4 scores, 2 for each team:
	# Possesion Prediction (index: 0, 2), Offensive Effeciency Prediction (index: 1, 3)
	predicted_scores = predict([team1, team2, opp_team1, opp_team2])

	# These are the predicted scores for each team.
	team1_revised_scores = (predicted_scores[0] + predicted_scores[1]) / 2
	team2_revised_scores = (predicted_scores[2] + predicted_scores[3]) / 2
	print(f'{team1[0]}: {round(team1_revised_scores)}\n{team2[0]}: {round(team2_revised_scores)}')
	
	if team1_revised_scores > team2_revised_scores:
		print(f'WINNER: {team1[0]}')
	else:
		print(f'WINNER: {team2[0]}')