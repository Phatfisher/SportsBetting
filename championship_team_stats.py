team1 = 'Duke'
team2 = 'Villanova'

### Change the teams above to get stats of wanted teams.
### Gets boxscores of NCAAB games from March 18th, 2022 to April 4th, 2022.
### The program then write averages of important stats of the March Madness
### tournament to a text file.
### Can use command line arguments for teams (has to be correct spelling).

from datetime import datetime
from sportsipy.ncaab.boxscore import Boxscores, Boxscore
import sys

# Averages number in a given list.
def average(list_to_average:list):
	revised_list = []
	for i in list_to_average:
		if type(i) == int or type(i) == float:
			revised_list.append(i)

	return round((sum(revised_list) / len(revised_list)), 2)

# Gets the stats of a given team using games in a time range.
def team_stats(team:str):
	points = []
	assists = []
	blocks = []
	field_goal_attempts = []
	field_goals = []
	free_throw_attempts = []
	free_throws = []
	three_point_attempts = []
	three_points = []
	two_point_attempts = []
	two_points = []
	fouls = []
	offensive_rebounds = []
	total_rebounds = []
	turnovers = []
	minutes_played = []
	pace = []

	for i in games.games:
		for j in games.games[i]:
			if j['away_name'] == team:
				boxscore = Boxscore(j['boxscore'])

				points.append(boxscore.away_points)
				assists.append(boxscore.away_assists)
				blocks.append(boxscore.away_blocks)
				field_goal_attempts.append(boxscore.away_field_goal_attempts)
				field_goals.append(boxscore.away_field_goals)
				free_throw_attempts.append(boxscore.away_free_throw_attempts)
				free_throws.append(boxscore.away_free_throws)
				three_point_attempts.append(boxscore.away_three_point_field_goal_attempts)
				three_points.append(boxscore.away_three_point_field_goals)
				two_point_attempts.append(boxscore.away_two_point_field_goal_attempts)
				two_points.append(boxscore.away_two_point_field_goals)
				fouls.append(boxscore.away_personal_fouls)
				offensive_rebounds.append(boxscore.away_offensive_rebounds)
				total_rebounds.append(boxscore.away_total_rebounds)
				turnovers.append(boxscore.away_turnovers)
				minutes_played.append(boxscore.away_minutes_played)
				pace.append(boxscore.pace)
			if j['home_name'] == team:
				boxscore = Boxscore(j['boxscore'])

				points.append(boxscore.home_points)
				assists.append(boxscore.home_assists)
				blocks.append(boxscore.home_blocks)
				field_goal_attempts.append(boxscore.home_field_goal_attempts)
				field_goals.append(boxscore.home_field_goals)
				free_throw_attempts.append(boxscore.home_free_throw_attempts)
				free_throws.append(boxscore.home_free_throws)
				three_point_attempts.append(boxscore.home_three_point_field_goal_attempts)
				three_points.append(boxscore.home_three_point_field_goals)
				two_point_attempts.append(boxscore.home_two_point_field_goal_attempts)
				two_points.append(boxscore.home_two_point_field_goals)
				fouls.append(boxscore.home_personal_fouls)
				offensive_rebounds.append(boxscore.home_offensive_rebounds)
				total_rebounds.append(boxscore.home_total_rebounds)
				turnovers.append(boxscore.home_turnovers)
				minutes_played.append(boxscore.home_minutes_played)
				pace.append(boxscore.pace)

	return [team,
		average(points),
		average(assists),
		average(blocks),
		average(field_goal_attempts),
		average(field_goals),
		average(free_throw_attempts),
		average(free_throws),
		average(three_point_attempts),
		average(three_points),
		average(two_point_attempts),
		average(two_points),
		average(fouls),
		average(offensive_rebounds),
		average(total_rebounds),
		average(turnovers),
		average(minutes_played),
		average(pace)]

