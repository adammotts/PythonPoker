# Poker Code

import random
import numpy as np
import time

class Cards:
    '''Class for Cards, Deck, and Card Operations'''
    
    # Cards #
    
    '''
    This section of the class represents a card object
    
    Static Attributes:
        ranks (dict): List of all valid ranks and corresponding card rank
        suits (dict): List of all valid suits and corresponding card suit
        
    Instance Attributes:
        rank (int): The numerical representation of the rank of a card
        suit (string): The name of the suit of a card
    '''
    
    ranks = {2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, 11:"J", 12:"Q", 13:"K", 14:"A"}
    suits = {'Club': "♣️", 'Diamond': "♦", 'Heart': "♥️", 'Spade': "♠️"}
    
    def __init__(self, rank, suit):
        
        '''
        Initializes a new card
        
        Arguments:
            rank (int): The numerical representation of the rank of a card
            suit (string): The name of the suit of a card
        '''
        
        self.rank = rank
        self.suit = suit
        
    @property
    def rank(self):
        
        '''
        Gets the rank of a card
    
        Returns:
            int: Card rank
        '''
        
        return self._rank
        
    @rank.setter
    def rank(self, r):
        
        '''
        Sets the rank of a card
    
        Arguments:
            r (int): Card rank
            
        Raises:
            ValueError: If the rank isn't in the ranks dictionary
        '''
        
        if r in Cards.ranks:
            self._rank = r
            
        else:
            raise ValueError("Invalid rank")
        
    @property
    def suit(self):
        
        '''
        Gets the suit of a card
    
        Returns:
            int: Card suit
        '''
        
        return self._suit
    
    @suit.setter
    def suit(self, s):
        
        '''
        Sets the suit of a card
    
        Arguments:
            s (int): Card suit
            
        Raises:
            ValueError: If the suit isn't in the suits dictionary
        '''
        
        if s in Cards.suits:
            self._suit = s
            
        else:
            raise ValueError("Invalid suit")
        
    def __lt__(self, other):
        
        '''
        Checks if the rank of one card is less than that of another; useful for sorting cards
        
        Arguments:
            other (Card): The other card whose rank is to be compared
        
        Returns:
            bool: Whether or not the rank of the first card is less than that of the second
        '''
        
        return self.rank < other.rank
    
    def __str__(self):
        
        '''
        Returns a string representation of a card
        
        Returns:
            str: String representation of a card
        '''
        
        return f'{Cards.ranks.get(self.rank)}{Cards.suits.get(self.suit)}'
    
    # Deck #
    
    '''
    This section of the class represents a deck of cards
    
    Static Attributes:
        deck (list): List of all cards in a deck
    '''
    
    deck = []
    
    def new_deck():
        
        '''
        Resets the deck by clearing and then filling it with all 52 cards
        '''
        
        Cards.deck.clear()
        
        for r in range(2, 15):
            for s in Cards.suits:
                Cards.deck.append(Cards(r, s))
                
    def deal():
        
        '''
        Deals a random card from the deck
        
        Returns:
            Card: A random card in the deck
        '''
        
        c = Cards.deck.pop(random.randint(0, len(Cards.deck) - 1))
        return c
    
    def print_deck():
        
        '''
        Prints the current state of the deck (all cards remaining)
        '''
        
        for c in range (len(Cards.deck)):
            print(Cards.deck[c], end = ' ')
        
        print(f'\nNumber of Cards Remaining: {len(Cards.deck)}')
        
    # Card Operations #
    
    '''
    This section of the class provides functions that help determine the "meaning" of a list of cards in poker
    
    Static Attributes:
        hand_names (dict): List of all integer handstrengths and their corresponding names
    '''
    
    hand_names = {1: "High Card", 2: "Pair", 3: "Two-Pair", 4: "Three of a Kind", 5: "Straight", 6: "Flush", 7: "Full House", 8: "Four of a Kind", 9: "Straight Flush", 10: "Royal Flush"}
    
    def print_list_of_cards(list_of_cards):
        
        '''
        Prints any list of cards
        
        Arguments:
            list_of_cards (list): List of cards to be printed
        '''
        
        for c in range (len(list_of_cards)):
            print(list_of_cards[c], end = ' ')  
    
    def compute_hand_strength(list_of_cards):
        
        '''
        Computes the precise handstrength of any given list of cards
        
        Arguments:
            list_of_cards: Poker hand to be analyzed
        
        Returns:
            float: Decimal representation of a poker hand's strength
        '''
        
        # Collect a list of all cards' ranks
        list_of_ranks = []
        for c in range (len(list_of_cards)):
            list_of_ranks.append(list_of_cards[c].rank)
        
        # Collect a list of unique ranks and their frequencies within the list of cards
        unique_ranks, unique_rank_frequencies = np.unique(np.array(list_of_ranks), return_counts = True)
        frequencies = sorted(zip(unique_ranks, unique_rank_frequencies))
        
        # Create a separate copy used for "kickers"
        kickers = sorted(unique_ranks).copy()
        
        # Collect a list of suits and their frequencies within the list of cards
        list_of_suits = []
        for c in range (len(list_of_cards)):
            list_of_suits.append(list_of_cards[c].suit)
        unique_suits, unique_suit_frequencies = np.unique(np.array(list_of_suits), return_counts = True)
        
        # Straight and Royal Flush
        higher_end_of_straight = 14
        for s in Cards.suits:
            while higher_end_of_straight >= 5:
                count = 0
                for c in range (len(list_of_cards)):
                    if higher_end_of_straight == 5:
                        if (list_of_ranks[c] == 14 and list_of_suits[c] == s):
                            count += 1  
                    else:
                        if (list_of_ranks[c] == higher_end_of_straight - 4 and list_of_suits[c] == s):
                            count += 1                    
                    if (list_of_ranks[c] == higher_end_of_straight - 3 and list_of_suits[c] == s):
                        count += 1
                    if (list_of_ranks[c] == higher_end_of_straight - 2 and list_of_suits[c] == s):
                        count += 1
                    if (list_of_ranks[c] == higher_end_of_straight - 1 and list_of_suits[c] == s):
                        count += 1
                    if (list_of_ranks[c] == higher_end_of_straight and list_of_suits[c] == s):
                        count += 1
                if count == 5:
                    if higher_end_of_straight == 14:
                        return 10.0
                    else:
                        return 9 + higher_end_of_straight / 100                    
                higher_end_of_straight -= 1
        
        # Quads and Full House
        for f in range (len(frequencies) -1, -1, -1):
            if frequencies[f][1] == 4:
                kickers.remove(frequencies[f][0])
                return 8 + frequencies[f][0] / 100 + kickers[-1] / 10000
            if frequencies[f][1] == 3:
                for kf in range (len(frequencies) -1, -1, -1):
                    if frequencies[kf][1] >= 2 and kf != f:
                        return 7 + frequencies[f][0] / 100 + frequencies[kf][0] / 10000
    
        # Flush
        for f in range (len(unique_suit_frequencies)):
            if unique_suit_frequencies[f] >= 5:
                flush_suit = unique_suits[f]
                flush_cards = []
                for c in range (len(list_of_cards)):
                    if list_of_cards[c].suit == flush_suit:
                        flush_cards.append(list_of_cards[c])
                flush_cards.sort()
                return 6 + flush_cards[-1].rank / 100 + flush_cards[-2].rank / 10000 + flush_cards[-3].rank / 1000000 + flush_cards[-4].rank / 100000000 + flush_cards[-5].rank / 10000000000
        
        # Straight
        higher_end_of_straight = 14
        while higher_end_of_straight >= 5:
            if higher_end_of_straight == 5:
                if 5 in list_of_ranks and 4 in list_of_ranks and 3 in list_of_ranks and 2 in list_of_ranks and 14 in list_of_ranks:
                    return 5.05
                
            else:
                if higher_end_of_straight in list_of_ranks and higher_end_of_straight-1 in list_of_ranks and higher_end_of_straight-2 in list_of_ranks and higher_end_of_straight-3 in list_of_ranks and higher_end_of_straight-4 in list_of_ranks:
                    return 5 + higher_end_of_straight / 100                    
            higher_end_of_straight -= 1
            
        # Trips, Two Pair, and Pair
        for f in range (len(frequencies) -1, -1, -1):
            if frequencies[f][1] == 3:
                kickers.remove(frequencies[f][0])
                return 4 + frequencies[f][0] / 100 + kickers[-1] / 10000 + kickers[-2] / 1000000
            if frequencies[f][1] == 2:
                kickers.remove(frequencies[f][0])
                for kf in range (len(frequencies) -1, -1, -1):
                    if frequencies[kf][1] == 2 and kf != f:
                        kickers.remove(frequencies[kf][0])
                        return 3 + frequencies[f][0] / 100 + frequencies[kf][0] / 10000 + kickers[-1] / 1000000
                return 2 + frequencies[f][0] / 100 + kickers[-1] / 10000 + kickers[-2] / 1000000 + kickers[-3] / 100000000
                    
        # High Card
        return 1 + kickers[-1] / 100 + kickers[-2] / 10000 + kickers[-3] / 1000000 + kickers[-4] / 100000000 + kickers[-5] / 10000000000

