
from flask import Flask, redirect, url_for, render_template, flash

app = Flask(__name__)

programming_langue = ['HTML','CSS','JAVASCRIPT','PYTHON','SQL','FIGMA']
@app.route('/home')
def home():
        return render_template('index.html', context = programming_langue)
@app.route('/skill')
def skill():
        return render_template('skill.html')

if __name__ == '__main__':
    app.run(debug=True)
