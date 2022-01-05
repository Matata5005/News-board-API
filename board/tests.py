from django.test import TestCase


# Create your tests here.
"""
### News-board-API
CRUD API that shows the list of news with functionality to upvote and comment.
Also shows details like creation date, amount of upvotes, title and author-name

### Set up with Docker
1. clone this repository 
2. Go into the project folder
3. Build the Image and run the container using Docker

```bash
$ git clone https://github.com/Matata5005/News-board-API
$ cd into News-board-API
$ docker-compose up --build 
$ docker-compose run web python3 manage.py migrate

### Go to postman and test the news board API by making endpoints requests



### Set up without Docker
1. clone this repository 
2. Go into the project folder
3. Activate the virtual environment and environment variables. Check the local.env file for all details
4. Configure your database and specify the values in .env file
5. Run RabbitMQ server locally or use:(https://hub.docker.com/_/rabbitmq))
6. Install dependencies in the requirments.txt file
5. Run app

```bash
$ git clone https://github.com/Matata5005/News-board-API
$ cd News-board-API
$ python3 -m venv <name_of_your_virtual_environment> eg: $python3 -m venv venv
$ pip install -r requirments.txt
$ python manage.py runserver

### Production
Import this public collection link https://www.getpostman.com/collections/035a692b97fbd7eb7bf5 on postman to view the APIs
set Variables:
- PROD: 'https://newz-board.herokuapp.com/`
- LOCAL: 'http://127.0.0.1:8000'
- name: `<Your username>`
- email: `<Your email address>`
- password: `<Your password>`

...and voila start your signup into the API , then sign in(using the sign in endpoint).
__`N|B`__:- Once your signed in, the token will be saved into a `cookie` and therefore you can successfully make requests to the endpoints as an `authenticated user` .If `cookie` is not available(Not signed in, requests to other endpoints will fail)

### API Docs
- Find the url for the published API doc  

### Developer
For inquiries:daviemata111@gmail.com

"""
