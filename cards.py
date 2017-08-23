#!/usr/bin/env python

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
        print "num cards: %d" %n
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


class CardGame:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()




if __name__ == '__main__':
    #c1 = Card(3, 11)

    d1 = Deck()
    #d1.print_deck()

    d1.shuffle()

    play_hands = []
    p1 = Hand("Adit")
    p2 = Hand("Rishith")

    play_hands.append(p1)
    play_hands.append(p2)

    d1.deal(play_hands, 10)

    print p1
    print p2

