from predictions import *


def favorite_adjusted_money_line(baseFavoriteline):
	# Determining the PLUS and MINUS lines.
	# Uses the difference of predicted team scores.
	team1_plus_minus = abs(predicted_scores[0] - predicted_scores[1])
	team2_plus_minus = abs(predicted_scores[2] - predicted_scores[3])
	# Then sum the differences and floors by 2.
	margin = round((team1_plus_minus + team2_plus_minus) // 2)
    
	if margin < 3:
		wdelta = .1
	elif margin > 5 & baseFavoriteline < 8:
		wdelta = .2
	elif margin > 8 & baseFavoriteline < 13: 
		wdelta = .3
	elif margin > 13 & baseFavoriteline < 21:
		wdelta = .5
	else:
		wdelta = 1

	return baseFavoriteline + (baseFavoriteline * wdelta)

def underdog_adjusted_money_line(baseUnderdogLine):
	# Determining the PLUS and MINUS lines.
	# Uses the difference of predicted team scores.
	team1_plus_minus = abs(predicted_scores[0] - predicted_scores[1])
	team2_plus_minus = abs(predicted_scores[2] - predicted_scores[3])
	# Then sum the differences and floors by 2.
	margin = round((team1_plus_minus + team2_plus_minus) // 2)
    
	if margin < 3:
		ldelta = .3
	elif margin > 5 & margin < 8:
		ldelta = .6
	elif margin > 8 & margin < 13: 
		ldelta = 1.5
	elif margin > 13 & margin < 21:
		ldelta = 2
	else:
		ldelta = 3

	return baseUnderdogLine + (baseUnderdogLine * ldelta)


if __name__ == '__main__':

	# Score Prediction
	team1_revised_scores = (predicted_scores[0] + predicted_scores[1]) / 2
	team2_revised_scores = (predicted_scores[2] + predicted_scores[3]) / 2

	# base money line numbers by default
	baseFavoriteLine = -100
	baseUnderdogLine = 100

	# Favorite is determined by winning team from score prediction.
	if team1_revised_scores > team2_revised_scores:
		favorite = team1[0]
	else:
		favorite = team2[0]

	# now figure out moneylines with point diff/ margin. 
	adjFavLine = favorite_adjusted_money_line(baseFavoriteLine)
	adjUnLine = underdog_adjusted_money_line(baseUnderdogLine)

	# States the money line in terminal.
	print('Money Line:')
	if favorite == team1[0]:
		print(f'{team1[0]:20s}: {adjFavLine}\n{team2[0]:20s}: +{adjUnLine}')
	else:
		print(f'{team1[0]:20s}: +{adjUnLine}\n{team2[0]:20s}: {adjFavLine}')