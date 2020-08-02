# discrete-math-restfulAPI

This is an API made by python using flask to generate unlimited questions for different discrete mathematic topics.

## Servers

| Name            | URL                 | Description                                                                                                   |
| :-------------- | :------------------ | :------------------------------------------------------------------------------------------------------------ |
| Staging     | https://mathgen-api.herokuapp.com/ | Synced with the master branch of this repository                |

## API Methods

### Get random quizz
By this call you can get as many questions as you requested for set theories randomly.

```HTTP
GET /random/int:num
```

**Response**

```{
"questions": [
{
"answerSelectionType": "single",
"answers": [
list
],
"correctAnswer": int,
"explanation": "",
"messageForCorrectAnswer": "CORRECT ANSWER",
"messageForIncorrectAnswer": "INCORRECT ANSWER",
"point": "10",
"question":str,
"questionType": "text"
}
],
"quizSynopsis":str,
"quizTitle":str
}
```

### Questions from topics

By calling this you need to first define the topic, then number of questions you want and finally type of items in each sets.
as an example to call 5 questions from union of sets that both sets are containing integers:

```HTTP
GET /union/5/11
```

Here is the list of all available topics:

| param     | Output                                                                                                                                                                                                                                                                                                      |
| :-------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| union    | two random sets and union of them as answer.                                                                                                                                                                                                                                                             |
| intersection  | two random sets and intersection of them as answer.                                                                                                                                                                                                                                                                                     |
| difference     | two random sets and difference of them as answer.                                                                                                                                                                                                                                                   |
| symmetric_difference      | two random sets and symmetric difference of them as answer.                                                                                                                                                                                                                                                                    |
| cartesian | two sets and cartesian product of them as answer.                                                                                                                                                                                                                                            |
| partition | one set and all subsets of it as answer.                                                                                                                                                                                                                                           |
| complement      | one set and complment of it as answer.

The first number defines the elements in first set and second number defines elements in second, here is the list of all available elements:
| param| Set Items                                                                                                                                                                                                                                                                                                      |
| :--- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1    | integer                                                                                                                                                                                                                                                            |
| 2    | float                                                                                                                                                                                                                                                                                     |
| 3    | character                                                                                                                                                                                                                                                  |
| 4    | country name                                                                                                                                                                                                                                                                    |
| 5    | city name                                                                                                                                                                                                                                            |
| 6    | male name                                                                                                                                                                                                                                           |
| 7    | female name


### Functions

You can generate random questions for different topics in function section by following calls. you can define number of output questions by giving the value for num.

| Call| Question Topic                                                                                                                                                                                                                                                                                                     |
| :--- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ```GET /function/int:num```    | Whether it's a function or not if yes what kind of function.                                                                                                                                                                                                         |
|  ```GET /function/floorceiling/int:num```    | Random questions for floor and ceiling function.                                                                                                                                                                                                                                                                                     |
| ```GET  /function/inverse/int:num```|Random question for inverse of a function.                                                                                                                                                                                           |
| ```GET  /function/domain/int:num```| Random question for domain of a function.                                                                                                                                                                                                                       |
| ```GET  /function/target/int:num```| Random question for target of a function.                                                                                                                                                                                                            |
