import random
import itertools
from functions import *


def is_reflexive(universe, relation):
    """
    Function to determine if a relation of a set is reflexiver
    :param universe: a set
    :param relation: a relation on set universe
    return: True if relation is a reflexiver relation of set universe
    """
    new_set = {(a, b) for a in universe for b in universe if a == b}
    if relation >= new_set:
        return True

    return False


def inverse_of_relation(r):
    """
    Function to determine the inverse of a relation
    :param r: a relation
    :return: inverse of the relation
    """
    return [(y, x) for (x, y) in r]


def is_symmetric(r):
    """
    Function to determine if a realtion is symmetric
    :param r: a relation
    :return: True if relation is symmetric, False otherwise
    """
    return set(r) == set([pair for pair in r if pair in inverse_of_relation(r)])


def is_asymmetric(r):
    """
    Function to determine if a realtion is asymmetric
    :param r: a relation
    :return: True if relation is asymmetric, False otherwise
    """
    return [pair for pair in r if pair in inverse_of_relation(r)] == []


def is_antisymmetric(r):
    """
    Function to determine if a realtion is antisymmetric
    :param r: a relation
    :return: True if relation is antisymmetric, False otherwise
    """
    for (x, y) in set([pair for pair in r if pair in inverse_of_relation(r)]):
        if x != y:
            return False
    return True


def binary_relations(n):
    '''Function to find all binary relations of a set n
    :param n: a python list of elements
    :return: all binary relations of set n
    '''
    cartesian = []
    for element in itertools.product(n, n):
        cartesian.append(element)
    result = [[]]
    for pair in cartesian:
        result = result + [L + [pair] for L in result]
    return result


def is_transitive(r, universe):
    """
    Function to determine if a relation is transitive
    :param r: a relation on set universe
    :param universe: a set
    :return: True if relation is transitive, False otherwise
    """
    for a in universe:
        for b in universe:
            if (a, b) in r:
                for c in universe:
                    if (b, c) in r and (a, c) not in r:
                        return False
    return True


def is_irreflexive(universe, relation):
    """
    Function to determine if a relation of a set is irreflexiver
    :param universe: a set
    :param relation: a relation on set universe
    return: True if relation is a reflexiver relation of set universe
    """
    new_set = {(a, b) for a in universe for b in universe if a == b}
    if relation >= new_set:
        return False

    return True


def transitive_closure_function(rel, universe):
    """
    Function to determine the transitive closure of a realtion
    :param rel: A list that represents a relation
    :return: The transitive closure of a relation
    """
    result = rel
    changed = True
    while changed:
        changed = False
        for a in universe:
            for b in universe:
                for c in universe:
                    if (a, b) in result and (b, c) in result and (a, c) not in result:
                        result.append((a, c))
                        changed = True
    return result


def symmetric_closure_function(rel):
    """
    Function to determine the symmetric closure of a relation
    :param rel: A list that represents a relation
    :return: The symmetric closure of relation rel
    """
    return rel + [(y, x) for (x, y) in rel if (y, x) not in rel]


def reflexive_closure_function(rel, universe):
    """
    Function to return the reflexive closure of a relation on a set
    :param rel: A list that is a relation on set universe
    :param universe: A list that represents a set
    :return: A list that is the  relexive closure of the relation rel on the set universe
    """
    return rel + [(x, x) for x in universe if (x, x) not in rel]


# ----- Questions ------


def reflexive_relation():
    """
    A T/F question for reflexive relation/
    :return: True or False
    """
    question_type = random.randint(0, 1)
    # False if 0, True if 1
    if question_type == 0:
        answer = False
        rand_set = list(set(random_set(integer=random.randint(2, 3))))
        relations = binary_relations(rand_set)
        random.shuffle(relations)
        ind_relation = []
        for i in range(len(relations)):
            if is_reflexive(set(rand_set), set(relations[i])) != True:
                ind_relation = relations[i]
                break
        question = (f'Is the relation R a reflecive relation of set A? A = {rand_set}, R = {ind_relation}').replace('[',
                                                                                                                    '{').replace(
            ']', '}')

    if question_type == 1:
        answer = True
        rand_set = list(set(random_set(integer=random.randint(2, 3))))
        relations = binary_relations(rand_set)
        random.shuffle(relations)
        ind_relation = []
        for i in range(len(relations)):
            if is_reflexive(set(rand_set), set(relations[i])) == True:
                ind_relation = relations[i]
                break
        question = (f'Is the relation R a reflecive relation of set A? A = {rand_set}, R = {ind_relation}').replace('[',
                                                                                                                    '{').replace(
            ']', '}')

    print(question)
    return answer


