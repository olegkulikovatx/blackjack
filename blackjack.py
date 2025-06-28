import random

''' Blackjack game implementation in Python
    This is a simple text-based version of the game where a human player plays against a robot.
    The game follows the basic rules of Blackjack, where the goal is to get as close to 21 points without going over.
    The player can choose to take another card or stop, and the robot makes decisions based on
    a random strategy.
    The game ends when both players decide to stop or one of them goes over 21 points
    (busts).
    The winner is determined based on the points of each player.
'''

class Card(object):
    def __init__(self, rank, suite):
        self.rank = rank
        self.suite = suite

    def __str__(self):
        return f"{self. rank} {self.suite}"


    @staticmethod
    def get_card_points():
        return {"2": 2, "3": 3, "4": 4, "5": 5,
                  "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
                  "В": 10, "Д": 10, "К": 10, "Т": 11}

    def get_points(self):
        points = Card.get_card_points()
        return points[self.rank]
        

class Deck():
    def __init__(self):
        self.cards = []
        ranks = Card.get_card_points().keys()
        suites = ['червей', 'бубен', 'пик', 'треф']
        for suite in suites:
            for rank in ranks:
                self.cards.append(Card(rank, suite))

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        self.shuffle()
        return self.cards.pop()
    
class Player():
    def __init__(self):
        self.cards = []
        self.passed = False

    def passed(self):
        return self.passed

    def two_aces(self):
        if len(self.cards) == 2 and self.cards[0].rank == "Т" \
        and self.cards[1].rank == "Т":
            return True
        return False
    
    def get_points(self):
        points = 0
        for card in self.cards:
            points += card.get_points()
        return points
    
    def bust(self):
        points = self.get_points()
        if points > 22 or points == 22 and not self.two_aces():
            return True
        return False
    
    def add_card(self, card):
        self.cards.append(card)

    
    def decide_to_take_card():
        return False


class HumanPlayer(Player):
    def __init__(self):
        super().__init__()

    def decide_to_take_card(self):
        if self.passed:
            return False
        
        if self.bust():
            return False
        
        decision = ""
        while not decision in ["1", "2"]:
            decision = input(f"У вас {self.get_points()} очков. 1 - себе, 2 - еще: ")

        if decision == "1":
            self.passed = True
            return False
        
        return True
    

class RoboPlayer(Player):
    def __init__(self):
        super().__init__()

    def decide_to_take_card(self):
        if self.passed:
            return False

        if self.bust():
            return False

        p = random.randint(10, 20) / self.get_points()
        if p < 1:
            return False
                
        return True
    

class Game:
    def __init__(self):
        self.human = HumanPlayer()
        self.robot = RoboPlayer()
        self.deck  = Deck()
        self.winner = None
    
    def play(self):
        card = self.deck.draw()
        print(card)
        self.human.add_card(card)
        card = self.deck.draw()
        print(card)
        self.human.add_card(card)

        card = self.deck.draw()
        #print(card)
        self.robot.add_card(card)
        card = self.deck.draw()
        #print(card)
        self.robot.add_card(card)

        while True:
            if self.human.passed and self.robot.passed:
                break
            if self.human.decide_to_take_card():
                card = self.deck.draw()
                print(card)
                self.human.add_card(card)                
                if self.human.bust():
                    print("Перебор")
                    break
            if self.robot.decide_to_take_card():
                card = self.deck.draw()
                print(card)
                self.robot.add_card(card)
                if self.robot.bust():
                    print("Перебор")
                    break
        self.decide_winner()
    
    def decide_winner(self):
        if self.human.bust() or self.human.get_points() < self.human.get_points():
            self.winner = "Робот"
        elif self.robot.bust() or self.human.get_points() > self.human.get_points():
            self.winner = "Человек"
        else:
            self.winner = "Никто не"
        print(f"Счет: Человек {self.human.get_points()} Робот {self.robot.get_points()}")
        print(f"{self.winner} победил")

game = Game()
game.play()



        
