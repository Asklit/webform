from flask import Flask, render_template
from data.users import User
from data import db_session
from forms.Feedback import FeedbackForm

LANGUAGES = ['russian', "english", 'spanish', 'chinese']
id_language = 0

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hse_secret_key'


@app.route('/', methods=["GET", "POST"])
def main():
    form = FeedbackForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = User(
            name=form.name.data,
            feedback=form.feedback.data,
            email=form.email.data,
        )
        db_sess.add(user)
        db_sess.commit()
    title = ['Отправьте нам сообщение', 'Send us a feedback', 'Envíenos un mensaje', '给我们留言']
    return render_template('base.html', form=form, title=title[id_language], )


if __name__ == '__main__':
    db_session.global_init("db/users_feedback.db")
    app.run(port=8080, host='127.0.0.1', debug=True)
