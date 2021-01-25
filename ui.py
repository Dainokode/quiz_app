from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"


class QuizAppUi():
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz


        # window setup
        self.window = Tk()
        self.window.title("Quiz App")
        self.window.config(bg=THEME_COLOR)


        # score label
        self.score = 0
        self.score_label = self.label = Label(text=f"Score: {self.score}", font=("arial", 12, "italic"))
        self.label.grid(row=0, column=1, pady=20)


        # canvas setup
        self.canvas = Canvas(height=250, width=300)
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)
        self.question_text = self.canvas.create_text(150, 125, width=280, text="some text", font=("arial", 18, "italic"))


        # buttons
        self.true_img = PhotoImage(file="images/true.png")
        self.true = Button(image=self.true_img, command=self.true_button)
        self.true.grid(row=2, column=0, pady=20)


        self.false_img = PhotoImage(file="images/false.png")
        self.false = Button(image=self.false_img, command=self.false_button)
        self.false.grid(row=2, column=1)

        
        self.show_question()


        # run program
        self.window.mainloop()


    def show_question(self):
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.canvas.configure(bg="white")
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.canvas.config(bg="white")
    
    def true_button(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)
    

    def false_button(self):
       is_right = self.quiz.check_answer("False")
       self.give_feedback(is_right)
    

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.configure(bg="green")
            self.window.after(1000, self.show_question)
        else:
            self.canvas.configure(bg="red")
            self.window.after(1000, self.show_question)
    
