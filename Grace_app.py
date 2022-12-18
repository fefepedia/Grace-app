
from flask import Flask, render_template
import json

@app.route('/dashboard')
def dashboard():
  return render_template('dashboard.html', first_number=first_number, second_number=second_number)

with open('data.json') as f:
    data = json.load(f)

first_number = data['first_number']
second_number = data['second_number']
text_content = data['text_content']
