import os
import re

from flask import Flask, flash, render_template, request

app = Flask(__name__)
app.secret_key = os.urandom(24)

ALLOWED_EXTENSIONS = {'md'}


def is_allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def clean_text(text: str):
    cleaned_text = re.sub(r'[\n\r]+', '\n', text)
    return cleaned_text



@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return render_template('index.html')

        file = request.files['file']

        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return render_template('index.html')

        if not is_allowed_file(file.filename):
            flash('File type not allowed')
            return render_template('index.html')

        try:
            document = file.read().decode('utf-8')
        except Exception as e:
            flash(f'Error reading file: {e}')
            return render_template('index.html')

        if not document.strip():
            flash('File is empty')
            return render_template('index.html')

        document = clean_text(document)
        flash('Document cleaned successfully!')
        return render_template('index.html', document=document)

    return render_template('index.html')


if __name__ == '__main__':
    app.run()
