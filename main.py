import turtle
import pandas as pd
from answer import Answer

screen = turtle.Screen()
screen.title("U.S. States")

image = "blank_states_img.gif"

def proper_input(answer):
    proper_answer = ''
    for word in answer.split():
        proper_answer += f"{word.capitalize()} "
    return proper_answer.strip()

screen.setup(700, 700)
screen.addshape(image)
turtle.shape(image)

coor_data = pd.read_csv("50_states.csv")

game_is_on = True
score = 0
guessed_states = []
while game_is_on:
    answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state's name?")
    if answer_state.lower() == 'exit':
        all_states = coor_data.state.to_list()
        states_to_learn = [i for i in all_states if i not in guessed_states]
        states_to_learn = pd.DataFrame(states_to_learn)
        states_to_learn.to_csv('states_to_learn.csv')
        break

    answer_state = proper_input(answer_state)
    if answer_state in coor_data['state'].to_list() and answer_state not in guessed_states:
        state_on_map = Answer(int(coor_data[coor_data['state'] == answer_state]['x']), int(coor_data[coor_data['state'] == answer_state]['y']), answer_state)
        #if answer_state not in guessed_states:
        guessed_states.append(answer_state)
        score += 1
























#import pandas as pd

#data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

#data = data.dropna(subset='Primary Fur Color')

#fur_colors = data["Primary Fur Color"].unique()
#counts = []

#for color in fur_colors:
#    counts.append(data[data["Primary Fur Color"] == color]["Primary Fur Color"].count())

#fur_color_counts = pd.DataFrame({"Fur Color" : fur_colors,"Count" : counts})
#fur_color_counts.to_csv("squirrel_count.csv")