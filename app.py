import json

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/home')
def home():
        with open('skills.json', 'r') as f:
            my_data = json.load(f)

        skills = my_data['skills']
        return render_template('index.html', skills = skills)
@app.route('/skill')
def skill():
        return render_template('skill.html')

if __name__ == '__main__':
    app.run(debug=True)
