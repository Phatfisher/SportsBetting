#Combined number of turnovers Over or under a line calculated by stats, 10% vig
class UnderOverBet():
    total_bet = 0
    bet_list = []
    line = (425/34)-(356/35)+(440/36)-(356/35)+(365/35) + (385/33)-(356/35) + (331/33)-(356/35) +(356/35)
    line=26

    def __init__(self, name, side, amount):
        self.name = name
        self.side = side
        self.bet_amnt = amount
        UnderOverBet.total_bet += amount
        UnderOverBet.bet_list.append(self)
    # allows for the bet to return as the string for printing
    def __repr__(self):
        return self.name + " bet: " + str(self.bet_amnt) + ' on the number of total turnovers being ' + self.side + "26"
    # calculates the winnings of the bet
    def outcome(self, actual):
        pay_load=0
        winners=0
        l=None
        if (UnderOverBet.line < actual):
            if self.side == 'over':
                l=True
            else:
                l=False
        if (UnderOverBet.line > actual):
            if self.side == 'under':
                l=True
            else:
                l=False
        if l == True:
            for i in UnderOverBet.bet_list:
                if (i.side != self.side):
                    pay_load+= i.bet_amnt*(0.9)
                if (i.side == self.side):
                    winners+=1
            return (self.bet_amnt + ((pay_load)/winners))
        else:
            return self.bet_amnt * -1
A=UnderOverBet('Apple','under',70)
B=UnderOverBet('Sal', 'over', 70)
print(UnderOverBet.bet_list)
print(B.outcome(25))
print(A.outcome(25))