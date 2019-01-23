# Questioner 

#### challenge 2 : API

#### Project Overview
This is a platform that allows organizers to plan meetups and to prioritize which questions will be answered depending on the questions with more votes. 


#### Tools used in this API includes:-
- Flask
- Git Version Control
- Pytest
- Postman
- Git


#### Installation
- cloning the Repository $ git clone https://github.com/exdus/Questioner
- checkout develop branch
- create a virtual environment
	• virtualenv env
    • source venv/bin/activate

- python run.py
- Test the api using postman

#### Endpoints
Method        | EndPoint         | Goal |
------------- | -----------------| ---------------
POST          | /api/v1/meetups  | Post a new meetup record   |
GET           | /api/v1/meetups/<int:meetup_id>  | Get a specific meetup   |
GET           | /api/v1/meetups/upcoming   | Get all upcoming meetup records   |
POST          | /api/v1/meetup/<int:meetup_id>/question | Create a question for a specific meetup.   |
PUT           | /api/v1/questions/<int:question_id>/upvote | Adds votes by one |
PUT           | /api/v1/questions/<int:question_id>/downvote | Decreases votes by one  |
POST          | /api/v1/meetups/<int:meetup_id>/rsvps | Create a meetup RSVP


#### Recognitions
- Tonui Benson
- #nbo-36 cycle
- Andela Community

#### Author
Kelvin Bunei
