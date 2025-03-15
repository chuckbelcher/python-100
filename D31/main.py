import tkinter as tk

BACKGROUND_COLOR = "#B1DDC6"


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
card_text = canvas.create_text(400, 263, text="Title", font=("Ariel", 40, "italic"))

# Create buttons
cross_img = tk.PhotoImage(file="images/wrong.png")
cross_button = tk.Button(image=cross_img, highlightthickness=0)
cross_button.grid(row=1, column=0)

check_img = tk.PhotoImage(file="images/right.png")
check_button = tk.Button(image=check_img, highlightthickness=0)
check_button.grid(row=1, column=1)


window.mainloop()