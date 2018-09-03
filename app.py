from flask import Flask, request

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!doctype html>
<html>
    <body>
        <form action="/hello">
            <label>Name
                <input type="text" name="customer_name" />
            </label>
            <br>
            <label>Small 
                <input type="radio" name="coffee-size" value="sm" />
            </label>
            <label>Medium
                <input type="radio" name="coffee-size" value="med" />
            </label>
            <label>Large
                <input type="radio" name="coffee-size" value="lg" />
                <input type="submit" />
            </label>
        </form>
    </body>
</html>

"""

@app.route("/")
def index_handler():
    return form

@app.route("/hello")
def hello():
    coffee_size = request.args.get('coffee-size')
    name = request.args.get('customer_name')
    if coffee_size == 'sm':
        return '<h1>' + name + ' ordered a small</h1>'
    elif coffee_size == 'med':
        return '<h1>' + name + ' ordered a medium</h1>'
    elif coffee_size == 'lg':
        return  '<h1>' + name + ' ordered a venti</h1>'
    else:
        return '<h1>' + name + ' didnt order a coffee</h1>'
app.run()