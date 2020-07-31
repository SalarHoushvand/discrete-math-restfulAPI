# -----------------------------------------------------------
# API to generate random questions for discrete mathematics topics
# and outputs them in a JSON file.
#
# 2020 East Carolina University
# email salarhoushvand@gmail.com
# -----------------------------------------------------------

# ---------- Imports ----------

import math
import random
from flask import Flask, jsonify, render_template
import functions as functions
import jsonify as js

# ---------- App ----------

app = Flask(__name__)


# ---------- Main Page ----------

@app.route('/', methods=['GET'])
def index():
    """
    Home page of API.

    :return: index.html
    """
    return render_template('./index.html')


# ---------- Set Operations ----------

def question_list_maker(num, par, operation):
    """
    Generates a list of questions based of requested number for set operations.

    :param num: number of requested questions.
    :param par: parameters that determine items in set.
    :param operation: type of operation on sets.
    :return: a list containing questions.
    """
    output = []
    for i in range(num):
        output.append(functions.choices(par, operation))
    return js.json_maker(operation, output)


@app.route('/union/<int:num>/<int:par>', methods=['GET'])
def union(num, par):
    """
    A function returns question for union of two input sets.

    :param num: number of questions.
    :param par: type of items in each sets based on documentation.
    :return: questions in JSON format.
    """
    output = question_list_maker(num, par, 'union')
    return jsonify(output)


@app.route('/intersection/<int:num>/<int:par>', methods=['GET'])
def intersection(num, par):
    """
    A function returns question for intersection of two input sets.

    :param num: number of questions.
    :param par: type of items in each sets based on documentation.
    :return: questions in JSON format.
    """
    output = question_list_maker(num, par, 'intersection')
    return jsonify(output)


@app.route('/difference/<int:num>/<int:par>', methods=['GET'])
def difference(num, par):
    """
       A function returns question for difference of two input sets.

       :param num: number of questions.
       :param par: type of items in each sets based on documentation.
       :return: questions in JSON format.
       """
    output = question_list_maker(num, par, 'difference')
    return jsonify(output)


@app.route('/cartesian/<int:num>/<int:par>', methods=['GET'])
def cartesian(num, par):
    """
       A function returns question for cartesian product of two input sets.

       :param num: number of questions.
       :param par: type of items in each sets based on documentation.
       :return: questions in JSON format.
       """
    output = question_list_maker(num, par, 'cartesian')
    return jsonify(output)


@app.route('/symmetric_difference/<int:num>/<int:par>', methods=['GET'])
def symmetric_difference(num, par):
    """
       A function returns question for symmetric difference of two input sets.

       :param num: number of questions.
       :param par: type of items in each sets based on documentation.
       :return: questions in JSON format.
       """
    output = question_list_maker(num, par, 'symmetric_difference')
    return jsonify(output)


@app.route('/partition/<int:num>/<int:par>', methods=['GET'])
def partition(num, par):
    """
       A function returns question for partitions of a generated set.

       :param num: number of questions.
       :param par: type of items in the set based on documentation.
       :return: questions in JSON format.
       """
    output = question_list_maker(num, par, 'partition')
    return jsonify(output)


@app.route('/complement/<int:num>/<int:par>', methods=['GET'])
def complement(num, par):
    """
        A function returns question for complement of a generated set.

        :param num: number of questions.
        :param par: type of items in the set based on documentation.
        :return: questions in JSON format.
    """
    output = question_list_maker(num, par, 'complement')
    return jsonify(output)


@app.route('/random/<int:num>', methods=['GET'])
def random_qa(num):
    """
    Generates random questions from the topics of set operations.

    :param num: number of questions.
    :return: questions and multiple choice answer options in JSON foramt.
    """
    output = []

    # list of available topics
    topics = ['union', 'intersection', 'difference', 'symmetric_difference', 'partition', 'cartesian']

    # generates asked number of questions and add them to the list(output) out of topics
    for i in range(num):
        topic = random.choice(topics)
        output.append(functions.choices('11', topic))

    return jsonify(js.json_maker('Random', output))

# ---------- Functions ----------


# DEBUG : Make multiple choice options
@app.route('/function/<int:num>', methods=['GET'])
def general_function(num):
    """
    Generates questions for determining if a set is function or not and if so what kind.

    :param num: number of questions.
    :return: questions in JSON format.
    """
    global zip
    # output_json = {}
    output = []
    for i in range(num):
        A = []
        B = []
        # question_json = 'question ' + str(i + 1)
        for i in range(random.randint(3, 6)):
            A.append(random.randint(1, 10))
        for i in range(random.randint(3, 6)):
            B.append(random.randint(1, 10))
        zip1 = list(zip(A, B))

        question = 'Is f(x) from A to B a function ? If so what kind of function it is ? f(x)=' + str(zip1)
        answer = functions.function(A, B)
        # output.update({question_json: {'A': A, 'B': B, 'question': question, 'answer': str(answer)}})
        answer_options = ['General function', 'Surjective function', 'Injective function', 'Bijective function',
                          'Not function']
        output_json = js.question_json_maker(question, answer)
        output.append(output_json)
    output_json = js.json_maker('function', output)
    return jsonify(output_json)


