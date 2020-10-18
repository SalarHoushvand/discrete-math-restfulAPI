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
GET /set-union/5/11
```

Here is the list of all available topics:

| Call     | Output                                                                                                                                                                                                                                                                                                      |
| :-------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ```GET /set-union```     | two random sets and union of them as answer.                                                                                                                                                                                                                                                             |
| ```GET /set-intersection```  | two random sets and intersection of them as answer.                                                                                                                                                                                                                                                                                     |
| ```GET /set-difference```     | two random sets and difference of them as answer.                                                                                                                                                                                                                                                   |
| ```GET /set-symmetric-difference```      | two random sets and symmetric difference of them as answer.                                                                                                                                                                                                                                                                    |
| ```GET /cartesian-product``` | two sets and cartesian product of them as answer.                                                                                                                                                                                                                                            |
| ```GET /set-partition``` | one set and all subsets of it as answer.                                                                                                                                                                                                                                           |
| ```GET /set-complement```      | one set and complment of it as answer.

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
| ```GET /function-definition```    | Random question for function definition..                                                                                                                                                                                                         |
|  ```GET /floor-function```    | Random question for floor function.                                                                                                                                                                                                                                                                                     |
|  ```GET /ceiling-function```    | Random question for ceiling function.                                                                                                                                                                                                                                                                                     |
| ```GET  /inverse-function```|Random question for inverse of a function.                                                                                                                                                                                           |
| ```GET  /function-domain```| Random question for domain of a function.                                                                                                                                                                                                                       |
| ```GET  /function-target```| Random question for target of a function.                                                                                                                                                                                                            |



### Probabilities

You can generate random questions for different topics in probabilities section by following calls. you can define number of output questions by giving the value for num.

| Call| Question Topic                                                                                                                                                                                                                                                                                                     |
| :--- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ```GET /event-probability```    | Probability of an event |
|  ```GET /permutation```    | Permutation  |
| ```GET /multiplication-rule```|Multiplication Rule|
| ```GET /combination```| Combination|
| ```GET /conditional-probability```| Conditional Probability |
| ```GET /probability-union```| Probability Union|
| ```GET /probability-complement```| Probability Complement |
| ```GET /bayes-theorem```| Bayes Theorem |



### Relations

You can generate random questions for different topics in relations section by following calls. you can define number of output questions by giving the value for num. Questions for relations are true or false questions.

| Call| Question Topic                                                                                                                                                                                                                                                                                                     |
| :--- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ```GET /reflexive-relation```    | Reflexive Relation |
|  ```GET /irreflexive-relation```    | Irreflexive Relation  |
| ```GET /symmetric-relation	```|Symmetric Relation|
| ```GET /asymmetric-relation	```| Asymmetric Relation|
| ```GET /antisymmetric-relation```| Antisymmetric Relation |
| ```GET /transitive-relation```| Transitive Relation|
| ```GET /reflexive-closure	```| Reflexive Closure |
| ```GET /symmetric-closure```| Symmetric Closure |
| ```GET /transitive-closure```| Transitive Closure |
