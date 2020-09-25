
def equation():
    choices = ['\(x^2\)', '$${\sqrt{x} \over 2}$$', '$${\sqrt{x}}$$', '\(x+1\)']
    question = 'Which one of these functions is one-to-one?'
    answer = '\(x+1\)'
    choices = random.sample(choices, len(choices))
    return js.question_json_maker(uuid.uuid1().hex,question, choices, choices.index(answer) + 1, difficulty= 3)

