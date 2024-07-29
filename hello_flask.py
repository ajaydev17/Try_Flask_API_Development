# importing flask framework
from flask import Flask

# creating a flask application
app = Flask(__name__)


# defining routes
@app.route('/')
def hello_from_flask():
    return "Hello from flask"
