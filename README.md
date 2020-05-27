# Flask Card

[![Python 3.7](https://img.shields.io/badge/python-3.7-blue)](https://www.python.org)

**Flask Card** is a personal project for my own good. I made it as a way to memorize critical Computer Science concepts. The app supports markdown and has a testing mode to keep track of number of right/wrong questions from last test.

## Usage

- Create an account and log in to dashboard.
- Create/Update and Delete different flashcard collections in dashboard.
- Flashcard has corresponding category. Delete category delete all collections under it.
- Each collection has a dashboard of flashcards for CRUD operation on them.
- Each flashcard can be either text or markdown.
- A preview mode that checks user's understanding and memorization on the subject.
- Profile page is used for account related functionalities.

## Getting started

1. Ensure [Docker](https://www.docker.com) is installed and running

2. Install [Poetry](https://github.com/python-poetry/poetry)
```
pip install poetry
```

3. Create an .env file in project in the format
```
SECRET_KEY=${your private key}
FLASK_APP=wsgi.py
FLASK_ENV=development
FLASK_RUN_PORT=8000
FLASK_RUN_HOST=0.0.0.0
SQLALCHEMY_DATABASE_URI=postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@postgres:5432/${POSTGRES_DB}
SQLALCHEMY_TRACK_MODIFICATIONS=0
```

4. Run the project
```
./scripts/dev.sh
```
The application will be running at http://locahost:8000

## DB Migration
Update the database host environment variables file in the database URI section to:
```
SQLALCHEMY_DATABASE_URI=postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@localhost:5432/${POSTGRES_DB}
```

Run Flask migration command:
```
poetry run flask db migrate -m "${YOUR COMMENT}"
poetry run flask db upgrade
```

Change the database host back to:
```
SQLALCHEMY_DATABASE_URI=postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@postgres:5432/${POSTGRES_DB}
```

Run the `./script/dev.sh` file in terminal to start server again.

## Built with

- **Language**: Python
- **Framework**: Flask
- **Template Engine**: Jinja
- **Styling Framework**: Bulma CSS
- **Database**: postgresql

## Credits to

- [Markdown It](https://github.com/markdown-it/markdown-it): Use for displaying code snippet on flashcard

## Screenshots

![Login Page](./screenshots/login.png)

![Dashboard](./screenshots/dashboard.png)

![Preview Flashcards](./screenshots/preview-mode.png)

## License

Under MIT License.
