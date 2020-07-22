
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
  "quizSynopsis": f"Test Quiz for {topic}",
  "questions": questions_list }

  return title













