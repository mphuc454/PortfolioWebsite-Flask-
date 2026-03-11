import json
import re
import smtplib
from email.mime.text import MIMEText
from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

# load skill từ file json
def load_skills():
    with open('PythonPortfolio\\skills.json', 'r', encoding='utf-8') as f:
        my_data = json.load(f)
    return my_data['skills']


# xử lý send email
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
def home():
        skills = load_skills()
        error = None
        if request.method == 'POST':
            name = request.form['usrname']
            email = request.form['usremail']
            message = request.form['mess']
            
            #kiểm tra tính hợp lệ form:
            if(len(name.strip()) < 2): 
                 error = "Tên phải lớn hơn hoặc bằng 2 ký tự"
            elif len(message) < 10:
                error = 'Vui lòng nhập lời nhắn ít nhất 10 từ'
            else:
                send_mail(email, message)
                return redirect(url_for('home'))
                
        return render_template('index.html', skills = skills, err = error)


if __name__ == '__main__':
    app.run(debug=True)
