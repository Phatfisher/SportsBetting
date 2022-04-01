#will the length of the national anthem be longer or shorter than average
class ExoticPropLengthOfAnthem():
    total_bet=0
    bet_list=[]
    line=114.5
    def __init__(self,name,side,amount):
        self.name=name
        self.side=side
        self.bet_amnt=amount
        ExoticPropLengthOfAnthem.total_bet += amount
        ExoticPropLengthOfAnthem.bet_list.append(self)
    #allows for the bet to return as the string for printing
    def __repr__(self):
        return self.name + " bet: " + str(self.bet_amnt) + ' on the length of the national anthem being ' + self.side + " 114.5 seconds."
    #calculates the winnings of the bet
    def outcome(self, actual):
        pay_load=0
        winners=0
        l=None
        if (ExoticPropLengthOfAnthem.line < actual):
            if self.side == 'over':
                l=True
            else:
                l=False
        if (ExoticPropLengthOfAnthem.line > actual):
            if self.side == 'under':
                l=True
            else:
                l=False
        if l == True:
            for i in ExoticPropLengthOfAnthem.bet_list:
                if (i.side != self.side):
                    pay_load+=i.bet_amnt
                if (i.side == self.side):
                    winners+=1
            return (self.bet_amnt + pay_load/winners)
        else:
            return self.bet_amnt * -1
A=ExoticPropLengthOfAnthem('Apple','under',70)
B=ExoticPropLengthOfAnthem('Sal', 'over', 70)
print(ExoticPropLengthOfAnthem.bet_list)
print(B.outcome(125))
print(A.outcome(125))