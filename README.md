# Questioner 

#### challenge 2 : API

#### Project Overview
This is a platform that allows organizers to plan meetups and to prioritize which questions will be answered depending on the questions with more votes. 


#### Deployment


#### Tools used in this API includes:-
- python 2.7
- Git
- Postman



#### Installation
- clone the repo $ git clone https://github.com/exdus/Questioner-api
- checkout develop branch
- create a virtual environment
	• virtualenv env
    • source venv/bin/activate
- install dependencies
    . pip install -r requirements.txt

- python run.py
- Test the api using postman

#### Endpoints
Method        | EndPoint         | Goal |
------------- | -----------------| ---------------
POST          | /api/v1/register |  register on the app
POST          | /api/v1/login     |  log into the app
POST          | /api/v1/logout  |  log out the app
POST          | /api/v1/meetups  | Post a new meetup record   |
GET           | /api/v1/meetups/<int:meetup_id>  | Get a specific meetup   |
GET           | /api/v1/meetups/upcoming   | Get all upcoming meetup records   |
POST          | /api/v1/meetup/<int:meetup_id>/question | Create a question for a specific meetup.   |
PUT           | /api/v1/questions/<int:question_id>/upvote | Adds votes by one |
PUT           | /api/v1/questions/<int:question_id>/downvote | Decreases votes by one  |
POST          | /api/v1/meetups/<int:meetup_id>/rsvps | Create a meetup RSVP
POST          | /api/v1/questions/<int:question_id/comments  | comment on a question
GET           | /api/v1/questions/<int:question_id>/comments | get all comments

#### Recognitions
- Tonui Benson
- #nbo-36 cycle
- Andela Community

#### Author
Kelvin Bunei
