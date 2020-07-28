import random
import jsonify as js

# We throw a dice for (n) times what is the probability of having number (m), (k)times?
def event_probability1():

    roll_number = random.randint(2,6)
    outcome_num = random.randint(1,6)
    times = random.randint(1,roll_number)

    question = f'We throw a dice for {roll_number} times what is the probability of having number {outcome_num}, {times} times?'
    answer = f'{times}/{6*roll_number}'

    output = question + answer

    return output

# (n) cards are randomly drawn from a deck of normal playing cards (52 cards) what is the probability of drawing (m) of [symbol] and
# k of [symbol]?
def event_probability2():
    symbols = ['spades', 'hearts', 'clubs', 'diamonds']
    cards=['Jack', 'King', 'Queen', 'Ace']
    cards_num = random.randint(2,8)
    goal_card1 = random.randint(2,10)
    goal_card2= random.choice(cards)

    question = f'{cards_num} cards are randomly drawn from a deck of normal playing cards (52 cards) and each time drawn card replaced to the deck what is the probability of drawing {goal_card1} of {random.choice(symbols)} and ' \
        f' {goal_card2} of {random.choice(symbols)}?'

    answer = f'1/52<sup>{cards_num}</sup>'
    output = question+answer
    return output


#In an experiment consisting of three flips of a fair coin, what is the probability that the first two flips are the same?
