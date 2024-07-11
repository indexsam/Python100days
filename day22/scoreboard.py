from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()
        self.draw_line()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))
        self.draw_line()

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()
    
    def draw_line(self):
        self.goto(0,280)
        self.setheading(270) # down heading
        for i in range(12):  # len(y-axis=600)/ 50(steps forward) = 12
            if i % 2 == 0:
                self.pendown()
                self.forward(50)
            else:
                self.penup()
                self.forward(50)

     
