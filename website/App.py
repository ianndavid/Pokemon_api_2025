# Running the main app

from flask import Flask
from Init import start_app

app = start_app()

from Oth import Oth

app.register_blueprint(Oth)

if __name__ == '__main__':
    app.run(debug=True)