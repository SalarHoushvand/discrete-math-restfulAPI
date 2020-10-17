# -----------------------------------------------------------
# API to generate random questions for discrete mathematics topics
# and outputs them in a JSON file.
#
# 2020 East Carolina University
# email salarhoushvand@gmail.com
# -----------------------------------------------------------

# ---------- Imports ----------

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


@app.route('/set-union', defaults={'num': 1, 'par': 11}, methods=['GET'])
@app.route('/set-union/<int:num>', defaults={'par': 11}, methods=['GET'])
@app.route('/set-union/<int:num>/<int:par>', methods=['GET'])
def set_union(num, par):
    """
    A function returns question for union of two input sets.

    :param num: number of questions.
    :param par: type of items in each sets based on documentation.
    :return: questions in JSON format.
    """
    output = question_list_maker(num, par, 'set-union')
    return jsonify(output)


@app.route('/set-intersection', defaults={'num': 1, 'par': 11}, methods=['GET'])
@app.route('/set-intersection/<int:num>', defaults={'par': 11}, methods=['GET'])
@app.route('/set-intersection/<int:num>/<int:par>', methods=['GET'])
def set_intersection(num, par):
    """
    A function returns question for intersection of two input sets.

    :param num: number of questions.
    :param par: type of items in each sets based on documentation.
    :return: questions in JSON format.
    """
    output = question_list_maker(num, par, 'set-intersection')
    return jsonify(output)


@app.route('/set-difference', defaults={'num': 1, 'par': 11}, methods=['GET'])
@app.route('/set-difference/<int:num>', defaults={'par': 11}, methods=['GET'])
@app.route('/set-difference/<int:num>/<int:par>', methods=['GET'])
def set_difference(num, par):
    """
       A function returns question for difference of two input sets.

       :param num: number of questions.
       :param par: type of items in each sets based on documentation.
       :return: questions in JSON format.
       """
    output = question_list_maker(num, par, 'set-difference')
    return jsonify(output)


@app.route('/cartesian-product', defaults={'num': 1, 'par': 11}, methods=['GET'])
@app.route('/cartesian-product/<int:num>', defaults={'par': 11}, methods=['GET'])
@app.route('/cartesian-product/<int:num>/<int:par>', methods=['GET'])
def cartesian_product(num, par):
    """
       A function returns question for cartesian product of two input sets.

       :param num: number of questions.
       :param par: type of items in each sets based on documentation.
       :return: questions in JSON format.
       """
    output = question_list_maker(num, par, 'cartesian-product')
    return jsonify(output)


@app.route('/set-symmetric-difference', defaults={'num': 1, 'par': 11}, methods=['GET'])
@app.route('/set-symmetric-difference/<int:num>', defaults={'par': 11}, methods=['GET'])
@app.route('/set-symmetric-difference/<int:num>/<int:par>', methods=['GET'])
def set_symmetric_difference(num, par):
    """
       A function returns question for symmetric difference of two input sets.

       :param num: number of questions.
       :param par: type of items in each sets based on documentation.
       :return: questions in JSON format.
       """
    output = question_list_maker(num, par, 'set-symmetric-difference')
    return jsonify(output)


@app.route('/set-partition', defaults={'num': 1, 'par': 11}, methods=['GET'])
@app.route('/set-partition/<int:num>', defaults={'par': 11}, methods=['GET'])
@app.route('/set-partition/<int:num>/<int:par>', methods=['GET'])
def set_partition(num, par):
    """
       A function returns question for partitions of a generated set.

       :param num: number of questions.
       :param par: type of items in the set based on documentation.
       :return: questions in JSON format.
       """
    output = question_list_maker(num, par, 'set-partition')
    return jsonify(output)


@app.route('/set-complement', defaults={'num': 1}, methods=['GET'])
@app.route('/set-complement/<int:num>', methods=['GET'])
def set_complement(num):
    """
        A function returns question for complement of a generated set.

        :param num: number of questions.
        :param par: type of items in the set based on documentation.
        :return: questions in JSON format.
    """
    questions = []
    for i in range(num):
        questions.append(functions.set_complement())
    return jsonify(js.json_maker('set-complement', questions))


@app.route('/random', defaults={'num': 1}, methods=['GET'])
@app.route('/random/<int:num>', methods=['GET'])
def random_qa(num):
    """
    Generates random questions from the topics of set operations.

    :param num: number of questions.
    :return: questions and multiple choice answer options in JSON foramt.
    """
    output = []

    # list of available topics
    topics = ['set-union', 'set-intersection', 'set-difference', 'set-symmetric-difference', 'set-partition',
              'cartesian-product']

    # generates asked number of questions and add them to the list(output) out of topics
    for i in range(num):
        topic = random.choice(topics)
        output.append(functions.choices('11', topic))

    return jsonify(js.json_maker('random', output))


