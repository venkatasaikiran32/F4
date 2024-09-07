from flask import Flask, render_template, request

app = Flask(__name__)

# Route for the form page
@app.route('/')
def form():
    return render_template('form.html')

# Route for handling form submission and displaying result
@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        return render_template('result.html', name=name, age=age)

if __name__ == '__main__':
    app.run(debug=True)
