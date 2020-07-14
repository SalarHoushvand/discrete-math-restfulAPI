# discrete-math-restfulAPI

This is an API made by python using flask to generate unlimited questions for different discrete mathematic topics.

## Servers

| Name            | URL                 | Description                                                                                                   |
| :-------------- | :------------------ | :------------------------------------------------------------------------------------------------------------ |
| Staging     | https://mathgen-api.herokuapp.com/ | Synced with the master branch of this repository                |

## API Methods

### Get random quizz
This call give you random quizz by choosing 3 questions from each topics.

```HTTP
GET /random
```

**Response**

```ts
question number : string{{
  
  question : string
  
  set1: list
  
  set2: list
  
  answer: string
}}
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


