import json
import smtplib
from email.mime.text import MIMEText
from flask import Flask, render_template, request

app = Flask(__name__)

def load_skills():
    with open('skills.json', 'r', encoding='utf-8') as f:
        my_data = json.load(f)
    return my_data['skills']

@app.route('/home')
def home():
        skills = load_skills()
        return render_template('index.html', skills = skills)
@app.route('/skill')
def skill():
        return render_template('skill.html')

# send email
def send_mail(from_email, message):
    SMTP_SERVER = "smtp.gmail.com"
    SMTP_PORT = 587
    USERNAME = "22130215@st.hcmuaf.edu.vn"
    PASSWORD = 'wvvt rmmk wyqz hvbr'

    body = f"From email: {from_email} \n with Message: {message}"

    msg = MIMEText(body)
    msg['Subject'] = f'Send from {from_email}'
    msg['From'] = from_email
    msg['To'] = "22130215@st.hcmuaf.edu.vn"
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(USERNAME, PASSWORD)
        server.sendmail(from_email, "22130215@st.hcmuaf.edu.vn", msg.as_string())
@app.route('/home', methods = ['GET', 'POST'])
def contact_form():
    skills = load_skills()
    if request.method == 'POST':
        email = request.form['usremail']
        message = request.form['mess']

        send_mail(email, message)
    return render_template("index.html", skills = skills)

if __name__ == '__main__':
    app.run(debug=True)
