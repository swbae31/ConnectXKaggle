from kaggle_environments import evaluate, make, utils
from random import choice

env = make("connectx", debug=True)
env.render()

# This agent random chooses a non-empty column.
def my_agent(observation, configuration):
    return choice([c for c in range(configuration.columns) if observation.board[c] == 0])

env.reset()
# Play as the first agent against default "random" agent.
env.run([my_agent, "random"])
env.render(mode="ipython", width=500, height=450)