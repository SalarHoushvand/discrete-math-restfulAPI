# -----------------------------------------------------------
# Functions to generate JSON files in a desired format
# from the functions inside functions.py
# -----------------------------------------------------------


def question_json_maker(question_id, question, answer, answer_index=1, question_type='MC', difficulty=1, points=10):
    """
    Generates JSON file for each question.
    :param question: input question.(str)
    :param answer: output answer(str or int)
    :param answer_index: index of the correct answer(int)
    :param question_type: type of question ex: MC (Multiple Choice).(str)
    :param difficulty: difficulty level of the question(1 to 5)(int)
    :param points : points for each right answer. (int)
    :return: a question.(JSON)
    """
    questions_template = {
        "questionID": question_id,
        "question": question,
        "questionType": question_type,
        "answerSelectionType": "single",
        "answers": answer,
        "correctAnswer": answer_index,
        "messageForCorrectAnswer": "Correct Answer",
        "messageForIncorrectAnswer": "Incorrect Answer",
        "difficulty": difficulty,
        "point": points
    }
    return questions_template


def json_maker(topic='', questions_list=[]):
    """
    Gets list of questions, topic and generates final version of JSON.

    :type questions_list: list
    :param topic: topic which question covers.(str)
    :param questions_list: list containing all the questions.(list)
    :return: final version of the question.(JSON)

    """
    question = {
        "quizTitle": topic,
        "quizSynopsis": f"Test Quiz for {topic}",
        "questions": questions_list}

    return question
