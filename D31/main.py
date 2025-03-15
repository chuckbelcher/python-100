import tkinter as tk

BACKGROUND_COLOR = "#B1DDC6"

# Read data from file
data = []
with open("data/french_words.csv") as file:
    for line in file:
        word, translation = line.strip().split(",")
        data.append({
            "Question": word,
            "Answer": translation
        })

# Create flash card
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = data.pop(1)
    canvas.itemconfig(card_image, image=card_front_img)
    canvas.itemconfig(label_text, text="Question", fill="black")
    canvas.itemconfig(card_text, text=current_card["Question"], fill="black")
    flip_timer = window.after(5000, flip_card)

def flip_card():
    canvas.itemconfig(card_image, image=card_back_img)
    canvas.itemconfig(label_text, text="Answer", fill="white")
    canvas.itemconfig(card_text, text=current_card["Answer"], fill="white")

def is_known():
    next_card()

def is_unknown():
    next_card()

# Create flash card window
window = tk.Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Create canvas
canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# Create flash card image
card_front_img = tk.PhotoImage(file="images/card_front.png")
card_back_img = tk.PhotoImage(file="images/card_back.png")
card_image = canvas.create_image(400, 263, image=card_front_img)

# Create flash card text
label_text = canvas.create_text(400, 150, text="Question", font=("Ariel", 40, "italic"))
card_text = canvas.create_text(400, 263, text="Title", font=("Ariel", 40, "italic"))

# Create buttons
cross_img = tk.PhotoImage(file="images/wrong.png")
cross_button = tk.Button(image=cross_img, highlightthickness=0, command=is_unknown)
cross_button.grid(row=1, column=0)

check_img = tk.PhotoImage(file="images/right.png")
check_button = tk.Button(image=check_img, highlightthickness=0, command=is_known)
check_button.grid(row=1, column=1)

# Create flash card
current_card = {}
flip_timer = window.after(3000, flip_card)
next_card()

window.mainloop()