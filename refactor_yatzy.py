import collections
ONE, TWO, THREE, FOUR, FIVE, SIX = 1, 2, 3, 4, 5, 6

class Yatzy:
    @staticmethod
    def oneList(d1, d2, d3, d4, d5):
        diceList = [d1, d2, d3, d4, d5]
        return diceList

    @staticmethod
    def chance(diceList):
        points = 0
        for dice in diceList:
            points += dice
        return points

    @staticmethod
    def yatzy(diceList):
        if diceList.count(diceList[0]) != FIVE:
            return 0
        return 50

    @staticmethod
    def ones(diceList):
        points = 0
        for dice in diceList:
            if dice == ONE:
                points += ONE
        return points
    
    @staticmethod
    def twos(diceList):
        points = 0
        for dice in diceList:
            if dice == TWO:
                points += TWO
        return points
    
    @staticmethod
    def threes(diceList):
        points = 0
        for dice in diceList:
            if dice == THREE:
                points += THREE
        return points
    
    @staticmethod
    def fours(diceList):
        points = 0
        for dice in diceList:
            if dice == FOUR:
                points += FOUR
        return points
    
    @staticmethod
    def fives(diceList):
        points = 0
        for dice in diceList:
            if dice == FIVE:
                points += FIVE
        return points
    
    @staticmethod
    def sixes(diceList):
        points = 0
        for dice in diceList:
            if dice == SIX:
                points += SIX
        return points

    @staticmethod
    def score_pair(diceList):
        for num in range(6,0,-1):
            if diceList.count(num) >= TWO:
                return num * TWO
        return 0
            
    @staticmethod
    def two_pair(diceList):
        points = 0
        counter = 0
        for num in range(6,0,-1):
            if diceList.count(num) >= TWO:
                points += num * TWO
                counter += ONE
            elif counter == TWO:
                return points
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
        if collections.Counter(diceList) == collections.Counter(range(1,6)):
            return 15
        return 0

    @staticmethod
    def largeStraight(diceList):
        if collections.Counter(diceList) == collections.Counter(range(2,7)):
            return 20
        return 0
    
    @staticmethod
    def fullHouse(diceList):
        for dice in diceList:
            if diceList.count(dice) == THREE:
                for otherDice in diceList:
                    if diceList.count(otherDice) == TWO and otherDice != dice:
                        return (dice * THREE + otherDice * TWO)
        return 0