from datetime import datetime
import sys
from ExoticPropLengthOfAnthem import ExoticPropLengthOfAnthem
from ExoticPropCommercials import ExoticPropCommercials
from UnderOverBet import UnderOverBet

if __name__ == '__main__':

	f = open('player_bets.txt', 'a')

	# Gets the current date and time.
	f.write(datetime.today())
	print('welcome to our sportsbook')
	user=str(input('please enter a name to be associated with your bets:\n to exit enter w'))
	num_bet=0
	while (user != 'w'):
		while (num_bet<8):
			print('1:Under/Over \n 2:Exotic Prop (Length of Anthem) \n 3:Exotic Prop (Commercials)\n')
			choice = str(input('pick a category to place a bet in'))
			if choice == 1:
				print('This bet is based off of the number of total turnovers in the game. \n Do you think that the number of turnovers will be over or under 26?')
				side= str(input('please enter either "over" or "under"'))
				amount= int(input('please enter the amount you would like to bet'))
			        bet= UnderOverBet(user,side,amount)
				print(bet)
				write(bet)
				num_bet+= 1
			elif choice == 2:
				print('This bet is based on how long the national anthem will be in the game. \n do you think it will take over or under 114.5 seconds?')
				side= str(input('please enter either "over" or "under"'))
				amount= int(input('please enter the amount you would like to bet'))
			        bet= ExoticPropLengthOfAnthem(user,side,amount)
				print(bet)
				write(bet)
				num_bet+= 1
			elif choice ==3:
				print('This bet is based on the number of visual and verbal advertisments during the game \n(actual network commericals vary from company to company so in game advertisments only)\n who do you think will have more adds Progressive or Coca-Cola?')
				side=str(input('please enter either "Progressive" or "Coke"'))
				amount= int(input('please enter the amount you would like to bet'))
			        bet= ExoticPropCommercial(user,side,amount)
				print(bet)
				write(bet)
				num_bet+= 1				
		user=str(input('please enter a name to be associated with your bets:\n to exit enter w'))
		num_bet=0	
	

	f.close()
