from flask import Flask, request, render_template, jsonify

app = Flask(__name__)


@app.route('/')
def index() :
    return render_template('index.html')


@app.route('/math', methods=['POST'])
def calculate() :
    if request.method == 'POST' :
        oparation = request.form['oparation'].lower()
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        res = num1

        if oparation == 'add' :
            res += num2
        
        elif oparation == 'sub' :
            res -= num2
        
        elif oparation == 'mul' :
            res *= num2
        
        elif oparation == 'div' :
            res /= num2
    
        return render_template('results.html', result=res)
    return {'msg' : "dunno"}


if __name__ == '__main__' :
    app.run(host='localhost', port='8000')