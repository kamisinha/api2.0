from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    try:
        inp = request.form['text']
        x, y, z = inp.split()
        x = float(x)
        z = float(z)
        if y=='+':
            add = (x+z)
            add = str(add)
            return "O resultado é "+add
        elif y=='-':
            sub = (x-z)
            sub = str(sub)
            return "O resultado é "+sub
        elif y=='*':
            mul = (x*z)
            mul = str(mul)
            return "O resultado é "+mul
        elif y=='/':
            div = (x/z)
            div = str(div)
            return "O resultado é "+div
    except:
        return ("Algo deu errado, confira se o valor digitado é válido")
if __name__ == "__main__":
    app.run(debug=True)