def irreflexive_relation():
    """
     A T/F question for irreflexive relation/
    :return: True or False

    """
    question_type = random.randint(0, 1)
    # False if 0, True if 1
    if question_type == 0:
        answer = False
        rand_set = list(set(random_set(integer=random.randint(2, 3))))
        relations = binary_relations(rand_set)
        random.shuffle(relations)
        ind_relation = []
        for i in range(len(relations)):
            if is_irreflexive(set(rand_set), set(relations[i])) != True:
                ind_relation = relations[i]
                break
        question = (f'Is the relation R an irreflecive relation of set A? A = {rand_set}, R = {ind_relation}').replace(
            '[', '{').replace(']', '}')

    if question_type == 1:
        answer = True
        rand_set = list(set(random_set(integer=random.randint(2, 3))))
        relations = binary_relations(rand_set)
        random.shuffle(relations)
        ind_relation = []
        for i in range(len(relations)):
            if is_irreflexive(set(rand_set), set(relations[i])) == True:
                ind_relation = relations[i]
                break
        question = (f'Is the relation R an irreflecive relation of set A? A = {rand_set}, R = {ind_relation}').replace(
            '[', '{').replace(']', '}')

    print(question)
    return answer


def symmetric_relation():
    """
     A T/F question for symmetric relation/
    :return: True or False
    """
    question_type = random.randint(0, 1)
    # False if 0, True if 1
    if question_type == 0:
        answer = False
        rand_set = list(set(random_set(integer=random.randint(2, 3))))
        relations = binary_relations(rand_set)
        random.shuffle(relations)
        ind_relation = []
        for i in range(len(relations)):
            if is_symmetric(relations[i]) != True:
                ind_relation = relations[i]
                break
        question = (f'Is the relation R a symmetric relation of set A? A = {rand_set}, R = {ind_relation}').replace('[',
                                                                                                                    '{').replace(
            ']', '}')

    if question_type == 1:
        answer = True
        rand_set = list(set(random_set(integer=random.randint(2, 3))))
        relations = binary_relations(rand_set)
        random.shuffle(relations)
        ind_relation = []
        for i in range(len(relations)):
            if is_symmetric(relations[i]) == True:
                ind_relation = relations[i]
                break
        question = (f'Is the relation R a symmetric relation of set A? A = {rand_set}, R = {ind_relation}').replace('[',
                                                                                                                    '{').replace(
            ']', '}')

    print(question)
    return answer


def assymetric_relation():
    """
     A T/F question for assymetric relation/
    :return: True or False
    """
    question_type = random.randint(0, 1)
    # False if 0, True if 1
    if question_type == 0:
        answer = False
        rand_set = list(set(random_set(integer=random.randint(2, 3))))
        rand_set = [1, 3, 9]
        relations = binary_relations(rand_set)
        random.shuffle(relations)
        ind_relation = []
        for i in range(len(relations)):
            if is_asymmetric(relations[i]) != True:
                ind_relation = relations[i]
                break
        question = (f'Is the relation R an asymmetric relation of set A? A = {rand_set}, R = {ind_relation}').replace(
            '[', '{').replace(']', '}')

    if question_type == 1:
        answer = True
        rand_set = list(set(random_set(integer=random.randint(2, 3))))
        relations = binary_relations(rand_set)
        random.shuffle(relations)
        ind_relation = []
        for i in range(len(relations)):
            if is_asymmetric(relations[i]) == True:
                ind_relation = relations[i]
                break
        question = (f'Is the relation R an asymmetric relation of set A? A = {rand_set}, R = {ind_relation}').replace(
            '[', '{').replace(']', '}')

    print(question)
    return answer


def anti_symmetric():
    """
     A T/F question for anti symetric relation/
    :return: True or False
    """
    question_type = random.randint(0, 1)
    # False if 0, True if 1
    if question_type == 0:
        answer = False
        rand_set = list(set(random_set(integer=random.randint(2, 3))))
        relations = binary_relations(rand_set)
        random.shuffle(relations)
        ind_relation = []
        for i in range(len(relations)):
            if is_antisymmetric(relations[i]) != True:
                ind_relation = relations[i]
                break
        question = (
            f'Is the relation R an antisymmetric relation of set A? A = {rand_set}, R = {ind_relation}').replace('[',
                                                                                                                 '{').replace(
            ']', '}')

    if question_type == 1:
        answer = True
        rand_set = list(set(random_set(integer=random.randint(2, 3))))
        relations = binary_relations(rand_set)
        random.shuffle(relations)
        ind_relation = []
        for i in range(len(relations)):
            if is_antisymmetric(relations[i]) == True:
                ind_relation = relations[i]
                break
        question = (
            f'Is the relation R an antisymmetric relation of set A? A = {rand_set}, R = {ind_relation}').replace('[',
                                                                                                                 '{').replace(
            ']', '}')

    print(question)
    return answer


