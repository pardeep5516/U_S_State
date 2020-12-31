import pandas
import turtle

screen = turtle.Screen()
screen.title("U.S State Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

# def get_mouse_click_coor(x, y):
#     print(x,y)

# turtle.onscreenclick(get_mouse_click_coor)

# turtle.mainloop()
states = pandas.read_csv("50_states.csv")
all_state = states.state.to_list()
guess_states = []

while len(guess_states) < 50:
    answer_state = screen.textinput(title=f"{len(guess_states)} / 50 State Correct", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        missing_state = []
        for state in all_state:
            if state not in guess_states:
                missing_state.append(state)
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("missing_state.csv")
                
        break

    if answer_state in all_state:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = states[states.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())
        guess_states.append(state_data.state.item())
