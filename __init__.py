from flask import Flask,render_template,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
import stripe


from werkzeug.urls import unquote
from flask_mail import Mail , Message
db = SQLAlchemy()
DB_NAME = "database.db"
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'jhfksjdfhlsyrehfsdkvbhfv'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['STRIPE_PUBLIC_KEY'] = 'pk_test_51O03ftSAm1yXJy6FXwURoEWIig94zvLUQG2UEmLhq9UogQ9ipcKJcjlaBVb7sJSeoRBn5Dg7Ghnu8zBEqwdG3IEt0017SqYlZK'
    app.config['STRIPE_SECRET_KEY'] = 'sk_test_51O03ftSAm1yXJy6FFTY1YNXbl9TgOODLKucdxhYRG4ysk7TTb6xHZM84eLIR8j1NU6BT7dPdcMPTTQbej37E9zn600ewdNWKpp'
    app.config['MAIL_SERVER']='smtp@gmail.com'
    app.config['MAIL_PORT']=465
    app.config['MAIL_USERNAME']='bhagyabeeb@gmail.com'
    app.config['PASSWORD'] = 'DulalNilima@123'
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL']= True
    mail = Mail(app)


    stripe.api_key =  app.config['STRIPE_SECRET_KEY']

    db.init_app(app)



    from musicista.views import views
    from musicista.auth import auth


    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')

    from .models import User, Book
    @app.route('/thanks', methods=['GET', 'POST'])
    def thanks():
        if request.method == 'POST':
            msg = Message("Hey how are you ", sender='noreply@demo.com', recipients=['bhagyabeeb@gmail.com'])
            msg.body = "yo yo"
            mail.send(msg)
            return "sent email"
        return render_template('thanks.html')

    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    return app

def create_database(app):
    if not path.exists('musicista/' + DB_NAME):
        db.create_all(app)
        print('Created Database!')