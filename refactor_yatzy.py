import collections
ONE, TWO, THREE, FOUR, FIVE, SIX = 1, 2, 3, 4, 5, 6
class Yatzy:
    @staticmethod
    def oneList(d1, d2, d3, d4, d5):
        diceList = [d1, d2, d3, d4, d5]
        return diceList

    @staticmethod
    def chance(diceList):
        total = 0
        for dice in diceList:
            total += dice
        return total

    @staticmethod
    def yatzy(diceList):
        if diceList.count(diceList[0]) != FIVE:
            return 0
        return 50
    
    @staticmethod
    def ones(diceList):
        sum = 0
        for dice in diceList:
            if dice == ONE:
                sum += ONE
        return sum
    
    @staticmethod
    def twos(diceList):
        sum = 0
        for dice in diceList:
            if dice == TWO:
                sum += TWO
        return sum
    
    @staticmethod
    def threes(diceList):
        sum = 0
        for dice in diceList:
            if dice == THREE:
                sum += THREE
        return sum
    
    @staticmethod
    def fours(diceList):
        sum = 0
        for dice in diceList:
            if dice == FOUR:
                sum += FOUR
        return sum
    
    @staticmethod
    def fives(diceList):
        sum = 0
        for dice in diceList:
            if dice == FIVE:
                sum += FIVE
        return sum
    
    @staticmethod
    def sixes(diceList):
        sum = 0
        for dice in diceList:
            if dice == SIX:
                sum += SIX
        return sum

    @staticmethod
    def score_pair(diceList):
        numbersDice = [6,5,4,3,2,1]
        for num in numbersDice:
            if diceList.count(num) >= TWO:
                return num * TWO
        return 0
            
    @staticmethod
    def two_pair(diceList):
        numbersDice = [6,5,4,3,2,1]
        sum = 0
        total = 0
        for num in numbersDice:
            if diceList.count(num) >= TWO:
                sum += num * TWO
                total += ONE
            elif total == TWO:
                return sum
        return 0

    @staticmethod
    def three_of_a_kind(diceList):
        for dice in diceList:
            if diceList.count(dice) >= THREE:
                return(dice * THREE)
        return 0
    
    @staticmethod
    def four_of_a_kind(diceList):
        for dice in diceList:
            if diceList.count(diceList[0]) < FOUR and diceList.count(diceList[1]) < FOUR:
                return 0
            else:
                return(dice * FOUR)

    @staticmethod
    def smallStraight(diceList):
        rightList = [1,2,3,4,5]
        if collections.Counter(diceList) == collections.Counter(rightList):
            return 15
        return 0

    @staticmethod
    def largeStraight(diceList):
        rightList = [2,3,4,5,6]
        if collections.Counter(diceList) == collections.Counter(rightList):
            return 20
        return 0
    
    @staticmethod
    def fullHouse(diceList):
        for dice in diceList:
            if diceList.count(dice) == THREE:
                for dice1 in diceList:
                    if diceList.count(dice1) == TWO and dice1 != dice:
                        return (dice * THREE + dice1 * TWO)
        return 0