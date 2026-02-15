class CreateBoard:
    def __init__(self):
        self.player_table = [[" ", "A" , "B" , "C" , "D" , "E" , "F"],
                            ["1" , "." , "." , "." , "." , "." , "."],
                            ["2" , "." , "." , "." , "." , "." , "."],
                            ["3" , "." , "." , "." , ".", "." , "."],
                            ["4" , "." , "." , "." , "." , "." , "."],
                            ["5" , "." , "." , "." , "." , "." , "."],
                            ["6" , "." , "." , "." , "." , "." , "."]]

        self.targeting_table =[[" ", "A" , "B" , "C" , "D" , "E" , "F"],
                            ["1" , "." , "." , "." , "." , "." , "."],
                            ["2" , "." , "." , "." , "." , "." , "."],
                            ["3" , "." , "." , "." , ".", "." , "."],
                            ["4" , "." , "." , "." , "." , "." , "."],
                            ["5" , "." , "." , "." , "." , "." , "."],
                            ["6" , "." , "." , "." , "." , "." , "."]]

    def __str__ (self):
        table = []
        for i in range(7):
            table.append(" ".join(self.player_table[i]) + "\t" + "\t" + " ".join(self.targeting_table[i]))
        return "\n".join(table)

    def place_simbol(self , x , y):
        self.player_table[x][y] = "+"

    def hit_simbol(self , x , y):
        self.targeting_table[x][y] = "O"

    def print_table(self):
        return self.player_table

