# Keep web handlers in its own arena.
from flask import Response, stream_with_context, Blueprint, render_template, request, session
from werkzeug.utils import secure_filename

import time
import subprocess
import os

stream_urls = Blueprint('url', __name__, static_folder="static", template_folder='templates')


@stream_urls.route('/stream/<int:num>')  # return a streaming
def root(num):

    def f(n):
        for i in range(n):
            time.sleep(.5)
            yield 'i={}<br>'.format(i+1)

    return Response(stream_with_context(f(num)))


@stream_urls.route('/ping/<string:site>')
def ping(site):
    def run(s):
        process = subprocess.Popen(['ping', s], stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE, universal_newlines=True)
        while True:
            output = process.stdout.readline()
            yield output.strip() + '<br/>'
            # Do something else
            return_code = process.poll()
            if return_code is not None:
                yield f'RETURN CODE: {return_code}'
                # Process has finished, read rest of the output
                for output in process.stdout.readlines():
                    yield output.strip() + '<br/>'
                break

    return Response(stream_with_context(run(site)))


# file upload
@stream_urls.route('/upload', methods=['GET', 'POST'])
def file_upload():
    if request.method == 'GET':
        return render_template('file_upload.html')
    else:  # guaranty POST by decorator
        uf = request.files['file_name']
        sf = os.path.join('/tmp', secure_filename(uf.filename))
        uf.save(sf)
        return 'file uploaded!'


# session
@stream_urls.route('/session_set')
def session_set():
    session['key'] = 'value'
    return 'ok'


@stream_urls.route('/session_get')
def session_get():
    return session.get('key', 'not set')
