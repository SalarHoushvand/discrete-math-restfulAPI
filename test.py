import requests

params = ['1', '2', '3', '4', '5', '6', '7']

param = []
for m in params:
    for n in params:
        param.append(m + n)

status_codes_list = []


# test for set theory
def set_theory_test():
    """
    Test function for set theory
    """
    topics_with_param = ['set-union', 'set-difference', 'set-symmetric-difference', 'cartesian-product',
                         'set-partition',
                         'set-intersection']

    topics_without_param = ['venn-diagram', 'set-complement']
    print('test started for set theory ...')
    test_case = 0
    for topic in topics_with_param:
        for p in param:
            for i in range(20):
                x = requests.get('http://127.0.0.1:5000/' + topic + '/' + str(i) + '/' + p)
                status_codes_list.append(x.status_code)
                if x.status_code is not 200:
                    print('Error : ' + str(x.status_code))
                if x.headers.get('content-type') is not 'application/json':
                    x.headers.get('content-type')
                test_case = test_case + 1
    for topic in topics_without_param:
        for i in range(20):
            x = requests.get('http://127.0.0.1:5000/' + topic + '/' + str(i))
            status_codes_list.append(x.status_code)
            if x.status_code is not 200:
                print('Error : ' + str(x.status_code))
            if x.headers.get('content-type') is not 'application/json':
                x.headers.get('content-type')
            test_case = test_case + 1
    print(f'{str(test_case)} test cases for {str(len(topics_with_param)+len(topics_without_param))} topics in '
          f'set theory with success (response code 200).')
    print(f'{str(test_case)} test cases for {str(len(topics_with_param)+len(topics_without_param))} topics in '
          f'set theory has body type of application/json.')
    print('test completed for set theory. \n')


def functions_test():
    """
   Test function for functions
    """
    topics = ['ceiling-function', 'floor-function', 'function-definition', 'function-domain',
              'function-target', 'inverse-function', 'one-to-one-function']
    print('test started for functions ...')
    test_case = 0
    for topic in topics:
        for i in range(20):
            x = requests.get('http://127.0.0.1:5000/' + topic + '/' + str(i))
            status_codes_list.append(x.status_code)
            if x.status_code is not 200:
                print('Error : ' + str(x.status_code))
            if x.headers.get('content-type') is not 'application/json':
                x.headers.get('content-type')
            test_case = test_case + 1
    print(f'{str(test_case)} test cases for {str(len(topics))} topics in functions with success (response code 200).')
    print(f'{str(test_case)} test cases for {str(len(topics))} topics in functions has body type of application/json.')
    print('test completed for functions. \n')


def probabilities_test():
    """
   Test function for probabilities
    """
    topics = ['event-probability', 'permutation', 'multiplication-rule', 'combination',
              'conditional-probability', 'probability-union', 'probability-complement', 'bayes-theorem']
    print('test started for probabilities ...')
    test_case = 0
    for topic in topics:
        for i in range(20):
            x = requests.get('http://127.0.0.1:5000/' + topic + '/' + str(i))
            status_codes_list.append(x.status_code)
            if x.status_code is not 200:
                print('Error : ' + str(x.status_code))
            if x.headers.get('content-type') is not 'application/json':
                x.headers.get('content-type')
            test_case = test_case + 1
    print(f'{str(test_case)} test cases for {str(len(topics))} topics in '
          f'probabilities with success (response code 200).')
    print(f'{str(test_case)} test cases for {str(len(topics))} topics in '
          f'probabilities has body type of application/json.')
    print('test completed for probabilities. \n')


def relations_test():
    """
   Test function for probabilities
    """
    topics = ['reflexive-relation', 'irreflexive-relation', 'symmetric-relation', 'asymmetric-relation',
              'antisymmetric-relation', 'transitive-relation', 'reflexive-closure', 'symmetric-closure',
              'transitive-closure']
    print('test started for relations ...')
    test_case = 0
    for topic in topics:
        for i in range(20):
            x = requests.get('http://127.0.0.1:5000/' + topic + '/' + str(i))
            status_codes_list.append(x.status_code)
            if x.status_code is not 200:
                print('Error : ' + str(x.status_code))
            if x.headers.get('content-type') is not 'application/json':
                x.headers.get('content-type')
            test_case = test_case + 1
    print(f'{str(test_case)} test cases for {str(len(topics))} topics in relations with success (response code 200).')
    print(f'{str(test_case)} test cases for {str(len(topics))} topics in relations has body type of application/json.')
    print('test completed for relations. \n')



set_theory_test()
functions_test()
probabilities_test()
relations_test()