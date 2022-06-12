class Configuration:
    configs = ["Category", "Ones", "Twos", "Threes", "Fours", "Fives", "Sixes",
               "Upper Scores", "Upper Bonus(35)", "Three of a kind", "Four of a kind", "Full House(25)",
               "Small Straight(30)", "Large Straight(40)", "Yahtzee(50)", "Chance", "Lower Scores", "Total"]

    @staticmethod
    def getConfigs(): 
        return Configuration.configs

    def score(row, d):  
        
        dicelist = []
        for n in d:
            dicelist.append(n.getRoll())
        if (row >= 0 and row <= 6):
            return Configuration.scoreUpper(dicelist, row + 1)
        elif (row == 8):
            return Configuration.scoreThreeOfAKind(dicelist)
        elif (row == 9):
            return Configuration.scoreFourOfAKind(dicelist)
        elif (row == 10):
            return Configuration.scoreFullHouse(dicelist)
        elif (row == 11):
            return Configuration.scoreSmallStraight(dicelist)
        elif (row == 12):
            return Configuration.scoreLargeStraight(dicelist)
        elif (row == 13):
            return Configuration.scoreYahtzee(dicelist)
        elif (row == 14):
            return Configuration.sumDie(dicelist)

    def scoreUpper(d, num): 
        return d.count(num)*num

    def scoreThreeOfAKind(d):
        for i in range(len(d)+1):
            if d.count(i+1) >= 3:
                return sum(d)
        return False

    def scoreFourOfAKind(d):
        for i in range(len(d)+1):
            if d.count(i+1) >= 4:
                return sum(d)
        return False

    def scoreFullHouse(d):
        for i in range(len(d)+1):
            for j in range(len(d)):
                if d.count(i+1) is 2 and d.count(j+1) is 3:
                    return 25
                if d.count(i+1) is 3 and d.count(j+1) is 2:
                    return 25
        return False

    def scoreSmallStraight(d):
        if (1 in d and 2 in d and 3 in d and 4 in d) or (2 in d and 3 in d and 4 in d and 5 in d) or (3 in d and 4 in d and 5 in d and 6 in d):
            return 30
        return False

    def scoreLargeStraight(d):
        if (1 in d and 2 in d and 3 in d and 4 in d and 5 in d) or (2 in d and 3 in d and 4 in d and 5 in d and 6 in d) :
            return 40
        return False

    def scoreYahtzee(d):
        for i in range(len(d)+1):
            if d.count(i+1) is 5:
                print( d.count(i+1))
                return 50
        return False

    def sumDie(d):
        return sum(d)