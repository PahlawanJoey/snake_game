from turtle import Turtle
class Snake:
    def __init__(self):
        self.snake_segments = []
        self.snake_start_point = 0
        self.create_snake()
        self.last_direction = self.snake_segments[0].heading()

    def create_snake(self):
        for add_snake_part in range(3):
            self.add_snakepart()
            self.snake_segments[add_snake_part].showturtle()

    def add_snakepart(self):
        self.begin_turtle = Turtle("square")
        self.begin_turtle.hideturtle()
        self.begin_turtle.penup()
        self.begin_turtle.color("chartreuse")
        self.begin_turtle.setpos(x=self.snake_start_point, y=0)
        self.snake_start_point -= 20
        self.snake_segments.append(self.begin_turtle)

    def extend_snake(self):
        last_snake = len(self.snake_segments)
        coordinates_lastpart = self.snake_segments[last_snake - 1].pos()
        self.begin_turtle.setpos(coordinates_lastpart)
        self.snake_segments[last_snake - 1].showturtle()
        self.add_snakepart()

    def move_up(self):
        if self.snake_segments[0].heading() != 270:
            self.snake_segments[0].setheading(90)
    def move_down(self):
        if self.snake_segments[0].heading() != 90:
            self.snake_segments[0].setheading(270)
    def move_left(self):
        if self.snake_segments[0].heading() != 0:
            self.snake_segments[0].setheading(180)
    def move_right(self):
        if self.snake_segments[0].heading() != 180:
            self.snake_segments[0].setheading(0)

    def move_snake(self):
        for seg_num in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[seg_num - 1].xcor()
            new_y = self.snake_segments[seg_num - 1].ycor()
            self.snake_segments[seg_num].goto(new_x, new_y)
        self.snake_segments[0].forward(20)
        self.last_direction = self.snake_segments[0].heading()