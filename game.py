#!/usr/bin/env python

## write a card game called Old Maid. Here is how it works:
#  - 1st: Get list of players
#  - 2nd: Hand out 10 cards to each player
#  - 3rd: Each player matches his cards based on same rank and complimentary suits (clubs<->spades) (diamonds<->hearts)
#  - 4th: The matched cards are discarded.
#  - 5th: Game begins with the rest of the cards
#  - 6th: Each player takes a card from the player on his left and matches it with his stack.
#           if there is a match, he removes both the matching cards else, he adds the new card to his stack
#  - 7th: Step 6 is repeated until one player has no more cards left



# Properties of card: 
#        1. suit
#        2. rank
# methods:
#        1. init
#        2. str
#        3. cmp
class Card:
    suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    ranks = ['NA', 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    def __init__(self, suit=0, rank=0):
        self.suit = suit
        self.rank = rank


    def __str__(self):
        return '%s of %s' %(self.ranks[self.rank], self.suits[self.suit])

    # any kind of comparision (<, >, ==, in etc)
    def __cmp__(self, other):
        if self.suit > other.suit: return 1
        if self.suit < other.suit: return -1

        if self.rank > other.rank: return 1
        if self.rank < other.rank: return -1

        return 0


# Properties of Deck: 
#        1. list of cards
# methods:
#        1. init
#        2. print_deck
#        3. shuffle
#        4. remove
#        5. add
#        6. pop
#        7. deal
#        8. is_empty
class Deck:
    def __init__(self):
        self.cards = []
        for s in range(4):
            for r in range(1, 14):
                self.cards.append(Card(s, r))

    def print_deck(self):
        for s in range(4):
            for r in range(1, 14):
                print Card(s, r)


    def shuffle(self):
        import random
        n = len(self.cards)
        for i in range(n/2):
            j = random.randrange(i, n)
            self.cards[i], self.cards[j] = self.cards[j], self.cards[i]


    def remove(self, card):
        if card in self.cards:
            self.cards.remove(card)
            return True
        else:
            return False

    def add(self, card):
        self.cards.append(card)


    def is_empty(self):
        return (len(self.cards) == 0)

    def pop(self):
        return self.cards.pop()

    def deal(self, hands, num_cards=99):
        n = len(hands)
        for i in range(num_cards):
            if self.is_empty(): break

            hand = hands[i % n]
            card = self.pop()
            hand.add(card)


    def remove_matches(self):
        dup_cards = self.cards[:]
        for c in dup_cards:
            for i in range(len(self.cards)):
                if dup_cards.rank == self.cards[i].rank:
                    self.cards.remove(self.cards[i])
                    dup_cards.remove(c)


# Properties of Hand: 
#        1. name of the player
#        2. list of cards
# methods:
#        1. init
#        2. str
#  all methods of Deck
class Hand(Deck):
    def __init__(self, name=""):
        self.name = name
        self.cards = []


    def __str__(self):
        l = len(self.cards)
        s = "Hand for player %s: \n\t" %(self.name)
        if (l <= 0): s += "Empty!!\n"
        else: 
            for i in range(l):
                s += str(self.cards[i]) + "\n\t"

        return s




# CardGame: parent class for OldMaidGame
class CardGame:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()




class OldMaidGame(CardGame):
    pass


# players is a list of objects of Hands
def remove_all_matches(players):
    for player in players:
        player.remove_matches()



# declare the constants
names = ["Adit", "Rishith", "Manu", "Sonu"]
cards_per_player = 10
players = []

# set the deck
deck = Deck()
deck.shuffle()


# initialize the players
for i, name in enumerate(names):
    players.append(Hand(name))
    

# deal the cards to the players
deck.deal(players, cards_per_player*len(players))


# print each player's hand
for player in players:
    print player


# remove matching cards from within each hand
remove_all_matches(players)

