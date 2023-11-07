from flask import Blueprint , render_template,url_for , request
from flask_login import login_required,current_user
import  stripe
from flask_mail import Mail , Message



from flask import request,jsonify
from .chat import get_response
views = Blueprint('views',__name__)


@views.route('/')
@login_required
def home():
    return render_template('login.html',user=current_user)

@views.route('/landing',methods =['GET'])
def landing():
    return render_template('index.html',user= current_user)

@views.route('/artists', methods=['GET'])
def artists():
    return render_template('ArtistSelection.html',user=current_user)
@views.route('/artistbooking', methods=['GET'])
def artistbooking():
    return render_template('artistbooking.html',user=current_user)

@views.route('/artistsSolo', methods=['GET'])
def artistsSolo():
    return render_template('solo.html',user=current_user)

@views.route('/artistsDuet', methods=['GET'])
def artistsDuet():
    return render_template('duet.html',user=current_user)
# @views.route('/stripe_pay')
# def index():
#     session = stripe.checkout.Session.create(
#         payment_method_types=['card'],
#         line_items=[{
#             'price': 'price_1O03qnSAm1yXJy6FP8bV5LxP',
#             'quantity': 1,
#         }],
#         mode='payment',
#         success_url=url_for('thanks', _external=True) + '?session_id={CHECKOUT_SESSION_ID}',
#         cancel_url=url_for('stripe', _external=True),
#     )
#     return  render_template('stripe.html',
#                             checkout_session_id=session['id'],
#                             checkout_public_key=app.config['STRIPE_PUBLIC_KEY']
#                             )



# @views.route('/thanks',methods =['GET','POST'])
# def thanks():
#     if request.method == 'POST':
#         msg = Message("Hey how are you ",sender = 'noreply@demo.com',recipients = ['bhagyabeeb@gmail.com'])
#         msg.body = "yo yo"
#         mail.send(msg)
#         return "sent email"
#     return render_template('thanks.html')
@views.route('/book-now',methods =['GET','POST'])
def book():
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price': 'price_1O03qnSAm1yXJy6FP8bV5LxP',
            'quantity': 1,
        }],
        mode='payment',
        success_url=url_for('views.thanks', _external=True) + '?session_id={CHECKOUT_SESSION_ID}',
        cancel_url=url_for('views.sstripe', _external=True),
    )
    return  render_template('payment.html',user=current_user,
                            checkout_session_id=session['id'],
                            checkout_public_key='pk_test_51O03ftSAm1yXJy6FXwURoEWIig94zvLUQG2UEmLhq9UogQ9ipcKJcjlaBVb7sJSeoRBn5Dg7Ghnu8zBEqwdG3IEt0017SqYlZK'
                            )


@views.route('/book',methods = ['GET','POST'])
def sstripe():
    return render_template('stripe.html',user=current_user)
@views.route('/payment',methods =['POST'])
def payment():
    return render_template('payment.html',user=current_user)

@views.route('/chat')
def chat():
    return render_template('chatbot.html')

@views.route('/predict',methods =['POST'])
def predict():
    text = request.get_json().get("message")

    response = get_response(text)
    message = {"answer": response}
    return  jsonify(message)



























