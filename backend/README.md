# Lodgify Backend

This is the backend for the Lodgify project, built with Flask-Resful API, Blueprints, Swagger (API documentation), and uses both Postgres and MongoDB databases.

## Environment Variables

To use this project, duplicate the `example.env` file and rename it to `.env.` This will create the necessary environment variables for the project.

## Installation

1. Create a virtual environment by running:

```Copy code
python -m venv env
```

2. Activate the virtual environment:

For Windows:

```Copy code
env\Scripts\activate 
```

For Mac:

```Copy code
source env/bin/activate
```

3. Install the dependencies using pipenv:

```Copy code
pipenv install
```

Update the database tables for Postgres:

```Copy code
flask db upgrade
```

## Running the app

To run the app, execute the following commands:

For Windows:

```Copy code
export FLASK_APP=server.py
export FLASK_DEBUG=True
```

then

```Copy code
python server.py
```

For Mac:

```Copy code
set FLASK_APP=server.py
set FLASK_DEBUG=True
```

then

```Copy code
python server.py
```

## Contributing

Please see the [contributing.md](CONTRIBUTING.md) file for details on how to contribute to this project.

## Contact

For any inquiries or feedback, please contact us at talkto@samdoghor.com.
