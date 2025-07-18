import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from quiz_brain import QuizBrain
from tkinter import PhotoImage

THEME = "darkly"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = ttk.Window(themename=THEME)
        self.window.title("Quizzy")
        self.window.geometry("400x500")
        self.window.resizable(False, False)
        self.window.configure(padx=20, pady=20)

        self.score_label = ttk.Label(text="SCORE: 0/0", font=("Helvetica", 12, "bold"), bootstyle="info")
        self.score_label.grid(row=0, column=1, sticky=E)

        self.canvas = ttk.Canvas(self.window, width=300, height=250, background="white", borderwidth=0, highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Loading question...",
            fill="#375362",
            font=("Helvetica", 16, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=30)

        true_img = PhotoImage(file="images/true.png")
        self.true_button = ttk.Button(image=true_img, command=self.true_pressed, bootstyle="success-outline")
        self.true_button.image = true_img
        self.true_button.grid(row=2, column=0, padx=10, pady=10)

        false_img = PhotoImage(file="images/false.png")
        self.false_button = ttk.Button(image=false_img, command=self.false_pressed, bootstyle="danger-outline")
        self.false_button.image = false_img
        self.false_button.grid(row=2, column=1, padx=10, pady=10)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(background="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            final_score = f"🎉 Quiz Completed!\nYour Final Score:\n{self.quiz.score}/{self.quiz.question_number}"
            self.canvas.itemconfig(self.question_text, text=final_score)
            self.canvas.config(bg="#4CAF50")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
        self.score_label.config(text=f"SCORE: {self.quiz.score}/{self.quiz.question_number}")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        self.canvas.config(bg="green" if is_right else "red")
        self.window.after(1000, self.get_next_question)
