

template = {
  "quizTitle": "sets",
  "quizSynopsis": "Test Quiz for ",
  "questions": [
    {
      "question": "What is a set?",
      "questionType": "text",
      "answerSelectionType": "single",
      "answers": [
        "A set is an unordered collection of different elements.",
        "",
        "",
        ""
      ],
      "correctAnswer": "1",
      "messageForCorrectAnswer": "CORRECT ANSWER",
      "messageForIncorrectAnswer": "INCORRECT ANSWER",
      "explanation": "",
      "point": "10"
    }]}

def json_maker(question, answer):

  questions_template = {
      "question": question,
      "questionType": "text",
      "answerSelectionType": "single",
      "answers": [
        answer,
        "",
        "",
        ""
      ],
      "correctAnswer": "1",
      "messageForCorrectAnswer": "CORRECT ANSWER",
      "messageForIncorrectAnswer": "INCORRECT ANSWER",
      "explanation": "",
      "point": "10"
    }


  return questions_template

def title_maker(topic='', questions_list=[]):
  title = {
  "quizTitle": topic,
  "quizSynopsis": "Test Quiz for ",
  "questions": questions_list }

  return title


print(title_maker('union', ['hello','salar']))










