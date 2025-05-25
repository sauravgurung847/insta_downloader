from flask import Flask, render_template, request, send_from_directory, redirect, url_for
from downloader import download_post
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    url = request.form['url']

    # Clear previous downloads
    folder = 'downloads'
    if os.path.exists(folder):
        for f in os.listdir(folder):
            os.remove(os.path.join(folder, f))
    else:
        os.makedirs(folder)

    success, message = download_post(url)

    if success:
        return redirect(url_for('media'))
    else:
        return f"Download failed: {message}", 400

@app.route('/media')
def media():
    folder = 'downloads'
    valid_extensions = ('.jpg', '.jpeg', '.png', '.mp4')
    media_files = [f for f in os.listdir(folder) if f.endswith(valid_extensions)]

    return render_template('media.html', files=media_files)

@app.route('/download_file/<filename>')
def download_file(filename):
    return send_from_directory('downloads', filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
