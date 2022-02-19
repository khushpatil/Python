from turtle import Turtle
step = 20
up , down , left , right = 90 , 270 , 180 , 0 
class Snake:
    def __init__(self):
        self.len_snake = []
        self.init_pos = 0
        for _ in range(3):
            new_turtle = Turtle()
            new_turtle.up()
            new_turtle.color("white")
            new_turtle.shape("square")
            new_turtle.setpos(int(self.init_pos),0)
            self.len_snake.append(new_turtle)
            self.init_pos -= 20
        self.head = self.len_snake[0]
    
    def move(self):
        for i in range(len(self.len_snake)-1, 0 , -1):
            new_x = self.len_snake[i-1].xcor()
            new_y = self.len_snake[i-1].ycor()
            self.len_snake[i].setpos(new_x, new_y)
        self.len_snake[0].fd(step)

    def up(self):
        if(self.head.heading() != down):
            self.head.seth(up)

    def down(self):
        if(self.head.heading() != up):
            self.head.seth(down)

    def left(self):
        if(self.head.heading() != right):
            self.head.seth(left)

    def right(self):
        if(self.head.heading()!= left):
            self.head.seth(right)

    def grow(self):
        position = self.len_snake[-1].position()
        new_turtle = Turtle("square")
        new_turtle.up()
        new_turtle.color("white")
        new_turtle.setpos(position)
        self.len_snake.append(new_turtle)