import random
from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def home():
    while True:
        num1 = random.randint(1000, 9999)
        num2 = random.randint(1000, 9999)
        result = num1 - num2
        if result < 0:
            continue
        else:
            operator = random.choice(['+', '-'])
            equation = f"{num1} {operator} {num2}"
            return render_template('main.html', equation=equation)
            break

@app.route('/check', methods=['POST'])
def check():
    try:
        user_answer = request.form['answer']
        equation = request.form['equation']

        num1, operator, num2 = request.form['equation'].split()
        num1 = int(num1)
        num2 = int(num2)
        if operator == '+':
            correct_answer = num1 + num2
        elif operator == '-':
            correct_answer = num1 - num2

        if int(user_answer) == correct_answer:
            result = "정답입니다!"
        else:
            result = "오답입니다!"
            return render_template('index.html', equation=equation, result=result)

        return render_template('result.html', result=result)
    except:
        user_answer = request.form['answer']
        equation = request.form['equation']
        return render_template('main.html', equation=equation)

if __name__ == '__main__':
    app.debug = True
    app.run()