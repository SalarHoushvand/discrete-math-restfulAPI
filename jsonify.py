# -----------------------------------------------------------
# Functions to generate JSON files in a desired format
# from the functions inside functions.py
# -----------------------------------------------------------


def question_json_maker(question, answer, answer_index=1):
    """
    Generates JSON file for each question.
    :param question: input question.(str)
    :param answer: output answer(str or int)
    :param answer_index: index of the correct answer(int)
    :return: a question.(JSON)
    """
    questions_template = {
        "question": question,
        "questionType": "text",
        "answerSelectionType": "single",
        "answers": answer,
        "correctAnswer": answer_index,
        "messageForCorrectAnswer": "Correct Answer",
        "messageForIncorrectAnswer": "Incorrect Answer",
        "explanation": "",
        "point": "10"
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
