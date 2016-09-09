#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
test_1_PokerHand


"""
import unittest
from PokerHand import *
from Card import *
import sys
sys.dont_write_bytecode=True

class Test_PokerHand(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
    	pass
    
    def setUp(self):
        print "\n-----| %s |-----------------------"%(self._testMethodName)
        self.cheatDeck=CheatDeck()
        self.cheatDeck.shuffle()
        self.hand=PokerHand()

    def test_1_has_pair(self):
        self.cheatDeck.move_cards_pair(self.hand, 5)
        self.hand.classify()
        print self.hand
        print self.hand.labels
        self.assertTrue(self.hand.has_1_pair())


    def test_2_has_two_pair(self):
        self.cheatDeck.move_cards_two_pair(self.hand, 5)
        self.hand.classify()
        print self.hand
        print self.hand.labels
        self.assertTrue(self.hand.has_2_two_pair())


    def test_3_three_of_a_kind(self):
        self.cheatDeck.move_cards_three_of_a_kind(self.hand, 5)
        self.hand.classify()
        print self.hand
        print self.hand.labels
        self.assertTrue(self.hand.has_3_three_of_a_kind())

    def test_4_straight(self):
        self.cheatDeck.move_cards_straight(self.hand, 5)
        self.hand.classify()
        print self.hand
        print self.hand.labels
        self.assertTrue(self.hand.has_4_straight())

    def test_5_flush(self):
        self.cheatDeck.move_cards_flush(self.hand, 5)
        self.hand.classify()
        print self.hand
        print self.hand.labels
        self.assertTrue(self.hand.has_5_flush())


    def test_6_full_house(self):
        self.cheatDeck.move_cards_full_house(self.hand, 5)
        self.hand.classify()
        print self.hand
        print self.hand.labels
        self.assertTrue(self.hand.has_6_full_house())


    def test_7_four_of_a_kind(self):
        self.cheatDeck.move_cards_four_of_a_kind(self.hand, 5)
        self.hand.classify()
        print self.hand
        print self.hand.labels
        self.assertTrue(self.hand.has_7_four_of_a_kind())


    def test_8_straight_flush(self):
        self.cheatDeck.move_cards_straight_flush(self.hand, 5)
        self.hand.classify()
        print self.hand
        print self.hand.labels
        self.assertTrue(self.hand.has_8_straight_flush())


    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

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
        ranks=random.sample(xrange(1,14), 5)
        for i in ranks[:2]:
        	hand.cards+=self.remove_cards_by_rank(i, 2)
        for i in ranks[3:]:
        	hand.cards+=self.remove_cards_by_rank(i, 1)

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
        hand.shuffle()

    def move_cards_flush(self,hand,n):
        """Move five cards with the same suit"""
        self.move_cards_n_duplicate_by_suit(hand, 5, n)
        self.move_cards(hand,-5)

    def move_cards_full_house(self,hand,n):
        """Move three cards with one rank, two cards with another"""
        self.move_cards_m_n_duplicates_by_rank(hand, 1, 3, 3)
        self.move_cards_m_n_duplicates_by_rank(hand, 1, 2, n-3)
        hand.shuffle()

    def move_cards_four_of_a_kind(self,hand,n):
        """Move four cards with the same rank"""
        self.move_cards_m_n_duplicates_by_rank(hand, 1, 4, n)
        hand.shuffle()

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
	tl=unittest.TestLoader()
	tl.sortTestMethodsUsing=None
	unittest.main(verbosity=5)

"""
MIT License

Copyright (c) 2016 Neela Krishna Teja Tadikonda

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""