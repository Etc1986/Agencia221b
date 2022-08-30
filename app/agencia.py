from flask import request, flash, Blueprint, render_template, current_app
import sendgrid
from sendgrid.helpers.mail import Mail, To, Email, Content

bp = Blueprint('agencia', __name__, url_prefix="/")

@bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        phone = request.form.get('phone')
        email = request.form.get('email')
        message = request.form.get('message')
        errors = []
        datos = str([phone ,email , message])

        if not name:
            errors.append('El Nombre es obligatorio')
        if not phone:
            errors.append('El Telefono es obligatorio')
        if not email:
            errors.append('El Correo es obligatorio')
        if not message:
            errors.append('El Mensaje  es obligatorio')


        if len(errors) == 0:
            send(name, datos)
            flash('El Mensaje se ha enviado correctamente','success')
        else:
            for error in errors:
                    flash(error, 'error')
    return render_template('index.html')

def send(subject, body):
    sg = sendgrid.SendGridAPIClient(api_key=current_app.config['SENDGRID_KEY'])
    from_email = Email(current_app.config['FROM_EMAIL'])
    to_email = To('agencia221b.SH@gmail.com')
    content = Content("text/plain", body)
    mail = Mail(from_email, to_email, subject, content)
    response=sg.client.mail.send.post(request_body=mail.get())
    print(response)
