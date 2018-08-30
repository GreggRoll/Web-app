from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index_handler():
    return 'this is my fucking webpage bitch'

app.run()