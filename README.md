Hi,

To run the project you will need Docker. Docker will take care of all
dependencies by creating a lightweight virtual machine to run the solution.
Commands to run the project:

Build the project with "docker build ." and "docker-compose build"

Run the test with (docker-compose run app sh -c "python manage.py test && flake8")

Run the project "docker-compose up"

Use the following links/path to validate the API:
- http://localhost:1337/linkshorteners/
to present the link shortener and to post full_link to create a new short link

- http://localhost:1337/linkshorteners/1/
to present a specific shorter link and can provide any id

- http://localhost:1337/linkshorteners/?full_link=https://www.google.com/
to present the shorter link base on a query param provided

- http://localhost:1337/xEJgUPy
to redirect to the original website (
  http://localhost:1337/ - localhost
  xEJgUPy - hash
  )

To build the API, I used Django Rest Framework, Docker, and PostgreSQL.
PostgreSQL is the most faster open-source database available to
read and write data.
Django Rest Framework is the most popular API builder for python programming
language and it provide great features do build rapidly e secure.
Docker is a lightweight virtual machine to containerize all our dependencies.

(Nice to have)
Redis is a platform that allows caching data to reduce the database hit.


Looking forward to hearing from you.

Kind regards,
Bruno Barros
