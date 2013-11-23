from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analytics')
def analytics():
    return render_template('analytics.html')

@app.route('/test', methods = ['POST'])
def test():
    print request.form['dropdown']
    return "passed"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
