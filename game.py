import customtkinter
from display.displayGUI import DisplayGUI
from board.buttonBoard import ButtonBoard

class Game:
    def __init__(self):
        print("Hello world from Game")
        self.display = DisplayGUI()
        self.button_board = ButtonBoard(self.display)

    def run(self):
        # Use self.display and self.button_board to add components or perform other actions
        self.button_board.create_board()

        # Run the DisplayGUI's main loop
        self.display.run()