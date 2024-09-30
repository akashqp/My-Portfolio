from flask import Flask, render_template
import logging

app = Flask(__name__)

logging.basicConfig(filename='app.log', level=logging.INFO)

@app.route('/')
def home():
    logging.info('Home page accessed')
    return render_template('index.html')

# @app.route('/about')
# def about():
#     return render_template('about.html')

if __name__ == '__main__':
    # app.run(host='0.0.0.0')
    app.run(debug=True)