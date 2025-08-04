from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quiz Application")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            text="Question will appear here",
            width=280,
            fill=THEME_COLOR,
            font=("Arial","16", "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=self.true_image, bg="green", fg="white", command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        self.false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.false_image, bg="red", fg="white", command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()


        self.window.mainloop()

    def get_next_question(self):
        if not self.quiz.still_has_questions():
            self.canvas.itemconfig(self.question_text, text="You've completed the quiz!")
            self.canvas.config(bg="lightgrey")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
            return
        q_text = self.quiz.next_question()
        print(f"Q.{self.quiz.question_number}: {q_text}")
        self.canvas.itemconfig(self.question_text, text=q_text)
        self.canvas.config(bg="white")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))


    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)  #Adding the give_feedback method call here provides better readability.


    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        self.window.after(1000, self.get_next_question)


