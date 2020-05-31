from random import randrange
import random
import numpy as np
import matplotlib.pyplot as plt


# starting position generated randomlly
start = randrange(30)

positions = [start]

# I have used numpy.random which is functions generate samples from the uniform distribution on [0, 1)
# By that uniform distrribution to distinguish equally between two events
# Probability to move up or down can be between any of these
# initalize an array with number betweeen 0 and 1 I choose 0.45 and 0.55 as the margin
margin = [0.45, 0.55]

# creating the random 500 points this is equal to number of walks
randomNum = np.random.random(500)

# now we have 500 randoms points generated

# boolean values assigned to distinguish betweeen two equal probablities +1 or -1
# if random number generated less than the margin go down
GoDown = randomNum < margin[0]

# if higher go up
GoUp = randomNum > margin[1]

# combine the two states (this contains true or false) weather to go up or down
UpDown = zip(GoDown, GoUp)


# depending on the True or False status add the randomly generated number into the positions array
for idownp, iupp in UpDown:
    down = idownp
    up = iupp
    positions.append(positions[-1] - down + up)


# plotting down the positions array which is the graph of the random walk
plt.plot(positions)
plt.show()
