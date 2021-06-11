# Best Buy Bot
Bot that scrapes the best buy website to buy stuff. Useful for auto-gpu buying and whatnot.

# Prerequisites
1. Already have a best buy account with payment and shipping info setup
2. Have [Python 3.9](https://www.python.org/downloads/) installed
3. Have [Google Chrome](https://www.google.com/chrome/) installed
4. If you don't have the selenium package run `pip install selenium` on the command line to install it

# Setup
1. Go into 'details.json' and edit the values of email, password, cvv, and link to what you need
2. Run bot.py

That's all! This code was inspired by [nickconnors' bot](https://github.com/nickconnors/RTX-3070-Best-Buy-Bot).
I really like the way they used their try and except loops so I implemented that. I decided use a .json file instead of a .py to store the information.
I also included the 'chromedriver.exe' to make it easier to use.
