import tkinter as tk
import random

#==========================================
# Purpose: An object of this class is a interactive GUI that holds the classic game, the sname game. 
# Instance variables:
# self.win = a 660x660 pixel window created by the tkinter package
# self.canvas = a canvas that holds all the interactive components of the snake game
# self.oval_xpos = the x position of the oval, which represents the food pellet
# self.oval_ypos = the y position of the oval, which represents the food pellet
# Methods:
# __init__ = initializes the frame and canvas that the game will be operating on
# start_game = begins the game - creates a border, a user snake, and enemy snakes on the canvas
# restart_game = restarts the game by clearing the canvas and initializing all the main components of the game
# gameloop = animates the game every 100 miliseconds. animations/actions depend on the state of the snakes
#==========================================

class SnakeGUI:
    def __init__(self):
        self.win = tk.Tk()
        self.win.title("Snake Game")
        self.canvas = tk.Canvas(self.win, width=660, height=660)
        self.canvas.pack()
        self.start_game()

    def start_game(self):
    
        self.board = self.canvas.create_rectangle(30,30,630,630)
        
        self.user_snake = Snake(330,330,'green',self.canvas, True)
        self.win.bind('<Down>',self.user_snake.go_down)
        self.win.bind('<Left>',self.user_snake.go_left)
        self.win.bind('<Right>',self.user_snake.go_right)
        self.win.bind('<Up>',self.user_snake.go_up)
        
        self.enemy_snake = Snake(90,90,'black',self.canvas, False)

        self.oval_xpos = random.randint(60,600)
        self.oval_ypos = random.randint(60,600)
        self.food_pellet = self.canvas.create_oval(self.oval_xpos,self.oval_ypos,self.oval_xpos+30,self.oval_ypos+30, fill='red')
        
        self.gameloop()

    def restart_game(self, event):
        self.canvas.delete(tk.ALL)
        self.start_game()
        
    def gameloop(self):
        if self.user_snake.move(self.oval_xpos, self.oval_ypos) == True or self.enemy_snake.move(self.oval_xpos, self.oval_ypos) == True:
            self.canvas.delete(self.food_pellet)
            self.oval_xpos = random.randint(30,600)
            self.oval_ypos = random.randint(30,600)
            self.food_pellet = self.canvas.create_oval(self.oval_xpos,self.oval_ypos,self.oval_xpos+30,self.oval_ypos+30, fill='red')
            self.canvas.after(100, self.gameloop)
        elif self.user_snake.collide_with_wall() == True or self.enemy_snake.collide_with_wall() == True or self.user_snake.collide_with_other(self.enemy_snake) == True:
            self.canvas.create_text(330,330,text="        Game Over\nYou reached level " + str(len(self.user_snake.segments)) + "\n    Press r to restart")
            self.win.bind('<r>', self.restart_game)
        else:
            self.canvas.after(100, self.gameloop)

#==========================================
# Purpose: An object of this class is a snake from the snake game
# Instance variables:
# self.xpos = x position of the snake
# self.ypos = y position of the snake
# self.vx = velocity of the snake along the x-coordinates
# self.vy = velocity of the snake along the y-coordinates
# self.color = color of the snake
# self.canvas = the canvas upon which the snake is being drawn
# is_user = determines whether the snake is user controlled or not
# self.segments = a list of each integer identifier for the create_rectangle method of tkinter, from oldest to newest
# Methods:
# __init__ = initializes the snake object
# eat_pellet = determines whether a snake object is close enough to eat the pellet
# collide_with_wall = determines whether a snake object has collided with the boarded wall
# college_with_other = determines whether a snake object has collied with anotheer snake object
# move = clarifies the movement of the snake objects, and determines whether a snake object can grow in length or not
# go_down = changes the velocity of the x position to 0, an velocity of the y position to 30
# go_up = changes the velocity of the x position to 0, an velocity of the y position to -30
# go_left = changes the velocity of the x position to -30, an velocity of the y position to 0
# go_right = changes the velocity of the x position to 30, an velocity of the y position to 0
#==========================================
    
class Snake:
    def __init__(self, xpos, ypos, color, canvas, is_user):
        self.xpos = xpos
        self.ypos = ypos
        self.vx = 30
        self.vy = 0
        self.color = color
        self.canvas = canvas
        self.is_user = is_user
        
        self.snake_part = self.canvas.create_rectangle(self.xpos, self.ypos, self.xpos+30, self.ypos+30, fill=self.color)
        self.segments = []
        self.segments.append(self.snake_part)

    def eat_pellet(self, oval_xpos, oval_ypos):
        x_diff = abs(self.xpos - oval_xpos)
        y_diff = abs(self.ypos - oval_ypos)
        
        if x_diff <= 30 and y_diff <= 30:
            return True
        else:
            return False

    def collide_with_wall(self):
        if (self.xpos <= 30 or self.xpos >= 600) or (self.ypos <= 30 or self.ypos >= 600):
            return True
        else:
            return False

    def collide_with_other(self, other):
        x_diff = abs(self.xpos - other.xpos)
        y_diff = abs(self.ypos - other.ypos)
        
        if x_diff <= 30 and y_diff <= 30:
            return True
        else:
            return False

    def move(self, oval_xpos, oval_ypos):
        if self.is_user == True:
            self.xpos += self.vx
            self.ypos += self.vy
        else:
            if oval_xpos > (self.xpos + 30):
                self.vy = 0
                self.vx = 30
                self.xpos += self.vx
            elif (oval_xpos + 30) < self.xpos:
                self.vy = 0
                self.vx = 30
                self.xpos -= self.vx
            elif oval_ypos < (self.ypos - 30):
                self.vy = 30
                self.vx = 0
                self.ypos -= self.vy
            elif oval_ypos > (self.ypos + 30):
                self.vy = 30
                self.vx = 0
                self.ypos += self.vy

        if self.eat_pellet(oval_xpos, oval_ypos) == True:
            self.next_snake_part = self.canvas.create_rectangle(self.xpos, self.ypos, self.xpos+30, self.ypos+30, fill=self.color)
            self.segments.insert(0, self.next_snake_part)
            return True
        else:
            self.next_snake_part = self.canvas.create_rectangle(self.xpos, self.ypos, self.xpos+30, self.ypos+30, fill=self.color)
            self.segments.insert(0, self.next_snake_part)
            self.last_snake_part = self.segments.pop()
            self.canvas.delete(self.last_snake_part)
            return False

    def go_down(self, event):
        self.vx = 0
        self.vy = 30

    def go_up(self, event):
        self.vx = 0
        self.vy = -30

    def go_right(self, event):
        self.vx = 30
        self.vy = 0

    def go_left(self, event):
        self.vx = -30
        self.vy = 0
        
        
SnakeGUI()
tk.mainloop()
