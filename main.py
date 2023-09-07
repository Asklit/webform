from flask import Flask, render_template
from werkzeug.utils import redirect

from data.users import User
from data import db_session
from forms.Feedback import FeedbackForm

LANGUAGES = ['russian', "english", 'spanish', 'chinese']
ID_LANGUAGE = 0

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hse_secret_key'


@app.route('/', methods=["GET", "POST"])
def main():
    form = FeedbackForm()
    message = ['', '', '', '']
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = User(
            name=form.name.data,
            feedback=form.feedback.data,
            email=form.email.data,
        )
        db_sess.add(user)
        db_sess.commit()
        message = ["Спасибо вам за ваше сообщение, мы отправим вам ответ на почту",
                   'Thank you for your message, we will send you a reply by email',
                   'Gracias por su mensaje, le enviaremos una respuesta por correo',
                   '感谢您的留言我们将通过电子邮件向您发送回复']
    title = ['Отправьте нам сообщение', 'Send us a feedback', 'Envíenos un mensaje', '给我们留言']
    title2 = ['Отправьте нам сообщение', 'Send us a feedback', 'Envíenos un mensaje', '给我们留言']
    name = ['Имя', 'Name', 'Nombre', '姓名']
    text = ['Напишите нам что нибудь', 'Write us something', 'Escríbenos algo', '给我们写点东西']
    email_form = ['Оставьте нам свой email для обратной связи', 'Leave us your email for feedback',
                  'Déjanos tu correo electrónico para comentarios', '留下您的电子邮件以获取反馈']
    send = ['Отправить', 'Send', 'Enviar', '发送']
    choose = ['Выбор языка', 'Language selection', 'Selección de idioma', '语言选择']
    russian_language = ['Русский', 'Russian', 'Rusa', '俄语']
    english_language = ['Английский', 'English', 'Inglés', '英语']
    spanish_language = ['Испанский', 'Spanish', 'Español', '西班牙语']
    chinese_language = ['Китайский', 'Chinese', 'Chino', '中文']
    made_by = ['Сделано студентами Высшей Школы Экономики', 'Made by students of the Higher School of Economics',
               'Hecho por estudiantes de la escuela Superior de Economía', '由高等经济学院的学生制作']
    return render_template('base.html', form=form, title=title[ID_LANGUAGE], message=message[ID_LANGUAGE], ID_LANGUAGE=ID_LANGUAGE,
                           title2=title2[ID_LANGUAGE], name=name[ID_LANGUAGE], text=text[ID_LANGUAGE],
                           email_form=email_form[ID_LANGUAGE], russian_language=russian_language[ID_LANGUAGE],
                           english_language=english_language[ID_LANGUAGE], spanish_language=spanish_language[ID_LANGUAGE],
                           chinese_language=chinese_language[ID_LANGUAGE], send=send[ID_LANGUAGE], choose=choose[ID_LANGUAGE],
                           made_by=made_by[ID_LANGUAGE])


@app.route('/russian', methods=["GET", "POST"])
def russian():
    global ID_LANGUAGE
    ID_LANGUAGE = 0
    main()
    return redirect("/")


@app.route('/english', methods=["GET", "POST"])
def english():
    global ID_LANGUAGE
    ID_LANGUAGE = 1
    main()
    return redirect("/")


@app.route('/spanish', methods=["GET", "POST"])
def spanish():
    global ID_LANGUAGE
    ID_LANGUAGE = 2
    main()
    return redirect("/")


@app.route('/chinese', methods=["GET", "POST"])
def chinese():
    global ID_LANGUAGE
    ID_LANGUAGE = 3
    main()
    return redirect("/")


if __name__ == '__main__':
    db_session.global_init("db/users_feedback.db")
    app.run(port=8080, host='127.0.0.1', debug=True)
