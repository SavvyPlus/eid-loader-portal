from flask import redirect, request, Blueprint, render_template, url_for, flash, current_app as app
from werkzeug.utils import secure_filename

import config
from transporter import s3_process
from . import forms


aws = Blueprint('aws', __name__, template_folder='templates')



@aws.route("", methods=["GET", "POST"])
def index():
    form = forms.UploadForm()

    if request.method == 'POST':
        # print (app.config["PREFIX_INV_IN_FOLDER"])
        file = request.files['file']
        file_name = secure_filename(file.filename)
        eid_format = request.form['eid_format']
        key = config.INV_UPLOAD_FOLDER + eid_format + file_name
        s3_process.put_file(config.INV_BUCKET, key, file)
        flash("Your request is submitted")
        return redirect(url_for('aws.index'))

    return render_template('aws/index.html', form=form)
