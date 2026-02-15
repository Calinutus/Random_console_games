class RoundManagement:
    def __init__(self):
        self.turn = "red"

    def switch_turn(self):
        """
        Switches the turn based on the current turn color.
        :return: The current turn color.
        """
        if self.turn == "red":
            self.turn = "white"
        else:
            self.turn = "red"