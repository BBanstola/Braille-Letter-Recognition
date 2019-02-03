import os
from os.path import join, dirname, realpath

from adapt import apply_threshold
from flask import Flask,render_template,request, flash,redirect
from identification import identify
from werkzeug.utils import secure_filename

app = Flask(__name__)

app = Flask(__name__,static_url_path = "", static_folder = "templates/mulsegimages")

UPLOAD_FOLDER = join(dirname(realpath(__file__)),'templates/images')
UPLOAD_FOLDERC = join(dirname(realpath(__file__)),'templates/mulsegimages')
ALLOWED_EXTENSIONS = set(['png', 'jpg','bmp','gif'])

@app.route('/', methods=['GET','POST'])
def index():
    if request.method =='POST':
        print("Post method")

        if 'file' not in request.files:
            print("No file")
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']

        if file.filename == '':
            print("No file is selected")
            flash('No file is selected')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            print(os.path.join(app.config['UPLOAD_FOLDER']))
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            # print(os.path.join(app.config['UPLOAD_FOLDERC']))
            # file.save(os.path.join(app.config['UPLOAD_FOLDERC'], filename))

            print(filename + " is saved and done !!")
            apply_threshold(filename)
            dig_string = identify()
            print(dig_string)
            return render_template('home.html', strings = dig_string, img = file.filename)

    return  render_template('home.html')


# @app.route('/')
# def index():
#     return render_template('home.html')

@app.route('/display')
def display():
    return render_template('display.html', img={'image0.png', 'image1.png', 'image2.png', 'image3.png', 'image4.png'})

@app.route('/about')
def about() :
    return render_template('about.html')

@app.route('/braille')
def braille() :
    return render_template('braille.html')

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.run(debug=True)
