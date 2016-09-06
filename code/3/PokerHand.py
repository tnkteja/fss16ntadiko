"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""
from __future__ import division
from Card import *
from collections import Counter
import sys
from test_PokerHand import *
sys.dont_write_bytecode=True

class ClassName(object):
    """docstring for ClassName"""

        
class PokerHand(Hand):
    """PokerHand class"""

    def __init__(self):
        super(PokerHand, self).__init__()
        self.ranks,self.suits = {},{}

    def suit_hist(self):
        """Builds a histogram of the suits that appear in the hand.

        Stores the result in attribute suits.
        """
        self.suits = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1

    def rank_hist(self):
        """Builds a histogram of the ranks that appear in the hand.

        Stores the result in attribute ranks.
        """
        self.ranks = Counter([card.rank for card in self.cards])

    def has_1_pair(self):
        """Returns True if the hand has a pair of cards with same rank, False otherwise.
        """
        return self._has_NofaRank(2)

    def has_2_two_pair(self):
        """Returns True if he hand has a twopair, False otherwise.
        """
        if not self.ranks:
            self.rank_hist()
        return Counter(self.ranks.values())[2] ==2 
      

    def _has_NofaRank(self, n):
        if not self.ranks:
            self.rank_hist()

        for v in self.ranks.values():
            if v >= n:
                return True
        return False

    def has_3_three_of_a_kind(self):
        """Returns True if the hand has three cards with the same rank, False otherwise.
        """
        return self._has_NofaRank(3)

    def has_4_straight(self):
        """Returns True if the hand has five cards with ranks in sequence (aces can be high or low, so Ace-2-3-4-5 is a straight and so is 10-Jack-Queen-King-Ace, but Queen-King-Ace-2-3 is not.), otherwise False.
        """
        if not self.ranks:
            self.rank_hist()

        ranks = self.ranks.keys()
        if len(ranks)<5:
            return False
        seq = 1
        for i in xrange(1, len(ranks)):
           seq = (seq + 1) if ranks[i - 1] + 1 == ranks[i] else 1
        return True if seq >= 5 else False

    def _has_NofaSuit(self, n):
        if not self.suits:
            self.suit_hist()
        for v in self.suits.values():
            if v >=n:
                return True
        return False

    def has_5_flush(self):
        """Returns True if the hand has a flush, False otherwise.

        Note that this works correctly for hands with more than 5 cards.
        """
        return self._has_NofaSuit(5)

    def has_6_full_house(self):
        """Returns True if the hand has three cards with one rank, two cards with another, otherwise False.
        Note: A Veener method calling self._has_NofaRank(arg)
        """
        twokind,threekind=False,False
        for k,v in self.ranks.iteritems():
            if v == 2:
                twokind=True
            if v== 3:
                threekind=True
            if twokind and threekind:
                return True
        return False


    def has_7_four_of_a_kind(self):
        """Returns True if the hand has four cards with the same rank, otherwise False.
        Note: A Veener method calling self._has_NofaRank(arg)
        """
        return self._has_NofaRank(4)

    def has_8_straight_flush(self):
        """Returns True if the hand has five cards in sequence (as defined above) and with the same suit, otherwise False.
        Note: A Veener method calling self._has_NofaRank(arg)
        """
        if not self.suits:
            self.suit_hist()
        for k,v in self.suits.iteritems():
            if v>=5:
               for v in Counter([ card.rank for card in self.cards if card.suit == k]).values():
                if v is not 1:
                    return False
               return True
        return False

    def classify(self):
        self.labels=[]
        for method in reversed([ attribute for attribute in dir(self) if "has" == attribute[:3]]):
            if getattr(self, method)():
                self.labels.append(method[6:])
        return self.labels


def probabilities(trails=1000,N=7):
    labels=[]
    for i in xrange(trails):
        deck=Deck()
        deck.shuffle()
        for hand in [ PokerHand() for i in xrange(int(52/N)) ]:
            deck.move_cards(hand, N)
            if hand.classify():
                labels+=hand.labels
    hist=Counter(labels)
    total= sum(hist.values())
    for k,v in hist.iteritems():
        hist[k]=v/total
    print sorted([(k,v) for k,v in hist.iteritems()],key=lambda x:  x[1])


if __name__ == '__main__':
    probabilities(trails=1000,N=5)
    quit()
    # make a deck
    deck=CheatDeck()
    deck.shuffle()
    # deal the cards and classify the hands
    for i in range(7):
        hand=PokerHand()
        deck.move_cards_straight_flush(hand, 7)
        hand.classify()
        print hand.label
        #hand.sort()
        print hand
        print hand.has_8_straight_flush()
        print ''
        quit()

