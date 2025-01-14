import random
from datetime import datetime
from flask import Flask, render_template, request, session


a = datetime.today().strftime("%Y%m%d%H") 
print (a)

app = Flask(__name__)
app.secret_key = a

@app.route('/')
def home():
    operator = random.choice(['+', '-', '×', '÷'])
    
    try:
        correct_count = session['correct_count']
    except:
        correct_count = 0

    if operator == '+':
        num1 = random.randint(1, 1000)
        num2 = random.randint(1, 1000)

    elif operator == '-':
        num1 = random.randint(1, 1000)
        num2 = random.randint(1, num1)

    elif operator == '×':
        num1 = random.randint(1, 99)
        num2 = random.randint(1, 99)

    elif operator == '÷':
        num1 = random.randint(10, 1000)
        num2 = random.randint(1, 10)
        
    sik = f"{num1} {operator} {num2}"

    if operator != "÷":
        return render_template('main.html', sik=sik, correct_count=correct_count)
    else:
        return render_template('divide.html', sik=sik, correct_count=correct_count)

@app.route('/check', methods=['post'])
def check():
    try:
        typed_answer = request.form['answer']
        sik = request.form['sik']

        num1, operator, num2 = request.form['sik'].split()
        num1 = int(num1)
        num2 = int(num2)
        if operator == '+':
            result = num1 + num2

        elif operator == '-':
            result = num1 - num2

        elif operator == '×':
            result = num1 * num2

        elif operator == '÷':
            typed_answer_2 = request.form['answer2']
            result = num1 // num2
            result2 = num1 % num2

        if operator != "÷":
            if int(typed_answer) == result:
                result = "정답입니다!"
                session['correct_count'] = session.get('correct_count', 0) + 1

                correct_count = session['correct_count']

                print (session['correct_count'])
                return render_template('result.html', result=result, correct_count=correct_count)

            else:
                return render_template('index.html', sik=sik, result=result)
            
        else:
            if int(typed_answer) == result:
                if int(typed_answer_2) == result2:
                    result = "정답입니다!"
                    session['correct_count'] = session.get('correct_count', 0) + 1

                    correct_count = session['correct_count']

                    print (session['correct_count'])
                    return render_template('result.html', result=result, correct_count=correct_count)
                
                else:
                    return render_template('divide_fail.html', sik=sik, result=result)
                
            else:
                return render_template('divide_fail.html', sik=sik, result=result)            

    except Exception as e:
        typed_answer = request.form['answer']
        sik = request.form['sik']
        print (e)

        num1, operator, num2 = request.form['sik'].split()

        if operator != "÷":
            return render_template('index.html', sik=sik)
        else:
            return render_template('divide.html', sik=sik)
        
if __name__ == '__main__':
    app.debug = True
    app.run()
