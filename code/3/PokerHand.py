"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""

from Card import *
from collections import Counter


class PokerHand(Hand):

    def suit_hist(self):
        """Builds a histogram of the suits that appear in the hand.

        Stores the result in attribute suits.
        """
        self.suits = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1

    def rank_hist(self):
        self.ranks = Counter([card.rank for card in self.cards])

    def has_pair(self):
        """Returns True if the hand has a pair of cards with same rank, False otherwise.
        """
        return self.has_NofaRank(2)

    def has_twopair(self):
        """Returns True if he hand has a twopair, False otherwise.
        """
        self.rank_hist()
        pairs = 0
        for v in self.ranks.values():
            if pairs == 2:
                return True
            if v >= 2 and pairs < 2:
                pairs += 1
        return False

    def has_NofaRank(self, n):
        self.rank_hist()

        for v in self.ranks.values():
            if v >= n:
                return True
        return False

    def has_threeofakind(self):
        """Returns True if the hand has three cards with the same rank, False otherwise.
        """
        return self.has_NofaRank(3)

    def has_straight(self):
        """Returns True if the hand has five cards with ranks in sequence (aces can be high or low, so Ace-2-3-4-5 is a straight and so is 10-Jack-Queen-King-Ace, but Queen-King-Ace-2-3 is not.), otherwise False.
        """
        self.rank_hist()
        ranks = self.ranks.keys()
        seq = 0
        for i in xrange(1, len(ranks)):
           seq = seq + (1 if ranks[i - 1] + 1 == ranks[i] else 0)
        return True if seq >= 5 else False

    def has_NofaSuit(self, n):
        self.suit_hist()
        for v in self.suits.values():
            if v >=n:
                return True
        return False

    def has_flush(self):
        """Returns True if the hand has a flush, False otherwise.

        Note that this works correctly for hands with more than 5 cards.
        """
        self.suit_hist()
        return self.has_NofaSuit(5)

    def has_fullhouse(self):
        """Returns True if the hand has three cards with one rank, two cards with another, otherwise False.
        """
        return self.has_NofaRank(3) and self.has_NofaRank(2)

    def has_fourofakind(self):
        """Returns True if the hand has four cards with the same rank, otherwise False.
        """
        return self.has_NofaRank(4)

    def has_straightflush(self):
        """Returns True if the hand has five cards in sequence (as defined above) and with the same suit, otherwise False.
        """
        return False

class CheatDeck(Deck):

    def remove_cards_by_rank(self, rank,n):
        arr=[]
        for card in self.cards:
            if card.rank == rank:
                arr.append(card)
                n-=1
            if n==0:
                break
        for card in arr:
            self.remove_card(card)
        return arr
    
    def move_cards_m_n_duplicates_by_rank(self,hand, m,n,T):
        for i in xrange(m):
            card1=self.cards[random.randint(1,len(self.cards)-1)]
            self.remove_card(card1)
            hand.cards+=[card1]+self.remove_cards_by_rank(card1.rank, n-1)
        self.move_cards(hand, T-(m*n))

    def remove_cards_by_suit(self, suit,n):
        arr=[]
        for card in self.cards:
            if n < 0:
                return arr
            if card.suit == suit:
                n-=1
                arr.append(card)
        for card in arr:
            self.remove_card(card)


    def move_cards_n_duplicate_by_suit(self,hand,n,T):
        card1 = self.cards[random.randint(1,len(self.cards))]
        hand.add_card(card1)
        hand.cards+=self.remove_cards_by_suit(card1.suit,n-1)
        self.move_cards(hand, T-n)

    def move_cards_pair(self,hand,n):
        """Moves two cards with the same rank"""
        self.move_cards_m_n_duplicates_by_rank(hand, 1, 2, n)

    def move_cards_two_pair(self, hand, n):
        """Moves two pairs of cards with the same rank"""
        self.move_cards_m_n_duplicates_by_rank(hand, 2, 2, n)

    def move_cards_three_of_a_kind(self,hand,n):
        """Moves three cards with the same rank"""
        self.move_cards_m_n_duplicates_by_rank(hand, 1, 3, n)

    def move_cards_straight(self,hand,n):
        """Move five cards with ranks in sequence (aces can be high or low, so Ace-2-3-4-5 is a straight and so is 10-Jack-Queen-King-Ace, but Queen-King-Ace-2-3 is not.)"""
        card1 = self.remove_cards_by_rank(random.randint(1,10), 1)[0]
        hand.add_card(card1)
        start=card1.rank
        for rank in xrange(start+1,start+5):
            card=self.remove_cards_by_rank(rank, 1)[0]
            hand.add_card(card)
        self.move_cards(hand, 2)

    def move_cards_flush(self,hand,n):
        """Move five cards with the same suit"""
        self.move_cards_n_duplicate_by_suit(hand, 5, 7)

    def move_cards_full_house(self,hand,n):
        """Move three cards with one rank, two cards with another"""
        self.move_cards_m_n_duplicates_by_rank(hand, 1, 3, 3)
        self.move_cards_m_n_duplicates_by_rank(hand, 1, 2, 4)

    def move_cards_four_of_a_kind(self,hand,n):
        """Move four cards with the same rank"""
        self.move_cards_m_n_duplicates_by_rank(hand, 1, 4, n)

    def move_cards_straight_flush(self,hand,n):
        """Move five cards in sequence (as defined above) and with the same suit"""
        suit=random.randint(0,3)
        cds=sorted([ card for card in self.cards if card.suit == suit], key=lambda card: card.rank)
        arr=[]
        for card in cds:
            if len(arr) == 5:
                for card in arr:
                    hand.add_card(card)
                    self.remove_card(card)
                break
            if len(arr) == 0:
                arr.append(card)
                continue
            if arr[-1].rank+1 == card.rank:
                arr.append(card)
            else:
                arr=[]
        self.move_cards(hand, n-5)



if __name__ == '__main__':
    # make a deck
    deck=CheatDeck()
    deck.shuffle()

    # deal the cards and classify the hands
    for i in range(7):
        hand=PokerHand()
        # deck.move_cards(hand, 7)
        # deck.move_cards_flush(hand, 7)
        # deck.move_cards_full_house(hand, 7)
        # deck.move_cards_two_pair(hand, 7)
        deck.move_cards_straight(hand, 7)
        # hand.sort()
        print hand
        # print "flush", hand.has_flush()
        # print "pair", hand.has_pair()
        # print "twopair", hand.has_twopair()
        # print "has_threeofakind", hand.has_threeofakind()
        # print "has_straight", hand.has_straight()
        # print "has_fullhouse", hand.has_fullhouse()
        # print "has_fourofakind", hand.has_fourofakind()
        # print "has_straightflush", hand.has_straightflush()
        print ''
        quit()
