import math
from flask import Flask, jsonify, request
import random_set as rs
import random
import jsonify as js

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return jsonify({'Welcome message': 'Welcome to api, start calling ex: /union/5/11 which means : '
                                       '/operation name/number of questions/<first set type><second set type>'})


def question(num, par, operation):
    # output_json = {}
    output = []
    # topic = js.title_maker(operation)

    for i in range(num):
        num2 = str(par)
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

        if operation == 'partition' or operation == 'complement':
            question = 'What is the ' + operation + ' of this set? '
        else:
            question = ('What is the ' + operation + ' of these two sets? ').replace('_', ' ')
        answer = rs.set_operation(op=operation, set_1=set1, set_2=set2)
        question_json = 'question ' + str(i + 1)
        # output.update({question_json: {'set1': set1, 'set2': set2, 'question': question, 'answer': answer}})
        output_json = js.json_maker(str(question) + ' ' + str(set1) + ' ' + str(set2), answer)
        output.append(output_json)
    output_json = js.title_maker(operation, output)
    return output_json


@app.route('/union/<int:num>/<int:par>', methods=['GET'])
def union(num, par):
    output = question(num, par, 'union')
    return jsonify(output)


@app.route('/intersection/<int:num>/<int:par>', methods=['GET'])
def intersection(num, par):
    output = question(num, par, 'intersection')
    return jsonify(output)


@app.route('/difference/<int:num>/<int:par>', methods=['GET'])
def difference(num, par):
    output = question(num, par, 'difference')
    return jsonify(output)


@app.route('/cartesian/<int:num>/<int:par>', methods=['GET'])
def cartesian(num, par):
    output = question(num, par, 'cartesian')
    return jsonify(output)


@app.route('/symmetric_difference/<int:num>/<int:par>', methods=['GET'])
def symmetric_difference(num, par):
    output = question(num, par, 'symmetric_difference')
    return jsonify(output)


@app.route('/partition/<int:num>/<int:par>', methods=['GET'])
def partition(num, par):
    output = question(num, par, 'partition')
    return jsonify(output)


@app.route('/complement/<int:num>/<int:par>', methods=['GET'])
def complement(num, par):
    output = question(num, par, 'complement')
    return jsonify(output)


@app.route('/function/<int:num>', methods=['GET'])
def function(num):
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
        answer = rs.function(A, B)
        # output.update({question_json: {'A': A, 'B': B, 'question': question, 'answer': str(answer)}})
        output_json = js.json_maker(question, answer)
        output.append(output_json)
    output_json = js.title_maker('function', output)
    return jsonify(output_json)


@app.route('/function/floorceiling/<int:num>', methods=['GET'])
def floor_ceiling(num):
    global question, answer
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
            question = l_floor_symbol + str(A) + r_floor_symbol + ' ?'
            answer = str(math.floor(A))
        else:
            question = l_ceiling_symbol + str(A) + r_ceiling_symbol + ' ?'
            answer = str(math.ceil(A))
        # output.update({question_json: {'question': question, 'answer': answer}})
        output_json = js.json_maker(question, answer)
        output.append(output_json)
    output_json = js.title_maker('floor and ceiling function', output)
    return jsonify(output_json)


@app.route('/function/inverse/<int:num>', methods=['GET'])
def inverse(num):
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
        output_json = js.json_maker(question, answer)
        output.append(output_json)
    output_json = js.title_maker('inverse of a function', output)
    return jsonify(output_json)


@app.route('/random', methods=['GET'])
def random_qa():
    output = {}
    output.update(question(21, 11, 'union'))
    output.update(question(18, 11, 'intersection'))
    output.update(question(15, 11, 'difference'))
    output.update(question(12, 11, 'cartesian'))
    output.update(question(9, 11, 'symmetric_difference'))
    output.update(question(6, 11, 'partition'))
    output.update(question(3, 11, 'complement'))

    return jsonify(output)


if __name__ == '__main__':
    app.run()
