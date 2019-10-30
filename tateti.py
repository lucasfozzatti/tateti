

class TaTeTi():

    def __init__(self, board=None):

        if board is None:

            self.board = [' ' for _ in range(9)]

        else:

            self.board = board