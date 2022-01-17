class Yatzy:
    ONE, TWO, THREE, FOUR, FIVE, SIX = 1, 2, 3, 4, 5, 6

    @staticmethod
    def oneList(d1, d2, d3, d4, d5):
        rollDice = [d1, d2, d3, d4, d5]
        return rollDice

    @staticmethod
    def chance(rollDice):
        points = 0
        for dice in rollDice:
            points += dice
        return points

    @staticmethod
    def yatzy(rollDice):
        if rollDice.count(rollDice[0]) != Yatzy.FIVE:
            return 0
        return 50

    @staticmethod
    def ones(rollDice):
        points = 0
        for dice in rollDice:
            if dice == Yatzy.ONE:
                points += Yatzy.ONE
        return points
    
    @staticmethod
    def twos(rollDice):
        points = 0
        for dice in rollDice:
            if dice == Yatzy.TWO:
                points += Yatzy.TWO
        return points
    
    @staticmethod
    def threes(rollDice):
        points = 0
        for dice in rollDice:
            if dice == Yatzy.THREE:
                points += Yatzy.THREE
        return points
    
    @staticmethod
    def fours(rollDice):
        points = 0
        for dice in rollDice:
            if dice == Yatzy.FOUR:
                points += Yatzy.FOUR
        return points
    
    @staticmethod
    def fives(rollDice):
        points = 0
        for dice in rollDice:
            if dice == Yatzy.FIVE:
                points += Yatzy.FIVE
        return points
    
    @staticmethod
    def sixes(rollDice):
        points = 0
        for dice in rollDice:
            if dice == Yatzy.SIX:
                points += Yatzy.SIX
        return points

    @staticmethod
    def score_pair(rollDice):
        for num in range(6,0,-1):
            if rollDice.count(num) >= Yatzy.TWO:
                return num * Yatzy.TWO
        return 0
            
    @staticmethod
    def two_pair(rollDice):
        points = 0
        amountPairs = 0
        for num in range(6,0,-1):
            if rollDice.count(num) >= Yatzy.TWO:
                points += num * Yatzy.TWO
                amountPairs += Yatzy.ONE
            if amountPairs == Yatzy.TWO:
                return points
        return 0
    
    @staticmethod
    def three_of_a_kind(rollDice):
        for dice in rollDice:
            if rollDice.count(dice) >= Yatzy.THREE:
                return dice * Yatzy.THREE 
        return 0
    
    @staticmethod
    def four_of_a_kind(rollDice):
        for dice in rollDice:
            if rollDice.count(dice) >= Yatzy.FOUR:
                return dice * Yatzy.FOUR
        return 0

    import collections
    @staticmethod
    def smallStraight(rollDice):
        if Yatzy.collections.Counter(rollDice) == Yatzy.collections.Counter(range(1,6)):
            return 15
        return 0

    @staticmethod
    def largeStraight(rollDice):
        if Yatzy.collections.Counter(rollDice) == Yatzy.collections.Counter(range(2,7)):
            return 20
        return 0
    
    @staticmethod
    def fullHouse(rollDice):
        isTrio = False
        for dice in rollDice:
            if rollDice.count(dice) == Yatzy.THREE:
                isTrio = True
                break
        for otherDice in rollDice:
            if isTrio and rollDice.count(otherDice) == Yatzy.TWO:
                    return (dice * Yatzy.THREE + otherDice * Yatzy.TWO)
        return 0


