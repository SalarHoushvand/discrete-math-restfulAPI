
import random
import functions as functions

choices = []
while len(choices) < 4:
    set_1 = functions.random_set()
    subset_1 = []
    for i in range(len(set_1) - 2):
        subset_1.append(random.choice(set_1))
    question = (
        f'What is the complement of set A= {str(set(subset_1))} considering U= {str(set(set_1))} is universal set? ').replace(
        '[]',
        '').replace(
        '[', '{').replace(']', '}').replace('_', ' ').replace('[', '{').replace(
        ']', '}')
    answer = str(set(set_1) - set(subset_1)).replace('[', '{').replace(']', '}')
    if answer not in choices:
        choices.append(answer)

print(question)
print(choices)