@app.route('/venn-diagram', defaults={'num': 1}, methods=['GET'])
@app.route('/venn-diagram/<int:num>')
def venn_diagram(num):
    """
     Generates random questions for Venn diagram.
    :param num: number of questions.
    :return: questions in JSON format.
    """
    questions = []
    for i in range(num):
        questions.append(functions.intersection_venn())
    return jsonify(js.json_maker('venn-diagram', questions))


# ---------- Functions ----------


# DEBUG : for some functions like (4,1) (4,1) gives not functions (eliminate repeated answers)
@app.route('/function-definition', defaults={'num': 1}, methods=['GET'])
@app.route('/function-definition/<int:num>', methods=['GET'])
def function_definition(num):
    """
    Generates questions for determining if a set is function or not and if so what kind.

    :param num: number of questions.
    :return: questions in JSON format.
    """
    questions = []

    for i in range(num):
        questions.append(functions.general_function())
    return jsonify(js.json_maker('function-definition', questions))


@app.route('/ceiling-function', defaults={'num': 1}, methods=['GET'])
@app.route('/ceiling-function/<int:num>', methods=['GET'])
def ceiling_function(num):
    """
    Generates floor and ceiling function with random floats and asks for the answer.

    :param num: number of questions.
    :return: questions in JSON format.
    """
    questions = []

    for i in range(num):
        questions.append(functions.ceiling_function())
    return jsonify(js.json_maker('ceiling-function', questions))


@app.route('/floor-function', defaults={'num': 1}, methods=['GET'])
@app.route('/floor-function/<int:num>', methods=['GET'])
def floor_function(num):
    """
    Generates floor and ceiling function with random floats and asks for the answer.

    :param num: number of questions.
    :return: questions in JSON format.
    """
    questions = []

    for i in range(num):
        questions.append(functions.floor_function())
    return jsonify(js.json_maker('floor-function', questions))


@app.route('/inverse-function', defaults={'num': 1}, methods=['GET'])
@app.route('/inverse-function/<int:num>', methods=['GET'])
def inverse_function(num):
    """
    Generates a random function and asks for inverse of it.

    :param num: number of questions.
    :return: questions in JSON format.
    """
    questions = []

    for i in range(num):
        questions.append(functions.inverse_function())
    return jsonify(js.json_maker('inverse-function', questions))


# DEBUG : Make sure its a function first, then ask for domain.
@app.route('/function-domain', defaults={'num': 1}, methods=['GET'])
@app.route('/function-domain/<int:num>', methods=['GET'])
def function_domain(num):
    """
    Generates a function output and asks for its domain.

    :param num: number of questions.(int)
    :return: question, answer, answer choices and topic.(JSON)
    """
    questions = []
    for i in range(num):
        questions.append(functions.function_domain())
    return jsonify(js.json_maker('function-domain', questions))


# DEBUG : Make sure its a function first, then ask for target.
@app.route('/function-target', defaults={'num': 1}, methods=['GET'])
@app.route('/function-target/<int:num>', methods=['GET'])
def function_target(num):
    """
       Generates a function output and asks for its target.

       :param num: number of questions.(int)
       :return: question, answer, answer choices and topic.(JSON)
       """
    questions = []
    for i in range(num):
        questions.append(functions.function_target())
    return jsonify(js.json_maker('function-target', questions))


@app.route('/one-to-one-function/<int:num>')
def one_to_one_function(num):
    """
    Generates a question for one to one function using equations.

    :param num: number of questions.(int)
    :return: question, answer, answer choices and topic.(JSON)
    """
    questions = []
    for i in range(num):
        questions.append(functions.one_to_one_function())
    return jsonify(js.json_maker('one-to-one-function', questions))


# ---------- Probabilities ----------

@app.route('/probability-event', defaults={'num': 1}, methods=['GET'])
@app.route('/probability-event/<int:num>', methods=['GET'])
def probability_event(num):
    """
    Questions for probability of an event.

    :param num:  number of questions.(int)
    :return: question, answer, answer choices and topic.(JSON)
    """
    questions = []

    for i in range(num):
        question_list = [functions.event_probability_1(), functions.event_probability_2(),
                         functions.event_probability_3()]
        questions.append(random.choice(question_list))
    return jsonify(js.json_maker('probability-event', questions))


