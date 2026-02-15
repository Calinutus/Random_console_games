from Battleship.Core import GameLogic



class UI:
    def __init__(self):
        self.logic = GameLogic()

    def start_menu(self):
        print("Welcome to BATTLESHIP")
        print(self.logic.repo)

    def main(self):
        self.start_menu()
        cnt = 1
        boat1 = ""
        boat2 = ""
        print("\nIf you need help type the command \033[1m help \033[0m ")
        print("Place 2 ships on the board using the command \033[1m ship \033[0m (3 blocks) then type the command \033[1m start \033[0m to start the game\n")
        while True:
            try:
                start_command = input("cmd> ")
            except ValueError:
                print("Invalid command. Please try again.")
                continue

            cmd = start_command.strip().upper()

            if cmd == "SHIP":
                letter_list = self.logic.define_pos()
                cnt += 1
                while True:
                    ship = input(f"Ship pos: ")
                    if len(ship) != 6:
                        print("Invalid ship pos. Please try again.")
                        continue
                    elif ship[0] not in letter_list.keys() or ship[2] not in letter_list.keys() or ship[4] not in letter_list.keys():
                        print("Invalid ship pos. Please try again.")
                        continue
                    try:
                        if int(ship[1]) not in letter_list.values() or int(ship[3]) not in letter_list.values() or int(
                                ship[5]) not in letter_list.values():
                            print("Invalid ship pos. Please try again.")
                            continue
                    except ValueError:
                        print("Invalid ship pos. Please try again.")
                        continue
                    if not self.logic.convert(ship):
                        print("Invalid ship pos. Please try again.")
                        continue
                    if cnt % 2 == 0:
                        boat2 = ship
                    else:
                        boat1 = ship
                    if boat1 != "" and boat2 != "":
                        if not self.logic.bool_boat_pos(boat1, boat2):
                            print("Invalid ship pos. Please try again.")
                            continue
                    break


            if cmd == "START":
                self.logic.place_ai_boats()
                while True:
                    if boat1 == "" and boat2 == "":
                        boat1 = self.logic.random_pos()
                        boat2 = self.logic.random_pos()
                        if not self.logic.bool_boat_pos(boat1, boat2):
                            continue
                    break
                while True:
                        boat3 = self.logic.random_pos()
                        boat4 = self.logic.random_pos()
                        if not self.logic.bool_boat_pos(boat3, boat4):
                            continue
                        break
                self.logic.set_boat_pos(boat1, boat2)
                print(self.logic)
                print("Attack phase(set pos to attack): ")
                player_moves = []
                while True:
                    player_shot = input(f"Choose attack: ").strip().upper()

                    if not self.logic.valid_attack(player_shot):
                        print("Invalid attack")
                        continue

                    if player_shot in player_moves:
                        print("Already attacked")
                        continue

                    player_moves.append(player_shot)

                    self.logic.apply_player_attack(player_shot)
                    ai_shot = self.logic.ai_attacks()
                    print(f"\nAI attacks: {ai_shot} \n")
                    self.logic.apply_ai_attack(ai_shot)
                    print(self.logic)

                    winner = self.logic.check_win()

                    if winner == "PLAYER":
                        print("You win")
                        return

                    if winner == "AI":
                        print("AI win")
                        return



            if cmd == "HELP":
                print("\nship - Put a ship on the board(max 3 block)(ex: A1A2A3 , C3D3E3)")
                print("start - If you put the ships already the game will start | if not the game chooses random position for the 2 boats")
                print("attack (after placing the ships) - The function to start the attack at a set coordinate(max 1 block) (ex: A2 , B4 , C1)\n")

            if cmd == "EXIT":
                break

if __name__ == "__main__":
    UI = UI()
    UI.main()
