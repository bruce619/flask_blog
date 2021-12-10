from os import environ
from learningflask import create_app

app = create_app(environ.get('FLASK_CONFIG'))


# >>> from your app import db, create_app
# >>> db.create_all(app=create_app('development'))

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')


