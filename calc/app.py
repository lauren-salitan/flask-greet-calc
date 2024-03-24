from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

operations = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div
}

@app.route('/math/<operation>')
def do_math(operation):
    """Perform a math operation on a and b."""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    if operation in operations:
        result = operations[operation](a, b)
        return str(result)
    else:
        return "Invalid operation", 404

@app.route('/add')
def do_add():
    """Add a and b."""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = add(a, b)
    return str(result)

@app.route('/sub')
def do_sub():
    """Subtract b from a."""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = sub(a, b)
    return str(result)

@app.route('/mult')
def do_mult():
    """Multiply a and b."""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = mult(a, b)
    return str(result)

@app.route('/div')
def do_div():
    """Divide a by b."""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = div(a, b)
    return str(result)

if __name__ == "__main__":
    app.run(debug=True)
