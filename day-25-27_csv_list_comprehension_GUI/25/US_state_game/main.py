import turtle
import pandas
from show_state import ShowState


def return_cordinates(df_name, answer_state):
    """Returns (x, y) position of state on the screen"""
    state = df_name[df_name["state"] == answer_state]
    state_x = int(state["x"])
    state_y = int(state["y"])
    return (state_x, state_y)

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# get coordinates on click
# import get_mouse_click_cor
# turtle.onscreenclick(get_mouse_click_cor.get_mouse_click_coor())
data = pandas.read_csv("50_states.csv")
states_list = data["state"].to_list()
correct_guesses = []

# MAIN
while len(correct_guesses) < 50:
    answer_state = (screen.textinput(title=f"{len(correct_guesses)}/50 Guess the State", prompt="Type the name of State")).title()
    if answer_state == "Exit":
        break
    if answer_state in states_list:
        correct_guesses.append(answer_state)
        position = return_cordinates(df_name=data, answer_state=answer_state)
        show_state = ShowState(answer_state, position)

# not_guessed = list(set(states_list) - set(correct_guesses))
# solution from next lesson day 26 exercise 4
not_guessed = [not_guessed_state for not_guessed_state in states_list if not_guessed_state not in correct_guesses]
to_learn_data = pandas.DataFrame(not_guessed)
to_learn_data.to_csv("a.csv")

