from turtle import Turtle, Screen
import pandas
screen = Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.bgpic(image)
screen.setup(width=740, height=500)
states_data = pandas.read_csv("50_states.csv")
states_names = states_data["state"].to_list()
states_answered = []
count = 0
while count < len(states_names):
    answer_state = screen.textinput(title="Guess-the-State", prompt=f"Enter the State's Name[current score - {count} / "
                                                                    + f"{len(states_names)}] = ").title()
    if answer_state == "Exit":
        break
    state_info = states_data[states_data["state"] == answer_state]
    if answer_state in states_names and answer_state not in states_answered:
        state = Turtle()
        state.hideturtle()
        state.penup()
        state.goto(int(state_info.x), int(state_info.y))
        state.write(arg=f"{answer_state}", align="center", font=("Arial", 8, "normal"))
        states_answered.append(answer_state)
        count += 1
states_missed = []
for state_name in states_names:
    if state_name not in states_answered:
        states_missed.append(state_name)
states_missed_dict = {"states": states_missed}
states_missed_data = pandas.DataFrame(states_missed_dict)
states_missed_data.to_csv("states_missed.csv")

# new screen for all the missed states
screen_2 = Screen()
screen_2.title(f"ALL-THE-MISSED-STATES [ Score = {count} / 50 ]")
screen_2.bgpic(image)
screen_2.setup(width=740, height=500)
for state_name in states_missed:
    state = Turtle()
    state.hideturtle()
    state.penup()
    state_info = states_data[states_data["state"] == state_name]
    state.goto(int(state_info.x), int(state_info.y))
    state.write(arg=f"{state_name}", align="center", font=("Arial", 8, "normal"))

state = Turtle()
state.hideturtle()
state.penup()
state.goto(0, 220)
state.pencolor("red")
if count != 50:
    state.write(arg="Try Your Best Next Time", align="center", font=("Arial", 14, "normal"))
else:
    state.write(arg="Great Work", align="center", font=("Arial", 14, "normal"))

screen_2.exitonclick()