class Players:
    '''Class for Players and the Game'''
    
    # Player #
    
    '''
    This section of the class represents a player object
    
    Instance Attributes:
        name (str): The name of a player
        stack (float): Dollars left in chips
        dealer (bool): Whether or not the player is currently the dealer
        small_blind (bool): Whether or not the player is currently the small blind
        big_blind (bool): Whether or not the player is currently the big blind
        all_in (bool): Whether or not the player is currently all in
        folded (bool): Whether or not the player is currently folded
        out (bool): Whether or not the player is currently out
        bet (float): Dollars bet in chips
        holdings (list): List of hole cards
        hand (list): List of hole cards plus community cards
        hand_strength (float): The decimal representation of the strength of a player's hand
        side_pot (float): Maximum of dollars in chips that a player is entitled to based on bets
    '''
    
    def __init__(self, name):
        '''
        Initializes a new player
        
        Arguments:
            name (str): The name of a player
        '''
        
        self.name = name
        self.stack = 500.0
        self.dealer = False
        self.small_blind = False
        self.big_blind = False
        self.all_in = False
        self.folded = False
        self.out = False
        self.bet = 0.0
        self.holdings = []
        self.hand = []
        self.hand_strength = 0.0
        self.side_pot = 0.0
        
        Players.list_of_players.append(self)
    
    def __lt__(self, other):
        
        '''
        Checks if the handstrength of one player is less than that of another; useful for sorting players by strength
        
        Arguments:
            other (Player): The other player whose handstrength is to be compared
            
        Returns:
            bool: Whether or not the handstrength of one player is less than that of another
        '''
        
        return self.hand_strength < other.hand_strength
        
    def __str__(self):
        
        '''
        Returns a string representation of a player
        
        Returns:
            str: String representation of a player
        '''
        
        return f'{self.name}: Stack = {self.stack}, ({self.dealer}, {self.small_blind}, {self.big_blind}), ({self.all_in}, {self.folded}, {self.out}), Bet = {self.bet}, Hand ='

    def reset_player_status(self):
        
        '''
        Restores a player's status back to default for a new round
        '''
        
        self.dealer = False
        self.small_blind = False
        self.big_blind = False
        self.all_in = False
        self.folded = False
        self.out = False
        self.bet = 0.0
        self.holdings.clear()
        self.hand.clear()
        self.hand_strength = 0.0
        self.side_pot = 0.0
    
    def action_call(self):
        
        '''
        Calls the round bet. If the player's stack isn't enough to call, sets the player to all in
        '''
        
        if self.stack <= Players.round_bet:
            self.all_in = True
            self.bet = self.stack
            print(f'{self.name} is ALL IN for {self.bet}')
            
        else:
            self.bet = Players.round_bet
            print(f'{self.name} calls the previous bet of {Players.round_bet}')
            
    def action_check(self):
        
        '''
        Checks the action
        '''
        
        print(f'{self.name} checks')
     
    def action_bet(self):
        
        '''
        Bets the specified amount, and changes the round bet to the bet. If the player's stack is
        less than the bet, sets the player to all in. Restores the number of players left to act
        to the number of non-folded players
        '''
        
        bet_amount = int(input("How much would you like to bet?"))
        
        if self.stack <= bet_amount:
            self.all_in = True
            self.bet = self.stack
            print(f'{self.name} is ALL IN for {self.stack}')
            
        else:
            self.bet = bet_amount
            print(f'{self.name} bets {bet_amount}')
            
        Players.round_bet = self.bet
        Players.number_of_players_left_to_act = len(Players.list_of_active_players)
           
    def action_raise(self):
        
        '''
        Raises the specified amount, and changes the round bet to the bet. If the player's stack is
        less than the bet, sets the player to all in. Restores the number of players left to act
        to the number of non-folded players
        '''
        
        raise_amount = int(input("How much would you like to raise to?"))
        
        if self.stack <= raise_amount:
            self.all_in = True
            self.bet = self.stack
            print(f'{self.name} is ALL IN for {self.stack}')
            
        elif raise_amount <= Players.round_bet:
            print(f'Invalid raise')
        
        else:
            self.bet = raise_amount
            print(f'{self.name} raises to {raise_amount}')
        
        Players.round_bet = self.bet
        Players.number_of_players_left_to_act = len(Players.list_of_active_players)
            
    def action_fold(self):
        
        '''
        Folds the action. Removes the player from the list of active players. Sets folded to true
        '''
        
        self.folded = True
        Players.list_of_active_players.remove(self)
        print(f'{self.name} folds')
        
    def can_check(self):
        
        '''
        Returns whether or not the player can check
        
        Returns:
            bool: Whether or not the player can check
        '''
        
        if (Players.round_bet == 0) or (self.big_blind and Players.round_bet == 5):
            return True
        
        else:
            return False
        
    def can_act_pre_flop(self):
        
        '''
        Returns whether or not the player can act preflop
        
        Returns:
            bool: Whether or not the player can act preflop
        '''
        
        if (not(self.folded or self.all_in or self.out) and (self.bet < Players.round_bet or (self.big_blind and Players.round_bet == 5))):
            return True
        
        else:
            return False
        
    def can_act_post_flop(self):
        
        '''
        Returns whether or not the player can act postflop
        
        Returns:
            bool: Whether or not the player can act postflop
        '''
        
        if (not(self.folded or self.all_in or self.out) and (self.bet < Players.round_bet or (self.bet == 0 and self.bet == Players.round_bet))):
            return True
        
        else:
            return False
        
    def is_out(self):
        
        '''
        Checks if the player is bankrupt, and returns the modified status accordingly
        
        Returns:
            bool: Whether or not the player is bankrupt
        '''
        
        if self.stack == 0:
            self.out = True
            
        return self.out
    
    def individual_side_pot(self):
        
        '''
        Generates a sidepot for the player        
        '''
        
        for b in range (len(Players.list_of_players)):
            if self.bet >= Players.list_of_players[b].bet:
                self.side_pot += Players.list_of_players[b].bet
                
            else:
                self.side_pot += self.bet
              
    def input_pre_flop(self):
        
        '''
        Ask players for their input preflop depending on circumstances and modifies the number of players left to act accordingly
        '''
        
        if self.can_act_pre_flop() == True:
            if self.can_check() == False:
                choice = int(input((f'It\'s {self.name}\'s turn to act. Would you like to (1)Call {Players.round_bet}, (2)Raise, or (3)Fold?')))
                match choice:
                    case 1:
                        self.action_call()
                    case 2:
                        self.action_raise()
                    case 3:
                        self.action_fold()
                    case _:
                        self.action_fold()
                        
            else:
                choice = int(input((f'It\'s {self.name}\'s turn to act. Would you like to (1)Check, (2)Raise, or (3)Fold?')))
                match choice:
                    case 1:
                        self.action_check()
                    case 2:
                        self.action_raise()
                    case 3:
                        self.action_fold()
                    case _:
                        self.action_fold()
                
        Players.number_of_players_left_to_act -= 1
    
    def input_post_flop(self):
        
        '''
        Ask players for their input postflop depending on circumstances and modifies the number of players left to act accordingly
        '''
        
        if self.can_act_post_flop() == True:
            if self.can_check() == False:
                choice = int(input((f'It\'s {self.name}\'s turn to act. Would you like to (1)Call {Players.round_bet}, (2)Raise, or (3)Fold?')))
                match choice:
                    case 1:
                        self.action_call()
                    case 2:
                        self.action_raise()
                    case 3:
                        self.action_fold()
                    case _:
                        self.action_fold()
                        
            else:
                choice = int(input((f'It\'s {self.name}\'s turn to act. Would you like to (1)Check, (2)Bet, or (3)Fold?')))
                match choice:
                    case 1:
                        self.action_check()
                    case 2:
                        self.action_bet()
                    case 3:
                        self.action_fold()
                    case _:
                        self.action_fold()
                
        Players.number_of_players_left_to_act -= 1
    
    # Game #
    
    '''
    This section of the class represents a game of poker
    
    Static Attributes:
        list_of_players (list): List of players in the game
        list_of_active_players (list): List of all non-folded players in a hand (mostly for pot awarding purposes, not betting)
        number_of_players_left_to_act (int): Number of players who can still act
        round_in_progress (bool): Whether or not a round is currently in progress
        community_cards (list): List of community cards
        dealer_index (int): The index of the dealer
        small_blind_index (int): The index of the small blind
        big_blind_index (int): The index of the big blind
        round_number (int): The round number
        pot_size (float): The total pot comprised of all players' bets
        round_bet (float): The largest bet that has occurred on a single street of betting
    '''
    
    list_of_players = []
    list_of_active_players = []
    number_of_players_left_to_act = 0
    round_in_progress = True
    community_cards = []
    dealer_index = 0
    small_blind_index = 0
    big_blind_index = 0
    round_number = 0
    pot_size = 0.0
    round_bet = 0.0
    
    def pre_flop_betting_sequence():
        
        '''
        Starting from the player after the big blind, commence action
        '''
        
        current_player = (Players.big_blind_index + 1) % len(Players.list_of_players)
        while (Players.number_of_players_left_to_act > 0):
            if (len(Players.list_of_active_players) == 1):
                break
            
            else:
                Players.list_of_players[current_player].input_pre_flop()                        
                current_player = (current_player + 1) % len(Players.list_of_players)
                time.sleep(0.1)
                    
    def post_flop_betting_sequence():
        
        '''
        Starting from the small blind, commence action
        '''
        
        current_player = (Players.small_blind_index) % len(Players.list_of_players)
        while (Players.number_of_players_left_to_act > 0):
            if (len(Players.list_of_active_players) == 1):
                break
            
            else:
                Players.list_of_players[current_player].input_post_flop()                        
                current_player = (current_player + 1) % len(Players.list_of_players)
                time.sleep(0.1)
                
    def start_game():
        
        '''
        Starts the game: ask how many players will be playing, add each to the game, pick a random starting dealer,
        and start a new round (also counting the total, stopping after 100 rounds)
        '''
        
        number_of_players = int(input("How many players will be playing?"))
        
        if number_of_players < 3:
            raise ValueError("Need at least 3 players for a game")

        for k in range(number_of_players):
            time.sleep(0.1)
            new_name = input(f'Enter the name of player {k+1}:')
            Players(new_name)
            
        Players.dealer_index = random.randint(0, (len(Players.list_of_players)) - 1)
        
        while Players.round_number < 100:
            Players.pre_flop()
            if (Players.round_in_progress == False):
                continue            
            
            Players.flop()
            if (Players.round_in_progress == False):
                continue          
                
            Players.turn()
            if (Players.round_in_progress == False):
                continue           
                
            Players.river()
    
    def pre_flop():
        
        '''
        Preflop action sequence: reset the deck, reset players, check if any players are bankrupt and
        provide the option to rebuy, reset the status of the game, move the blinds, deal cards, print
        players, commence action, collect side pots, collect main pot, and check if one player remains
        '''
        
        Cards.new_deck()
        
        for p in range(len(Players.list_of_players)):
            Players.list_of_players[p].reset_player_status()
            
        Players.re_buy()
        
        Players.community_cards.clear()
        Players.list_of_active_players = Players.list_of_players.copy()
        Players.number_of_players_left_to_act = len(Players.list_of_players)
        Players.round_in_progress = True
        Players.round_number += 1
        Players.pot_size = 0.0
        Players.round_bet = 5
        
        Players.dealer_index = (Players.dealer_index + 1) % len(Players.list_of_players)
        Players.list_of_players[Players.dealer_index].dealer = True
        Players.small_blind_index = (Players.dealer_index + 1) % len(Players.list_of_players)
        Players.list_of_players[Players.small_blind_index].small_blind = True
        Players.list_of_players[Players.small_blind_index].bet = 2.0
        Players.big_blind_index = (Players.small_blind_index + 1) % len(Players.list_of_players)
        Players.list_of_players[Players.big_blind_index].big_blind = True
        Players.list_of_players[Players.big_blind_index].bet = 5.0
        
        print('\n\nDealing Cards...\n\n')
        time.sleep(0.5)
        
        for c in range(0, 2):
            current_player = Players.small_blind_index
            for p in range (len(Players.list_of_players)):
                Players.list_of_players[current_player].holdings.append(Cards.deal())
                current_player = (current_player + 1) % len(Players.list_of_players)
                
        Players.print_all_players()
        
        Players.pre_flop_betting_sequence()
        
        Players.set_side_pots()        
        Players.set_pot()
        Players.folded_pot()
        
    def flop():
        
        '''
        Flop action sequence: deal 3 community cards, print players, commence action, collect side pots,
        collect main pot, and check if one player remains
        '''
        
        print('\n\nDealing The Flop...\n\n')
        time.sleep(0.5)
        
        Players.round_bet = 0
        Players.number_of_players_left_to_act = len(Players.list_of_players)
        Players.reset_bets()
        
        Cards.deal()
        Players.community_cards.append(Cards.deal())
        Players.community_cards.append(Cards.deal())
        Players.community_cards.append(Cards.deal())
        Players.update_player_hands()
        Players.print_game()
            
        Players.print_all_players()           
        Cards.print_deck()
        
        Players.post_flop_betting_sequence()
            
        Players.set_side_pots()
        Players.set_pot()
        Players.folded_pot()
            
    def turn():
        
        '''
        Turn action sequence: deal 1 community card, print players, commence action, collect side pots,
        collect main pot, and check if one player remains
        '''
        
        print('\n\nDealing The Turn...\n\n')
        time.sleep(0.5)
        
        Players.round_bet = 0
        Players.number_of_players_left_to_act = len(Players.list_of_players)
        Players.reset_bets()
        
        Cards.deal()
        Players.community_cards.append(Cards.deal())
        Players.update_player_hands()
        Players.print_game()
        
        Players.print_all_players()           
        Cards.print_deck()
        
        Players.post_flop_betting_sequence()
        
        Players.set_side_pots()
        Players.set_pot()
        Players.folded_pot()
            
    def river():
        
        '''
        River action sequence: deal 1 community card, print players, commence action, collect side pots,
        collect main pot, check if one player remains, then award sidepots to winners organized by handstrength
        '''
        
        print('\n\nDealing The River...\n\n')
        time.sleep(0.5)
        
        Players.round_bet = 0
        Players.number_of_players_left_to_act = len(Players.list_of_players)
        Players.reset_bets()
        
        Cards.deal()
        Players.community_cards.append(Cards.deal())
        Players.update_player_hands()
        Players.print_game()
        
        Players.print_all_players()           
        Cards.print_deck()
        
        Players.post_flop_betting_sequence()
        
        Players.set_side_pots()
        Players.set_pot()
        Players.folded_pot()
        
        if (Players.round_in_progress == True):
            Players.award_pots()
    
    
    def update_player_hands():
        
        '''
        Updates each player hand to be the combination of the community cards and their personal holdings
        '''
        
        for p in range (len(Players.list_of_players)):
            Players.list_of_players[p].hand.clear()
            Players.list_of_players[p].hand.extend(Players.community_cards)
            Players.list_of_players[p].hand.extend(Players.list_of_players[p].holdings)
            
    def re_buy():
        
        '''
        Gives players the option to rebuy if they are bankrupt
        '''
        
        for p in range (len(Players.list_of_players) -1, -1, -1):
            if (Players.list_of_players[p].is_out()):
                print('\n\n')
                choice = input(f'{Players.list_of_players[p].name}, you are out of chips. Would you like to rebuy for $500 more? Type \'Yes\' or \'No\'')
                if choice == 'Yes':
                    Players.list_of_players[p].stack = 500
                    Players.list_of_players[p].out = False
                    Players.list_of_players[p].all_in = False
                else:
                    Players.list_of_players.remove(Players.list_of_players[p])
                    if (len(Players.list_of_players) < 3):
                        print('Not enough players to continue the game')
                        quit()
                        
    def folded_pot():
        
        '''
        Checks if there is only one player remaining. If so, then award the pot
        '''
        
        if (len(Players.list_of_active_players) == 1):
            time.sleep(0.5)
            print('\n\n')
            
            Players.list_of_active_players[0].stack += Players.list_of_active_players[0].side_pot
            print(f'{Players.list_of_active_players[0].name} wins a pot of ${Players.pot_size}')
            Players.round_in_progress = False
    
    def reset_bets():
        
        '''
        Resets all players' bets
        '''
        
        for p in range (len(Players.list_of_players)):
            Players.list_of_players[p].bet = 0
    
    def set_side_pots():
        
        '''
        Calculates side pots for all players
        '''
        
        for p in range (len(Players.list_of_active_players)):
            Players.list_of_active_players[p].individual_side_pot()
    
    def set_pot():
        
        '''
        Collects the main pot
        '''
        
        for p in range (len(Players.list_of_players)):
            Players.list_of_players[p].stack -= Players.list_of_players[p].bet
            Players.pot_size += Players.list_of_players[p].bet
    
    def award_pots():
        
        '''
        Awards pots to winners based on rank of handstrengths as well as side pots
        '''
        
        print('\n')
        time.sleep(0.5)
        
        for p in range (len(Players.list_of_active_players)):
            Players.list_of_active_players[p].hand_strength = Cards.compute_hand_strength(Players.list_of_active_players[p].hand)
        
        hierarchy = sorted(Players.list_of_active_players)
        
        count = -1
        while Players.pot_size > 0:
            winners = []
            for p in range (len(hierarchy)):
                if hierarchy[p].hand_strength == hierarchy[count].hand_strength:
                    winners.append(hierarchy[p])
            
            temporary_pot_size = Players.pot_size
            for p in range (len(winners)):
                minimum = min(winners[p].side_pot, temporary_pot_size)
                # TODO: Instead of dividing by length, subtract bets of all other tied winners. Keep track of bets with list of bets instead of resetting? 
                winners[p].stack += minimum / len(winners)
                if minimum / len(winners) > 0:
                    print(f'{winners[p].name} wins ${minimum / len(winners)} with a {Cards.hand_names.get((int)(winners[p].hand_strength))}')                                   
                Players.pot_size -= minimum / len(winners)
                count -= 1
            
            for p in range (len(hierarchy)):
                hierarchy[p].side_pot -= minimum
        
    def print_game():
        
        '''
        Prints the board and the potsize
        '''
        
        print(f'The board is: ', end = '')
        Cards.print_list_of_cards(Players.community_cards)
        print(f'\nThe pot is ${Players.pot_size}')
    
    def print_all_players():
        
        '''
        Prints all players in the game
        '''
        
        for p in range (len(Players.list_of_players)):
            print(Players.list_of_players[p], end = ' ')
            Cards.print_list_of_cards(Players.list_of_players[p].holdings)
            print()
          
Players.start_game()