import tkinter as tk
from tkinter import messagebox
class Game:
    def __init__(self):
        self.current_player = "X"
        self.board = [["","",""],["","",""],["","",""]]
        self.window = tk.Tk()
        self.window.title("**TIC TAC TOE**")
        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                buttons = tk.Button(self.window,text="",width = 25,height = 15, command = lambda i=i,j=j:self.moves(i,j))
                buttons.grid(row=i,column =j)
                row.append(buttons)
            self.buttons.append(row)
    

    def moves(self,row,column):
        if self.board[row][column] =="":
            self.board[row][column] =self.current_player
            self.buttons[row][column].config(text=self.current_player)
            if self.checkwinner(self.current_player):
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.window.quit()
            elif self.isDraw():
                messagebox.showwarning("Game over " "Its an Draw")
                self.window.quit()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    
    def checkwinner(self,player):
        for i in range(3):
            if player == self.board[i][0] == self.board[i][1] == self.board[i][2]:
                return True
            if player == self.board[0][i] == self.board[1][i] == self.board[2][i]:
                return True
        if player == self.board[0][0] == self.board[1][1] == self.board[2][2]:
                return True
        if player == self.board[0][2] == self.board[1][1] == self.board[2][0]:
                return True
        return False
    
    def isDraw(self):
        for row in self.board:
            if "" in row:
                return False
        return True 
    
    def run(self):
        self.window.mainloop()


game = Game()
game.run()




