import random
import bisect
import statistics

# WeightedChoice function
# Returns a random value, considering the weights of each item.
class WeightedChoice(object):
    def __init__(self, weights):
        self.totals = []
        self.weights = weights
        running_total = 0

        for w in weights:
            running_total += w[1]
            self.totals.append(running_total)

    def next(self):
        rnd = random.random() * self.totals[-1]
        i = bisect.bisect_right(self.totals, rnd)
        return self.weights[i][0]

print ('Insert the chance to win a bet as a % value and press enter...')
winning_chance=float(input())

print ('Insert the number of total tries (betting until winning) and press enter...')
n_tries=int(input())

# List of possible outcomes
outcomelist = (
    ("Win!", winning_chance), #win
    ("Loss!", 100-winning_chance), #loose
)

# Feeding possible outcomes to the WeightedChoice function
weightedChoice = WeightedChoice(outcomelist)

all_bet_outcomes = []

# Make a choice (test purpose)
for i in range(0,n_tries):
    single_bet_outcomes = ["Filling temporary element"]
    first = True

    while single_bet_outcomes[-1] != "Win!":

        if first:
            single_bet_outcomes[0] = weightedChoice.next()
            fisrt = False

        single_bet_outcomes.append(weightedChoice.next())
        #print(single_bet_outcomes[-1] != "Win!") DEBUG

    all_bet_outcomes.append(len(single_bet_outcomes))

# Save results
average_tries_to_success=statistics.mean(all_bet_outcomes)
#mostfrequent_tries_to_success=statistics.mode(all_bet_outcomes)
median_of_tries_to_success=statistics.median(all_bet_outcomes)

# Print results
print ('Average number of bets to succed:')
print(average_tries_to_success)
print(' ')

#print ('Most frequent number of bets to succed (mode):')
#print(mostfrequent_tries_to_success)
#print(' ')

print ('50% of the times it requires this number of bets (median):')
print(median_of_tries_to_success)
print(' ')

# Data visualization
import matplotlib.pyplot as plt
import numpy as np 



n, bins, patches = plt.hist(x=all_bet_outcomes, bins='auto', color='#0504aa',
                            alpha=0.7, rwidth=0.85)

plt.grid(axis='y', alpha=0.75)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Bets required to win')
plt.text(23, 45, r'$\mu=15, b=3$')
maxfreq = n.max()
# Set a clean upper y-axis limit.
plt.ylim(top=np.ceil(maxfreq / 10) * 10 if maxfreq % 10 else maxfreq + 10)

# Display the graph
plt.show()
