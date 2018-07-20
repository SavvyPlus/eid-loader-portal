from wtforms import Form, BooleanField, StringField, SelectField, FileField, validators
from commons import helpers

class UploadForm(Form):
    file = FileField("CSV File")
    eid_format = SelectField(
        'EID Format',
        choices=helpers.get_inv_input_folders()
    )
