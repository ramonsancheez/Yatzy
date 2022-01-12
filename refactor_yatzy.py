import collections
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
        if diceList.count(diceList[0]) != 5:
            return 0
        return 50
    
    @staticmethod
    def ones(diceList):
        sum = 0
        for dice in diceList:
            if dice == 1:
                sum += 1
        return sum
    

    @staticmethod
    def twos(diceList):
        sum = 0
        for dice in diceList:
            if dice == 2:
                sum += 2
        return sum
    
    @staticmethod
    def threes(diceList):
        sum = 0
        for dice in diceList:
            if dice == 3:
                sum += 3
        return sum
    
    @staticmethod
    def fours(diceList):
        sum = 0
        for dice in diceList:
            if dice == 4:
                sum += 4
        return sum
    
    @staticmethod
    def fives(diceList):
        sum = 0
        for dice in diceList:
            if dice == 5:
                sum += 5
        return sum
    
    @staticmethod
    def sixes(diceList):
        sum = 0
        for dice in diceList:
            if dice == 6:
                sum += 6
        return sum
    
    @staticmethod
    def score_pair(diceList):
        numbersDice = [6,5,4,3,2,1]
        for num in numbersDice:
            if diceList.count(num) >= 2:
                return num * 2
        return 0
            
    @staticmethod
    def two_pair(diceList):
        numbersDice = [6,5,4,3,2,1]
        sum = 0
        total = 0
        for num in numbersDice:
            if diceList.count(num) >= 2:
                sum += num * 2
                total += 1
            elif total == 2:
                return sum
        return 0

    @staticmethod
    def three_of_a_kind(diceList):
        for dice in diceList:
            if diceList.count(dice) >= 3:
                return(dice * 3)
        return 0
    
    @staticmethod
    def four_of_a_kind(diceList):
        for dice in diceList:
            if diceList.count(diceList[0]) < 4 and diceList.count(diceList[1]) < 4:
                return 0
            else:
                return(dice * 4)

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
            if diceList.count(dice) == 3:
                for dice1 in diceList:
                    if diceList.count(dice1) == 2 and dice1 != dice:
                        return (dice * 3 + dice1 * 2)
        return 0