def transitive_relation():
    """
    A T/F question for transitive relation/
    :return: True or False
    """
    question_type = random.randint(0, 1)
    # False if 0, True if 1
    if question_type == 0:
        answer = False
        rand_set = list(set(random_set(integer=random.randint(2, 3))))
        relations = binary_relations(rand_set)
        random.shuffle(relations)
        ind_relation = []
        for i in range(len(relations)):
            if is_transitive(relations[i], rand_set) != True:
                ind_relation = relations[i]
                break
        question = (f'Is the relation R a transitive relation of set A? A = {rand_set}, R = {ind_relation}').replace(
            '[', '{').replace(']', '}')

    if question_type == 1:
        answer = True
        rand_set = list(set(random_set(integer=random.randint(2, 3))))
        relations = binary_relations(rand_set)
        random.shuffle(relations)
        ind_relation = []
        for i in range(len(relations)):
            if is_transitive(relations[i], rand_set) == True:
                ind_relation = relations[i]
                break
        question = (f'Is the relation R a transitive relation of set A? A = {rand_set}, R = {ind_relation}').replace(
            '[', '{').replace(']', '}')

    print(question)
    return answer


def reflexive_closure():
    """
    A T/F question for transitive relation/
    :return: True or False
    """

    question_type = random.randint(0, 1)
    if question_type == 0:
        answer = False
        rand_set = list(set(random_set(integer=random.randint(2, 4))))
        relations = binary_relations(rand_set)
        relation_1 = relations[random.randint(1, len(relations) - 1)]
        closure_relation = relations[random.randint(1, len(relations) - 1)]
        question = (
            f'Is {closure_relation} the reflexive closure of relation R on set A? A = {rand_set}, R = {relation_1}').replace(
            '[', '{').replace(']', '}')
    if question_type == 1:
        answer = True
        rand_set = [1, 3, 9]
        relations = binary_relations(rand_set)
        relation_1 = relations[random.randint(1, len(relations) - 1)]
        closure_relation = reflexive_closure_function(relation_1, rand_set)
        question = (
            f'Is {closure_relation} the reflexive closure of relation R on set A? A = {rand_set}, R = {relation_1}').replace(
            '[', '{').replace(']', '}')

    print(question)
    return answer


def symmetric_closure():
    question_type = random.randint(0, 1)
    if question_type == 0:
        answer = False
        rand_set = list(set(random_set(integer=random.randint(2, 4))))
        relations = binary_relations(rand_set)
        relation_1 = relations[random.randint(1, len(relations) - 1)]
        closure_relation = relations[random.randint(1, len(relations) - 1)]
        question = (
            f'Is {closure_relation} the symmetric closure of relation R on set A? A = {rand_set}, R = {relation_1}').replace(
            '[', '{').replace(']', '}')
    if question_type == 1:
        answer = True
        rand_set = [1, 3, 9]
        relations = binary_relations(rand_set)
        relation_1 = relations[random.randint(1, len(relations) - 1)]
        closure_relation = symmetric_closure_function(relation_1)
        question = (
            f'Is {closure_relation} the symmetric closure of relation R on set A? A = {rand_set}, R = {relation_1}').replace(
            '[', '{').replace(']', '}')

    print(question)
    return answer


def transitive_closure():
    question_type = random.randint(0, 1)
    if question_type == 0:
        answer = False
        rand_set = list(set(random_set(integer=random.randint(2, 4))))
        relations = binary_relations(rand_set)
        relation_1 = relations[random.randint(1, len(relations) - 1)]
        closure_relation = relations[random.randint(1, len(relations) - 1)]
        question = (
            f'Is {closure_relation} the transitive closure of relation R on set A? A = {rand_set}, R = {relation_1}').replace(
            '[', '{').replace(']', '}')
    if question_type == 1:
        answer = True
        rand_set = [1, 3, 9]
        relations = binary_relations(rand_set)
        relation_1 = relations[random.randint(1, len(relations) - 1)]
        closure_relation = transitive_closure_function(relation_1, rand_set)
        question = (
            f'Is {closure_relation} the transitive closure of relation R on set A? A = {rand_set}, R = {relation_1}').replace(
            '[', '{').replace(']', '}')

    print(question)
    return answer