# Gets the opposing stats of a given team using games in a time range.
def opp_team_stats(team:str):
	points = []
	assists = []
	blocks = []
	field_goal_attempts = []
	field_goals = []
	free_throw_attempts = []
	free_throws = []
	three_point_attempts = []
	three_points = []
	two_point_attempts = []
	two_points = []
	fouls = []
	offensive_rebounds = []
	total_rebounds = []
	turnovers = []
	minutes_played = []
	pace = []

	for i in games.games:
		for j in games.games[i]:
			if j['home_name'] == team:
				boxscore = Boxscore(j['boxscore'])

				points.append(boxscore.away_points)
				assists.append(boxscore.away_assists)
				blocks.append(boxscore.away_blocks)
				field_goal_attempts.append(boxscore.away_field_goal_attempts)
				field_goals.append(boxscore.away_field_goals)
				free_throw_attempts.append(boxscore.away_free_throw_attempts)
				free_throws.append(boxscore.away_free_throws)
				three_point_attempts.append(boxscore.away_three_point_field_goal_attempts)
				three_points.append(boxscore.away_three_point_field_goals)
				two_point_attempts.append(boxscore.away_two_point_field_goal_attempts)
				two_points.append(boxscore.away_two_point_field_goals)
				fouls.append(boxscore.away_personal_fouls)
				offensive_rebounds.append(boxscore.away_offensive_rebounds)
				total_rebounds.append(boxscore.away_total_rebounds)
				turnovers.append(boxscore.away_turnovers)
				minutes_played.append(boxscore.away_minutes_played)
				pace.append(boxscore.pace)
			if j['away_name'] == team:
				boxscore = Boxscore(j['boxscore'])

				points.append(boxscore.home_points)
				assists.append(boxscore.home_assists)
				blocks.append(boxscore.home_blocks)
				field_goal_attempts.append(boxscore.home_field_goal_attempts)
				field_goals.append(boxscore.home_field_goals)
				free_throw_attempts.append(boxscore.home_free_throw_attempts)
				free_throws.append(boxscore.home_free_throws)
				three_point_attempts.append(boxscore.home_three_point_field_goal_attempts)
				three_points.append(boxscore.home_three_point_field_goals)
				two_point_attempts.append(boxscore.home_two_point_field_goal_attempts)
				two_points.append(boxscore.home_two_point_field_goals)
				fouls.append(boxscore.home_personal_fouls)
				offensive_rebounds.append(boxscore.home_offensive_rebounds)
				total_rebounds.append(boxscore.home_total_rebounds)
				turnovers.append(boxscore.home_turnovers)
				minutes_played.append(boxscore.home_minutes_played)
				pace.append(boxscore.pace)

	return [f'vs. {team}',
		average(points),
		average(assists),
		average(blocks),
		average(field_goal_attempts),
		average(field_goals),
		average(free_throw_attempts),
		average(free_throws),
		average(three_point_attempts),
		average(three_points),
		average(two_point_attempts),
		average(two_points),
		average(fouls),
		average(offensive_rebounds),
		average(total_rebounds),
		average(turnovers),
		average(minutes_played),
		average(pace)]

# Writes a list to a file.
def write(to_write:list):
	for i in to_write:
		if i == to_write[len(to_write) - 1]:
			f.write(f'{i}')
		else:	
			f.write(f'{i}, ')
	f.write('\n')


if __name__ == '__main__':

	try:
		if sys.argv[1] != None and sys.argv[2] != None:
			team1 = sys.argv[1]
			team2 = sys.argv[2]
	except:
		pass

	print('Getting games')
	# Gets games between the start of March Madness and the project due date.
	games = Boxscores(datetime(2022, 3, 18), datetime(2022, 4, 4))

	# Opens championship_teams_stats.txt to be written in.
	f = open('championship_teams_stats.txt', 'w')

	print('Writing to file')
	write(['Team', 'PTS', 'AST', 'BLK', 'FGA', 'FG', 'FTA', 'FT', '3PA', '3P', '2PA', '2P', 'PF', 'ORB', 'TRB', 'TOV', 'MP', 'Pace'])
	write(team_stats(team1))
	print('First team done')
	write(team_stats(team2))
	print('Second team done\nWriting opposing teams stats')
	f.write('\nOpposing Team Stats\n')
	write(opp_team_stats(team1))
	print('First team done')
	write(opp_team_stats(team2))
	print('Second team done')
	f.close()
	print('File is completed')