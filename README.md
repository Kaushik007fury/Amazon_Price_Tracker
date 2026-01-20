Amazon Price Tracker
A simple Python script that tracks the price of an Amazon product and sends an email alert when the price drops below a target value.

Features:
1.Scrapes product title and price from Amazon
2.Compares price with a predefined threshold
3.Sends an email alert when the price drops
4.Uses environment variables for email credentials(best for safety)

Tech Used:
1.Python
2.Requests
3.BeautifulSoup
4.smtplib
5.python-dotenv

Setup:-
Install dependencies:
pip install requests beautifulsoup4 python-dotenv

Create a .env file:
SENDER=your_email@gmail.com
RECIEVER=receiver_email@gmail.com
APP_PW=your_gmail_app_password

Set your target price in the script:
BUY_PRICE = 8500

Run
python main.py

-> You’ll receive an email alert when the product price drops below the target.

Notes:
Amazon page structure may change and break scraping !
Use Gmail App Passwords, not your main password!
Intended for educational purposes!
