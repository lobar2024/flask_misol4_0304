from flask import Flask, render_template

app = Flask(__name__)

@app.route('/classify')
def classify_page():
    numbers = [0, -5, 42, -1, 7, 0, -99, 3]
    return render_template('classify.html', numbers=numbers)

if __name__ == '__main__':
    app.run(debug=True)
