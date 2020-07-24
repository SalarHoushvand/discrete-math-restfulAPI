import random
import random_set as rs
import jsonify as js
def inverse(num):
    global zip
    output = {}
    for i in range(num):
        A = []
        B = []
        set_len = random.randint(3, 6)
        question_json = 'question ' + str(i + 1)
        for i in range(set_len):
            rand_int = random.randint(1, 15)
            if rand_int not in A:
                    A.append(rand_int)
        for i in range(set_len):
            rand_int = random.randint(15, 30)
            if rand_int not in B:
                B.append(rand_int)
        zip1 = list(zip(A, B))

        question = 'Is f(x) from A to B a function ? If so what kind of function it is ? f(x)=' + str(zip1)
        answer = rs.function(A, B)

        output.update({question_json: {'A': A, 'B': B, 'question': question, 'answer': str(answer)}})
        print(output)


def choices(par, operation):
    choices = []
    output = []
    while len(choices) < 4:
        num2 = str(par)
        if operation == 'partition' or operation == 'complement':
            set2 = []
            if num2[0] == '1':
                set1 = rs.random_set(integer=3)
            elif num2[0] == '2':
                set1 = rs.random_set(integer=0, float=3)
            elif num2[0] == '3':
                set1 = rs.random_set(integer=0, char=3)
            elif num2[0] == '4':
                set1 = rs.random_set(integer=0, country_name=3)
            elif num2[0] == '5':
                set1 = rs.random_set(integer=0, city_name=3)
            elif num2[0] == '6':
                set1 = rs.random_set(integer=0, male_name=3)
            elif num2[0] == '7':
                set1 = rs.random_set(integer=0, female_name=3)

        else:
            if num2[0] == '1':
                set1 = rs.random_set()
            elif num2[0] == '2':
                set1 = rs.random_set(integer=0, float=5)
            elif num2[0] == '3':
                set1 = rs.random_set(integer=0, char=5)
            elif num2[0] == '4':
                set1 = rs.random_set(integer=0, country_name=5)
            elif num2[0] == '5':
                set1 = rs.random_set(integer=0, city_name=5)
            elif num2[0] == '6':
                set1 = rs.random_set(integer=0, male_name=5)
            elif num2[0] == '7':
                set1 = rs.random_set(integer=0, female_name=5)
            if num2[1] == '1':
                set2 = rs.random_set()
            elif num2[1] == '2':
                set2 = rs.random_set(integer=0, float=5)
            elif num2[1] == '3':
                set2 = rs.random_set(integer=0, char=5)
            elif num2[1] == '4':
                set2 = rs.random_set(integer=0, country_name=5)
            elif num2[1] == '5':
                set2 = rs.random_set(integer=0, city_name=5)
            elif num2[1] == '6':
                set2 = rs.random_set(integer=0, male_name=5)
            elif num2[1] == '7':
                set2 = rs.random_set(integer=0, female_name=5)
        answer = rs.set_operation(op=operation, set_1=set1, set_2=set2)
        if answer not in choices:
            choices.append(answer)
        else:
            pass
    if operation == 'partition' or operation == 'complement':
        question = 'What is the ' + operation + ' of this set? '
    else:
        question = ('What is the ' + operation + ' of these two sets? ').replace('_', ' ')
    choices = random.sample(choices, len(choices))
    output_json = js.json_maker(str(question) + ' ' + str(set1) + ' ' + str(set2), choices , choices.index(answer)+1)

    return output_json


