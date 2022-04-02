### Determines the plus and minus lines based on the predicted score of a game.
### Uses the 'predicted_scores' list from predictions.py as the scores.
### Favorites are determined by the winner using predicted score.

from predictions import *

def plus_minus():
	# Determining the PLUS and MINUS lines.
	# Uses the difference of predicted team scores.
	team1_plus_minus = abs(predicted_scores[0] - predicted_scores[1])
	team2_plus_minus = abs(predicted_scores[2] - predicted_scores[3])
	# Then sum the differences and floors by 2.
	plus_minus = (team1_plus_minus + team2_plus_minus) // 2

	return plus_minus


if __name__ == '__main__':

	plus_minus = plus_minus()

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
	else:
		print(f'{team1[0]:20s}: +{round(plus_minus)}\n{team2[0]:20s}: -{round(plus_minus)}')