from tkinter import *

from quiz_brain import  QuizBrain

THEME_COLOR = "#375362"


class QuizzInterface:
    
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz=quiz_brain

        self.current_score=0
        self.window = Tk()
        self.window.title("Quiz")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.quizquest = self.canvas.create_text(150,125, 
        width=280, text="Sample text",
        fill=THEME_COLOR, font=("Ariel", 20, "italic"))

        self.score = Label(text=f"Score: {self.current_score}", fg="white", bg=THEME_COLOR)
        self.score.grid(column=1, row=0)

        img_tick= PhotoImage(file="./images/true.png")
        self.tick = Button(image=img_tick, highlightthickness=0, command=self.true_guess)
        self.tick.grid(column=0, row=2)

        img_x = PhotoImage(file="./images/false.png")
        self.x = Button(image=img_x, highlightthickness=0, command=self.false_guess)
        self.x.grid(column=1, row=2)

        self.get_next_question()


        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.quest = self.quiz.next_question()
        self.canvas.itemconfig(self.quizquest, text=self.quest)



    def true_guess(self):
        val = self.quiz.check_answer("true")
        self.current_score = self.quiz.score
        self.score.config(text=f"Score: {self.current_score}")
        if self.quiz.still_has_questions():
            if val:
                self.canvas.config(bg="green")
                self.window.after(1000, func=self.get_next_question)
            else:
                self.canvas.config(bg="red")
                self.window.after(1000, func=self.get_next_question)
        else:
            self.canvas.config(bg="white")
            self.canvas.itemconfig(self.quizquest, text="The End!!")
            self.x.config(state="disabled")
            self.tick.config(state="disabled")

        

    def false_guess(self):
        val = self.quiz.check_answer("false")
        self.current_score = self.quiz.score
        self.score.config(text=f"Score: {self.current_score}")
        if self.quiz.still_has_questions():
            if val:
                self.canvas.config(bg="green")
                self.window.after(1000, func=self.get_next_question)
            else:
                self.canvas.config(bg="red")
                self.window.after(1000, func=self.get_next_question)
        else:
            self.canvas.config(bg="white")
            self.canvas.itemconfig(self.quizquest, text="The End!!")
            self.x.config(state="disabled")
            self.tick.config(state="disabled")
