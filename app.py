import math
from flask import Flask, jsonify, request, render_template
import random_set as rs
import random
import jsonify as js

app = Flask(__name__)


def question(num, par, operation):
    output = []
    for i in range(num):
        output.append(rs.choices(par, operation))
    return js.title_maker(operation, output)


@app.route('/', methods=['GET'])
def index():
    return render_template('./index.html')


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
        answer_options = ['General function', 'Surjective function', 'Injective function', 'Bijective function',
                          'Not function']
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


@app.route('/random/<int:num>', methods=['GET'])
def random_qa(num):
    output = []
    operations = ['union', 'intersection', 'difference', 'symmetric_difference', 'partition', 'cartesian']
    for i in range(num):
        operation = random.choice(operations)
        output.append(rs.choices('11', operation))
    return jsonify(js.title_maker('Random', output))


@app.route('/function/domain/<int:num>', methods=['GET'])
def domain(num):
    questions = []
    for i in range(num):
        questions.append(rs.domain())
    return jsonify(js.title_maker('function domain', questions))


@app.route('/function/target/<int:num>', methods=['GET'])
def target(num):
    questions = []
    for i in range(num):
        questions.append(rs.target())
    return jsonify(js.title_maker('function domain', questions))


if __name__ == '__main__':
    app.run()
