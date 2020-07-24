import random
import jsonify as js

def domain(num):
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
        question = 'what is the domain of this function ? f(x)=' + str(zip1)
        answer = A

        return js.json_maker(question, answer)


print(domain(1))
