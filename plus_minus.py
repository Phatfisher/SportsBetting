from predictions import *

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


	# Determining the PLUS and MINUS lines.
	team1_plus_minus = abs(predicted_scores[0] - predicted_scores[1])
	team2_plus_minus = abs(predicted_scores[2] - predicted_scores[3])
	plus_minus = (team1_plus_minus + team2_plus_minus) // 2

	# Score Prediction
	team1_revised_scores = (predicted_scores[0] + predicted_scores[1]) / 2
	team2_revised_scores = (predicted_scores[2] + predicted_scores[3]) / 2
	# Favorite is determined by winning team from score prediction.
	if team1_revised_scores > team2_revised_scores:
		favorite = team1[0]
	else:
		favorite = team2[0]

	# States the PLUS and MINUS lines in terminal.
	print('PLUS AND MINUS LINES:')
	if favorite == team1[0]:
		print(f'{team1[0]:20s}: -{round(plus_minus)}\n{team2[0]:20s}: +{round(plus_minus)}')