# Crypto Wallet Project

A simple and lightweight cryptocurrency wallet web application built with **Flask** and **SQLite**.  
It allows users to securely store, manage, and track cryptocurrency transactions on a minimal blockchain simulation.

---

## 🚀 Features
- 🛡️ Securely store and send transactions.
- 📜 Maintain a complete transaction history.
- 📈 Track current wallet balance.
- 🎨 Clean and aesthetic frontend with responsive design.
- 🛠️ Lightweight blockchain-like structure for internal transaction recording.

---

## 🛠️ Technologies Used

- Frontend: HTML, CSS
- Backend: Python (Flask Framework)
- Database: SQLite
- Version Control: Git & GitHub

---

## 📦 Installation Steps

1. Clone the repository:
   bash:
   git clone https://github.com/your_username/crypto_wallet_project.git
2.Navigate into the project folder:
   bash:
   cd crypto_wallet_project
3.Install required Python packages:
   bash:
   pip install flask
4.Start the Flask server:
   bash:
   python app.py
5.Open your browser and visit:
   http://127.0.0.1:5000/

---

⚙️ Project Structure

crypto_wallet_project/
├── app.py              # Flask backend application
├── blockchain.py       # Blockchain-related classes and transaction handling
├── static/
│   └── style.css       # Frontend styling
├── templates/
│   └── index.html      # Frontend web page
├── wallet.db           # SQLite database file (auto-created after first run)
└── README.md           # Project description (this file)

---

📋 Key Functionalities

1.View Wallet: See all past transactions and current balance.
2.Send Transaction: Enter receiver's address and amount to transfer.
3.Error Handling: Shows error if user tries to send more than available balance.
4.Database: All transactions are stored securely in an SQLite database.

---

💡 Future Improvements

1.Add user login system (authentication).
2.Extend Blockchain logic to real-time mining/blocks.
3.Connect real cryptocurrency APIs.
4.Add QR Code generation for addresses.
5.Deploy the application online (Render, Heroku).

---

✨ Author

Chinmayi 
GitHub: chinmayijagadish606@gmail.com



