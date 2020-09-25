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
from flask_cors import CORS, cross_origin



# ---------- App ----------

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'



# ---------- Main Page ----------

@app.route('/', methods=['GET'])
@cross_origin()

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


# DEBUG : for some functions like (4,1) (4,1) gives not functions (eliminate repeated answers)
@app.route('/function/<int:num>', methods=['GET'])
def general_function(num):
    """
    Generates questions for determining if a set is function or not and if so what kind.

    :param num: number of questions.
    :return: questions in JSON format.
    """
    questions = []

    for i in range(num):
        questions.append(functions.general_function())
    return jsonify(js.json_maker('general function', questions))


@app.route('/function/floorceiling/<int:num>', methods=['GET'])
def floor_ceiling_function(num):
    """
    Generates floor and ceiling function with random floats and asks for the answer.

    :param num: number of questions.
    :return: questions in JSON format.
    """
    questions = []

    for i in range(num):
        questions.append(functions.floor_ceiling_function())
    return jsonify(js.json_maker('floor ceiling function', questions))


@app.route('/function/inverse/<int:num>', methods=['GET'])
def inverse_of_function(num):
    """
    Generates a random function and asks for inverse of it.

    :param num: number of questions.
    :return: questions in JSON format.
    """
    questions = []

    for i in range(num):
        questions.append(functions.inverse_of_function())
    return jsonify(js.json_maker('inverse of function', questions))


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
        question_list = [functions.event_probability_1(), functions.event_probability_2(),
                         functions.event_probability_3()]
        questions.append(random.choice(question_list))
    return jsonify(js.json_maker('probability of an event', questions))


@app.route('/probability/permutation/<int:num>', methods=['GET'])
def permutation(num):
    questions = []

    for i in range(num):
        question_list = [functions.permutation_1(), functions.permutation_2()]
        questions.append(random.choice(question_list))
    return jsonify(js.json_maker('permutation', questions))


@app.route('/probability/multiplication/<int:num>', methods=['GET'])
def multiplication(num):
    questions = []

    for i in range(num):
        question_list = [functions.multiplication_2(), functions.multiplication_3(),
                         functions.multiplication_4()]
        questions.append(random.choice(question_list))
    return jsonify(js.json_maker('multiplication', questions))


@app.route('/probability/combination/<int:num>', methods=['GET'])
def combination(num):
    questions = []

    for i in range(num):
        question_list = [functions.combination_2(), functions.combination_1(), functions.combination_3()]
        questions.append(random.choice(question_list))
    return jsonify(js.json_maker('combination', questions))


@app.route('/probability/conditional/<int:num>', methods=['GET'])
def conditional_probability(num):
    questions = []

    for i in range(num):
        questions.append(functions.conditional_probability_1())
    return jsonify(js.json_maker('conditional probability', questions))


@app.route('/probability/union/<int:num>', methods=['GET'])
def probability_union(num):
    questions = []

    for i in range(num):
        questions.append(functions.probability_union())
    return jsonify(js.json_maker('probability union', questions))


@app.route('/probability/complement/<int:num>', methods=['GET'])
def probability_complement(num):
    questions = []

    for i in range(num):
        questions.append(functions.probability_complement())
    return jsonify(js.json_maker('probability complement', questions))


@app.route('/probability/bayes/<int:num>', methods=['GET'])
def bayes_theorem(num):
    questions = []

    for i in range(num):
        questions.append(functions.bayes_theorem())
    return jsonify(js.json_maker('bayes theorem', questions))


@app.route('/relations_1/<int:num>', methods=['GET'])
def relations_1(num):
    questions = []

    for i in range(num):
        questions.append(functions.relations_1())
    return jsonify(js.json_maker('relations', questions))


@app.route('/relations_2/<int:num>', methods=['GET'])
def relations_2(num):
    questions = []

    for i in range(num):
        questions.append(functions.relations_2())
    return jsonify(js.json_maker('relations', questions))


@app.route('/relations_3/<int:num>', methods=['GET'])
def relations_3(num):
    questions = []

    for i in range(num):
        questions.append(functions.relations_3())
    return jsonify(js.json_maker('relations', questions))



@app.route('/relations_4/<int:num>', methods=['GET'])
def relations_4(num):
    questions = []

    for i in range(num):
        questions.append(functions.relations_4())
    return jsonify(js.json_maker('relations', questions))



@app.route('/relations_5/<int:num>', methods=['GET'])
def relations_5(num):
    questions = []

    for i in range(num):
        questions.append(functions.relations_5())
    return jsonify(js.json_maker('relations', questions))


@app.route('/relations_6/<int:num>', methods=['GET'])
def relations_6(num):
    questions = []

    for i in range(num):
        questions.append(functions.relations_6())
    return jsonify(js.json_maker('relations', questions))


@app.route('/relations/<int:num>')
def relations(num):
    questions = []

    for i in range(num):
        question_list = [functions.relations_1(), functions.relations_2(), functions.relations_3(), functions.relations_4(),
                         functions.relations_5(), functions.relations_6()]
        questions.append(random.choice(question_list))
    return jsonify(js.json_maker('Relations', questions))

@app.route('/img/<int:num>')
def img_test(num):
    questions = []
    for i in range(num):
        questions.append(functions.img_test())
    return jsonify(js.json_maker('image',questions))

@app.route('/topics', methods=['GET'])
def topics():
    topics = {"topics": {
        'Relations': '/relations/',
        'bayes theorem': '/probability/bayes/',
        'probability complement': '/probability/complement/',
        'probability union': '/probability/union/',
        'conditional probability': '/probability/conditional/',
        'combination': '/probability/combination/',
        'multiplication': '/probability/multiplication/',
        'permutation': '/probability/permutation/',
        'probability of an event': '/probability/event/',
        'function target': '/function/target/',
        'function domain': '/function/domain/',
        'inverse of a function': '/function/inverse/',
        'floor and ceiling function': '/function/floorceiling/',
        'general function': '/function/',
        'set theory': '/random/',
        'complement': '/complement/',
        'partition': '/partition/',
        'symmetric difference': '/symmetric_difference/',
        'cartesian product': '/cartesian/',
        'difference of sets': '/difference/',
        'intersection of sets': '/intersection/',
        'union of sets': '/union/',
        'img':'/img/'
    }}
    return jsonify(topics)


# ---------- App Run ----------
if __name__ == '__main__':
    app.run()
