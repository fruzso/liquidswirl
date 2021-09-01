from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')

@app.route('/animation_squid', methods=['POST', 'GET'])
def animation_squid():
    return render_template('animation_squid.html')

if __name__ == '__main__':
    app.run(debug=True)