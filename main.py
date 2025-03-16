import turtle
import pandas

screen = turtle.Screen()
screen.setup(width=710, height=500)
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data["state"].values
guessed_states = []
missing_states = []
game_on = True

while game_on:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/{len(all_states)} States Correct", prompt="What's another state name?").title()
    if answer_state == "Exit":
        game_on = False
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        states_to_learn_dict = {
            "state": missing_states
        }
        states_to_learn_data = pandas.DataFrame(states_to_learn_dict)
        states_to_learn_data.to_csv("states_to_learn.csv")

    if answer_state in all_states:
        if answer_state not in guessed_states:
            t = turtle.Turtle()
            t.penup()
            t.hideturtle()
            state_data = data[data["state"] == answer_state]
            guessed_states.append(answer_state)
            t.goto(state_data.x.item(), state_data.y.item())
            t.write(answer_state, align="center")
        if len(guessed_states) == len(all_states):
            game_on = False
            turtle.color("green")
            turtle.write("You won!", align="center", font=('Arial', 25, 'normal'))



screen.exitonclick()