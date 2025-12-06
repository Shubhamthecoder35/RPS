class Game:
    def __init__(self, id):
        self.p1Went = False
        self.p2Went = False
        self.ready = False
        self.id = id
        self.moves = [None, None]
        self.wins = [0, 0]
        self.ties = 0

    def get_player_move(self, p):
        """Returns the move of player p (0 or 1)"""
        return self.moves[p]

    def player(self, player, move):
        """Records the move of player (0 or 1)"""
        self.moves[player] = move
        if player == 0:
            self.p1Went = True
        else:
            self.p2Went = True

    def connected(self):
        """Marks the game as ready when both players are connected"""
        return self.ready

    def bothWent(self):
        """Checks if both players have made their moves"""
        return self.p1Went and self.p2Went

    def winner(self):
        """Determines the winner of the round"""
        # Check if moves are set
        if self.moves[0] is None or self.moves[1] is None:
            return -1
            
        p1 = self.moves[0].upper()[0]
        p2 = self.moves[1].upper()[0]

        winner = -1
        if p1 == "R" and p2 == "S":
            winner = 0
        elif p1 == "S" and p2 == "R":
            winner = 1
        elif p1 == "P" and p2 == "R":
            winner = 0
        elif p1 == "R" and p2 == "P":
            winner = 1
        elif p1 == "S" and p2 == "P":
            winner = 0
        elif p1 == "P" and p2 == "S":
            winner = 1

        return winner

    def resetWent(self):
        """Resets the move status for the next round"""
        self.p1Went = False
        self.p2Went = False
