from flask import Flask, jsonify, request
import random_set as rs

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if (request.method == 'POST'):
        some_json = request.get_json()
        return jsonify({'you send': some_json}), 201
    else:
        return jsonify({'about': 'hello world'})


@app.route('/union/<int:num>', methods=['GET'])
def union(num):
    output = {}
    for i in range(num):
        set1 = rs.random_set()
        set2 = rs.random_set()
        question = 'What is the union of these two sets? '
        answer  = rs.set_operation(op='union', set_1=set1, set_2=set2)
        question_json = 'question '+str(i+1)
        output.update({question_json:{'set1': set1, 'set2':set2, 'question':question, 'answer':answer}})
    print(output)
    return jsonify(output)

@app.route('/intersection/<int:num>', methods=['GET'])
def intersection(num):
    output = {}
    for i in range(num):
        set1 = rs.random_set()
        set2 = rs.random_set()
        question = 'What is the intersection of these two sets? '
        answer  = rs.set_operation(op='intersection', set_1=set1, set_2=set2)
        question_json = 'question '+str(i+1)
        output.update({question_json:{'set1': set1, 'set2':set2, 'question':question, 'answer':answer}})
    print(output)
    return jsonify(output)

@app.route('/difference/<int:num>', methods=['GET'])
def difference(num):
    output = {}
    for i in range(num):
        set1 = rs.random_set()
        set2 = rs.random_set()
        question = 'What is the difference of these two sets? '
        answer  = rs.set_operation(op='difference', set_1=set1, set_2=set2)
        question_json = 'question '+str(i+1)
        output.update({question_json:{'set1': set1, 'set2':set2, 'question':question, 'answer':answer}})
    print(output)
    return jsonify(output)


@app.route('/cartesian/<int:num>', methods=['GET'])
def cartesian(num):
    output = {}
    for i in range(num):
        set1 = rs.random_set()
        set2 = rs.random_set()
        question = 'What is the cartesian product of these two sets? '
        answer  = rs.set_operation(op='cartesian', set_1=set1, set_2=set2)
        question_json = 'question '+str(i+1)
        output.update({question_json:{'set1': set1, 'set2':set2, 'question':question, 'answer':answer}})
    print(output)
    return jsonify(output)


@app.route('/symmetric_difference/<int:num>', methods=['GET'])
def symmetric_difference(num):
    output = {}
    for i in range(num):
        set1 = rs.random_set()
        set2 = rs.random_set()
        question = 'What is the symmetric difference of these two sets? '
        answer  = rs.set_operation(op='symmetric_difference', set_1=set1, set_2=set2)
        question_json = 'question '+str(i+1)
        output.update({question_json:{'set1': set1, 'set2':set2, 'question':question, 'answer':answer}})
    print(output)
    return jsonify(output)


@app.route('/partition/<int:num>', methods=['GET'])
def partition(num):
    output = {}
    for i in range(num):
        set1 = rs.random_set()
        question = 'What is the partition of this set? '
        answer  = rs.set_operation(op='partition', set_1=set1)
        question_json = 'question '+str(i+1)
        output.update({question_json:{'set1': set1, 'question':question, 'answer':answer}})
    print(output)
    return jsonify(output)


@app.route('/complement/<int:num>', methods=['GET'])
def complement(num):
    output = {}
    for i in range(num):
        set1 = rs.random_set()
        question = 'What is the complement of this set? '
        answer  = rs.set_operation(op='complement', set_1=set1)
        question_json = 'question '+str(i+1)
        output.update({question_json:{'set1': set1, 'question':question, 'answer':answer}})
    print(output)
    return jsonify(output)




if __name__ == '__main__':
    app.run()
