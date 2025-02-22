import pandas
import turtle
IMAGE = "blank_states_img.gif"
screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape(IMAGE)
turtle.shape(IMAGE)
states_file = pandas.read_csv("50_states.csv")
states_list = states_file.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name? ").title()
    
    if answer_state == "Exit":
        missing_states = []
        for state in states_list:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in states_list:
        guessed_states.append(answer_state)
        writer = turtle.Turtle()
        writer.hideturtle()
        writer.penup()
        state_info = states_file[states_file.state == answer_state]
        writer.goto(state_info.x.item(), state_info.y.item())
        writer.write(answer_state, align="center", font=("Arial", 12, "normal"))
        states_list.remove(answer_state)