@app.route('/probability/permutation/<int:num>', methods=['GET'])
def permutation(num):
    """
    Questions for permutation.

    :param num:  number of questions.(int)
    :return: question, answer, answer choices and topic.(JSON)
    """
    questions = []

    for i in range(num):
        question_list = [functions.permutation_1(), functions.permutation_2()]
        questions.append(random.choice(question_list))
    return jsonify(js.json_maker('permutation', questions))


@app.route('/probability/multiplication/<int:num>', methods=['GET'])
def multiplication(num):
    """
    Questions for multiplication.

    :param num:  number of questions.(int)
    :return: question, answer, answer choices and topic.(JSON)
    """
    questions = []

    for i in range(num):
        question_list = [functions.multiplication_2(), functions.multiplication_3(),
                         functions.multiplication_4()]
        questions.append(random.choice(question_list))
    return jsonify(js.json_maker('multiplication', questions))


@app.route('/probability/combination/<int:num>', methods=['GET'])
def combination(num):
    """
    Questions for combination.

    :param num:  number of questions.(int)
    :return: question, answer, answer choices and topic.(JSON)
    """
    questions = []

    for i in range(num):
        question_list = [functions.combination_2(), functions.combination_1(), functions.combination_3()]
        questions.append(random.choice(question_list))
    return jsonify(js.json_maker('combination', questions))


@app.route('/probability/conditional/<int:num>', methods=['GET'])
def conditional_probability(num):
    """
    Questions for conditional probability.

    :param num:  number of questions.(int)
    :return: question, answer, answer choices and topic.(JSON)
    """
    questions = []

    for i in range(num):
        questions.append(functions.conditional_probability_1())
    return jsonify(js.json_maker('conditional probability', questions))


@app.route('/probability/union/<int:num>', methods=['GET'])
def probability_union(num):
    """
    Questions for union of events.

    :param num:  number of questions.(int)
    :return: question, answer, answer choices and topic.(JSON)
    """
    questions = []

    for i in range(num):
        questions.append(functions.probability_union())
    return jsonify(js.json_maker('probability union', questions))


@app.route('/probability/complement/<int:num>', methods=['GET'])
def probability_complement(num):
    """
    Questions for complement of events.

    :param num:  number of questions.(int)
    :return: question, answer, answer choices and topic.(JSON)
    """

    questions = []

    for i in range(num):
        questions.append(functions.probability_complement())
    return jsonify(js.json_maker('probability complement', questions))


@app.route('/probability/bayes/<int:num>', methods=['GET'])
def bayes_theorem(num):
    """
    Questions for Bayes theorem.

    :param num:  number of questions.(int)
    :return: question, answer, answer choices and topic.(JSON)
        """
    questions = []

    for i in range(num):
        questions.append(functions.bayes_theorem())
    return jsonify(js.json_maker('bayes theorem', questions))


# ======================================================================================================================


@app.route('/topics', methods=['GET'])
def topics():
    """
    List of topics to be used in a third party application.
    :return: JSON file.
    """
    topics = {"topics": {
        'bayes theorem': '/probability/bayes/',
        'probability complement': '/probability/complement/',
        'probability union': '/probability/union/',
        'conditional probability': '/probability/conditional/',
        'combination': '/probability/combination/',
        'multiplication': '/probability/multiplication/',
        'permutation': '/probability/permutation/',
        'probability of an event': '/probability/event/',
        'function-target': '/function-target/',
        'function-domain': '/function-domain/',
        'inverse-function': '/inverse-function/',
        'ceiling-function': '/ceiling-function/',
        'floor-function': '/floor-function/',
        'function-definition': '/function-definition/',
        'set-theory': '/random/',
        'set-complement': '/set-complement/',
        'set-partition': '/set-partition/',
        'set-symmetric-difference': '/set-symmetric-difference/',
        'cartesian-product': '/cartesian-product/',
        'set-difference': '/set-difference/',
        'set-intersection': '/set-intersection/',
        'set-union': '/set-union/',
        'venn-diagram': '/venn-diagram/',
        'one to one function': '/function/equation/'
    }}
    return jsonify(topics)


# ---------- Error Handling ----------


@app.errorhandler(404)
def not_found(e):
    error_msg = {
        "error": "404",
        "message": "The requested resource does not exist.",
        "detail": " Ensure that the URL you are using is correct."
    }
    return jsonify(error_msg), 404


@app.errorhandler(500)
def server_error(e):
    error_msg = {
        "error": "500",
        "message": "A generic error occurred on the server.",
        "detail": "please try again later."
    }
    return jsonify(error_msg), 500


@app.errorhandler(405)
def server_error(e):
    error_msg = {
        "error": "405",
        "message": "Method not allowed.",
        "detail": "You requested a method that is not allowed by server."
    }
    return jsonify(error_msg), 405


# ---------- App Run ----------
if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=5000)