@app.route('/function/floorceiling/<int:num>', methods=['GET'])
def floor_ceiling_function(num):
    """
    Generates floor and ceiling function with random floats and asks for the answer.

    :param num: number of questions.
    :return: questions in JSON format.
    """
    global question_list_maker, answer
    # output_json = {}
    output = []
    # r_floor_symbol = u"\u230B"
    # l_floor_symbol = u"\u230A"
    # r_ceiling_symbol = u"\u2309"
    # l_ceiling_symbol = u"\u2308"
    r_floor_symbol = '&rfloor;'
    l_floor_symbol = '&lfloor;'
    r_ceiling_symbol = '&rceil;'
    l_ceiling_symbol = '&lceil;'
    A = 0
    for i in range(num):
        # question_json = 'question ' + str(i + 1)
        A = round(random.uniform(-40, 40), 2)
        identifier = random.randint(0, 10)
        if identifier % 2 == 0:
            question_list_maker = l_floor_symbol + str(A) + r_floor_symbol + ' ?'
            answer = str(math.floor(A))
        else:
            question_list_maker = l_ceiling_symbol + str(A) + r_ceiling_symbol + ' ?'
            answer = str(math.ceil(A))
        # output.update({question_json: {'question': question, 'answer': answer}})
        output_json = js.question_json_maker(question_list_maker, answer)
        output.append(output_json)
    output_json = js.json_maker('floor and ceiling function', output)
    return jsonify(output_json)


@app.route('/function/inverse/<int:num>', methods=['GET'])
def inverse_of_function(num):
    """
    Generates a random function and asks for inverse of it.

    :param num: number of questions.
    :return: questions in JSON format.
    """
    global zip
    # output_json = {}
    output = []
    for i in range(num):
        A = []
        B = []
        set_len = random.randint(3, 6)
        # question_json = 'question ' + str(i + 1)
        while len(A) != set_len:
            rand_int = random.randint(1, 15)
            if rand_int not in A:
                A.append(rand_int)
        while len(B) != set_len:
            rand_int = random.randint(15, 30)
            if rand_int not in B:
                B.append(rand_int)
        zip1 = list(zip(A, B))
        zip2 = list(zip(B, A))

        question = 'What is the inverse of function f=' + str(zip1) + ' ?'
        answer = str(zip2)

        # output.update({question_json: {'question': question, 'answer': str(answer)}})
        output_json = js.question_json_maker(question, answer)
        output.append(output_json)
    output_json = js.json_maker('inverse of a function', output)
    return jsonify(output_json)

# DEBUG : Make sure its a function first, then ask for domain.
@app.route('/function/domain/<int:num>', methods=['GET'])
def domain(num):
    """
    Generates a function output and asks for its domain.

    :param num: number of questions.(int)
    :return: question, answer, answer choices and topic.(JSON)
    """
    questions = []
    for i in range(num):
        questions.append(functions.domain())
    return jsonify(js.json_maker('function domain', questions))

# DEBUG : Make sure its a function first, then ask for target.
@app.route('/function/target/<int:num>', methods=['GET'])
def target(num):
    """
       Generates a function output and asks for its target.

       :param num: number of questions.(int)
       :return: question, answer, answer choices and topic.(JSON)
       """
    questions = []
    for i in range(num):
        questions.append(functions.target())
    return jsonify(js.json_maker('function domain', questions))


# ---------- Probabilities ----------

@app.route('/probability/event/<int:num>', methods=['GET'])
def event_probability(num):
    questions = []

    for i in range(num):
        question_list = [functions.event_probability_1(), functions.event_probability_2()]
        questions.append(random.choice(question_list))
    return jsonify(js.json_maker('probability of an event', questions))


@app.route('/probability/permutation/<int:num>', methods=['GET'])
def permutation_1(num):
    questions = []

    for i in range(num):
        questions.append(functions.permutation_1())
    return jsonify(js.json_maker('permutation', questions))


@app.route('/probability/combination/<int:num>', methods=['GET'])
def combination_1(num):
    questions = []

    for i in range(num):
        questions.append(functions.combination_1())
    return jsonify(js.json_maker('combination', questions))


# ---------- App Run ----------
if __name__ == '__main__':
    app.run()
