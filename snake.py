from turtle import Turtle

STARTING_POINT = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        # create baby Mr. Very Dangerous with three segments
        # eg. segment_1 at (0,0) and 20 pixels
        # for loop to shift segment_2 and segment_3 so three segments do not overlap on top of each other
        for position in STARTING_POINT:
            self.add_seg(position)

    def add_seg(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    # Mr. very dangerous grow up everytime he eats food
    def grow(self):
        self.add_seg(self.segments[-1].position())

    def move(self):
        # to make three segments appear smooth without gap and be able to turn
        # segment 3 moves to segment 2 position and segment 2 moves to segment 1 position
        # it starts on the segments -1: seg 3 at position 2, seg 1 at position 0
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)

    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)

    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)
