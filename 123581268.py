import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def _init_(self, root):
        self.root = root
        root.title("Tic-Tac-Toe")

        self.buttons=[[0 for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.moves_left = 9
        self.create_board()

    def create_board(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(
                    self.root,
                    text="",
                    font=('Arial', 8),
                    background="lightblue",
                    width=15,
                    height=5,
                    command=lambda row=i,col=j:self.make_move(row,col),
                )
                self.buttons[i][j].grid(row=i,column=j)

    def make_move(self, row, col):
        try:
            if self.buttons[row][col]["text"] == "":
                self.buttons[row][col]["text"] = self.current_player
                self.moves_left -= 1

                if self.check_winner():
                    self.game_over(self.current_player)
                elif self.moves_left == 0:
                    self.game_over("Draw")
                else:
                    self.switch_player()
            else:
                pass

        except IndexError:
            messagebox.showerror("Error", "Invalid move.please select a valid cell.")

    def switch_player(self):
        self.current_player = "0" if self.current_player == "X" else "X"

    def check_winner(self):
            # Check rows
            for i in range(3):
                if self.buttons[i][0]["text"] == self.buttons[i][1]["text"] == self.buttons[i][2]["text"] != "":
                    return True
            # Check columns
            for j in range(3):
                if self.buttons[0][j]["text"] == self.buttons[1][j]["text"] == self.buttons[2][j]["text"] != "":
                    return True
            # Check diagonals
            if self.buttons[0][0]["text"] == self.buttons[1][1]["text"] == self.buttons[2][2]["text"] != "":
                return True
            if self.buttons[0][2]["text"] == self.buttons[1][1]["text"] == self.buttons[2][0]["text"] != "":
                return True
            return False

    def game_over(self, result):
            if result == "Draw":
             messagebox.showinfo("Game Over","It's a draw!")
            else:
                messagebox.showinfo("Game Over",f"Player{result} wins!")
            self.reset_board()

    def reset_board(self):
        for i in range(3):
            for j in range (3):
                self.buttons[i][j]["text"] = ""
        self.current_player="X"
        self.moves_left=9

if __name__ == "_main_":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()