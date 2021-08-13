import tkinter
import time

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #
tick_mark = "✅"
reset_status = False
lap = 0


def timer_reset():
    global reset_status
    canvas.itemconfig(text_id, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")
    reset_status = True
    lap_count()


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reset_status
    global tick_mark
    min = WORK_MIN - 1
    sec = 60
    if reset_status is False:
        heading_label.config(text="Work", font=(FONT_NAME, 45, "bold"), fg=GREEN, bg=YELLOW)
    while min > -1 and reset_status is False:
        canvas.itemconfig(text_id, text=f"{min:02}:{sec:02}", font=(FONT_NAME, 35, "bold"), fill="white")
        if sec == 0:
            sec = 60
            min -= 1
        sec -= 1
        time.sleep(1)
        window.update()
    if reset_status is False:
        if lap >= 1:
            tick_mark += "✅"
        lap_count()
        break_timer()
    elif reset_status is True:
        heading_label.config(text="Timer", font=(FONT_NAME, 45, "bold"), fg=GREEN, bg=YELLOW)
    reset_status = False


def break_timer():
    global tick_mark
    global reset_status
    global lap
    window.focus_force()
    heading_label.config(text="Break", font=(FONT_NAME, 45, "bold"), fg=PINK, bg=YELLOW)
    min = 4
    sec = 60
    if lap == 4:
        min = 20
        heading_label.config(text="Break", font=(FONT_NAME, 45, "bold"), fg=RED, bg=YELLOW)
    while min > -1 and reset_status is False:
        canvas.itemconfig(text_id, text=f"{min:02}:{sec:02}", font=(FONT_NAME, 35, "bold"), fill="white")
        if sec == 0:
            sec = 60
            min -= 1
        sec -= 1
        time.sleep(1)
        window.update()
    heading_label.config(text="Timer", font=(FONT_NAME, 45, "bold"), fg=GREEN, bg=YELLOW)
    start_timer()


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def lap_count():
    global tick_mark
    global lap
    global reset_status
    # tick label
    tick = tkinter.Label(text=tick_mark, font=(FONT_NAME, 15, "bold"), fg=GREEN, bg=YELLOW)
    tick.grid(column=1, row=2)
    lap += 1
    if reset_status is True:
        tick.config(text="         ", font=(FONT_NAME, 15, "bold"), bg=YELLOW)
        lap = 0
        tick_mark = "✅"


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# adding heading
heading_label = tkinter.Label(text="Timer")
heading_label.config(font=(FONT_NAME, 45, "bold"), fg=GREEN, bg=YELLOW)
heading_label.grid(column=1, row=0)

# adding canvas
canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
text_id = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")
canvas.grid(column=1, row=1)

# start button
start = tkinter.Button(text="Start", command=start_timer, activebackground=RED, font=(FONT_NAME, 12))
start.grid(column=0, row=2)

# reset button
reset = tkinter.Button(text="Reset", command=timer_reset, activebackground=RED, font=(FONT_NAME, 12))
reset.grid(column=2, row=2)

window.mainloop()
