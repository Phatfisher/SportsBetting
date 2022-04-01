#who will have more advertisments: Coca-cola or Progressive insurance
class ExoticPropCommercial():
    total_bet=0
    bet_list=[]
    def __init__(self,name,company,amount):
        self.name=name
        self.company=company
        self.bet_amnt=amount
        ExoticPropCommercial.total_bet += amount
        ExoticPropCommercial.bet_list.append(self)
    #allows for the bet to return as the string for printing
    def __repr__(self):
        return self.name + " bet: " + str(self.bet_amnt) + ' on ' + self.company + " to have more advertising."
    #calculates the winnings of the bet
    def outcome(self, actual):
        pay_load=0
        winners=0
        if (self.company == actual):
            for i in ExoticPropCommercial.bet_list:
                if (i.company != actual):
                    pay_load+=i.bet_amnt
                if (i.company == actual):
                    winners+=1
            return (self.bet_amnt + pay_load/winners)
        else:
            return self.bet_amnt * -1
A=ExoticPropCommercial('Apple','Progressive',70)
B=ExoticPropCommercial('Sal', 'Coke', 70)
print(ExoticPropCommercial.bet_list)
print(B.outcome('Coke'))
print(A.outcome('Coke'))