"""
main.py: entry point for Pomodoro program
"""
from tkinter import *
import math

# --------------------------------------------- CONSTANTS ------------------------------------------------------ #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Comic Sans MS"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 30
reps = 0
timer = None

# ----------------------------------------------- TIMER RESET -------------------------------------------------- #
def reset_timer():
    window.after_cancel(timer) # Stops timer
    canvas.itemconfig(timer_text, text="00:00") # Reset timer text
    heading.config(text="Timer", fg=GREEN) # reset heading text
    checkmarks.config(text="") # reset checkmarks

    # Reset number of reps
    global reps
    reps = 0

# ----------------------------------------------- TIMER MECHANISM ---------------------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # If it's the 8th rep, go for a long break
    if reps % 8 == 0:
        heading.config(text="Break", fg=RED)
        countdown(long_break_sec)

    # If it's the 2nd/4th/6th rep, go for a short break
    elif reps % 2 == 0:
        heading.config(text="Break", fg=PINK)
        countdown(short_break_sec)

    # If it's the 1st/3rd/5th/7th reps, start work session
    else:
        heading.config(text="Work", fg=GREEN)
        countdown(work_sec)


# ----------------------------------------------- COUNTDOWN MECHANISM ------------------------------------------ #
def countdown(count):
    minutes = math.floor(count / 60) # Number of minutes left
    seconds = count % 60 # Number of seconds left
    if seconds < 10:
        seconds = f"0{seconds}"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✓"
        checkmarks.config(text=marks)

# ----------------------------------------------- UI SETUP ----------------------------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=50, pady=25, bg=YELLOW)

# Create "Timer" label
heading = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 40, "normal"), bg=YELLOW)
heading.grid(row=0, column=1)

# Creating a canvas
canvas = Canvas(width=250, height=250, bg=YELLOW, highlightthickness=0)
bg_img = PhotoImage(file="tomato.png")
canvas.create_image(125, 125, image=bg_img) # x, y, PhotoImage
timer_text = canvas.create_text(125, 135, text="00:00", fill="white", font=(FONT_NAME, 25, "bold")) # x, y, text
canvas.grid(row=1, column=1)


# Creating the "Start" and "Reset" buttons
start_btn = Button(text="Start", relief="flat", borderwidth=0, padx=10, pady=2,
                   command=start_timer)
start_btn.grid(row=2, column=0)

reset_btn = Button(text="Reset", relief="flat", borderwidth=0, padx=10, pady=2,
                   command=reset_timer)
reset_btn.grid(row=2, column=2)

# Creating the green checkmark
checkmarks = Label(bg=YELLOW, fg=GREEN, font=("", 15, "bold"))
checkmarks.grid(row=3, column=1)








window.mainloop()