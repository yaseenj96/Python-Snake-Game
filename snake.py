from turtle import Turtle
UP = 90
RIGHT = 0
LEFT = 180
DOWN = 270


class Snake:
    def __init__(self):
        self.starting_positions = [(0,0), (-20, 0), (-40, 0)]
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in self.starting_positions:
            self.add_segment(position)

    def add_segment(self, position):
        t1 = Turtle(shape="square")
        t1.color("white")
        t1.penup()
        t1.setposition(position)
        self.segments.append(t1)

    def extend(self):
        self.add_segment(self.segments[-1].position())
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(20)

    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)

    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)

    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)
