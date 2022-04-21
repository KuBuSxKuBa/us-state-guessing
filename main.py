import pandas
import turtle
data = pandas.read_csv("50_states.csv")

s = turtle.Screen()
s.title("U.S. States Game")
image = "blank_states_img.gif"
s.addshape(image)
turtle.shape(image)


def write(guess):
    name = turtle.Turtle()
    country_data = data[data["state"] == guess]
    country_x = country_data.x.to_string(index=False)
    country_y = country_data.y.to_string(index=False)
    name.shape("turtle")
    name.penup()
    name.hideturtle()
    name.goto(int(country_x) , int(country_y))
    name.write(guess)


data_list = data["state"].to_list()
is_on = True
already_guessed = 0
already_guessed_list = []
all_states = []
for i in data:
    all_states.append(data["state"].to_string(index=False))
while is_on:
    guess = s.textinput(title=f"{already_guessed}/50", prompt="What's another state's name?")
    guess = guess.title()
    if guess == "exit":
        left = [state for state in all_states if state not in already_guessed_list]
        # left = []
        # for i in all_states:
        #     if i not in already_guessed_list:
        #         left.append(i)
        break
    if guess not in already_guessed_list:
        if guess in data_list:
            write(guess)
            already_guessed_list.append(guess)
            already_guessed += 1
    else:
        pass
# for i in data["state"]:
#     print(i)

s.exitonclick()
