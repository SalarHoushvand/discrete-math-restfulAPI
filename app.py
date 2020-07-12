from flask import Flask, jsonify, request
import random_set as rs

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return jsonify({'Welcome message': 'Welcome to api, start calling ex: /union/5/11 which means : '
                                       '/operation name/number of questions/<first set type><second set type>'})


def question(num, par, operation):
    output = {}
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
        output.update({question_json: {'set1': set1, 'set2': set2, 'question': question, 'answer': answer}})
    return output


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


@app.route('/random', methods=['GET'])
def random():
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
