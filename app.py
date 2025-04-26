from flask import Flask, request, render_template, redirect, url_for
from blockchain import Blockchain
from models import db, Block
import json

app = Flask(__name__)
blockchain = Blockchain()

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///wallet.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add_transaction', methods=['POST'])
def add_transaction():
    sender = request.form['sender']
    receiver = request.form['receiver']
    coin = request.form['coin']
    amount = float(request.form['amount'])

    transaction = {
        "sender": sender,
        "receiver": receiver,
        "coin": coin,
        "amount": amount
    }
    blockchain.add_block([transaction])

    # Save to database
    new_block = Block(
        index=len(blockchain.chain)-1,
        timestamp=blockchain.chain[-1].timestamp,
        transactions=json.dumps(blockchain.chain[-1].transactions),
        previous_hash=blockchain.chain[-1].previous_hash,
        hash_=blockchain.chain[-1].hash
    )
    db.session.add(new_block)
    db.session.commit()

    return redirect(url_for('home'))

@app.route('/balance/<user>')
def balance(user):
    user_balance = blockchain.get_balance(user)
    return user_balance

@app.route('/transactions/<user>')
def transactions(user):
    user_txns = blockchain.get_transactions(user)
    return {"transactions": user_txns}

if __name__ == '__main__':
    app.run(debug=True)
