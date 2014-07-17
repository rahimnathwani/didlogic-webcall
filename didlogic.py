import re
from robobrowser import RoboBrowser as RB
import argparse

# Parse arguments
parser = argparse.ArgumentParser(description='Place a call via DidLogic.')
parser.add_argument("from_number")
parser.add_argument("to_number")
parser.add_argument("username")
parser.add_argument("password")
args = parser.parse_args()

from_number, to_number, username, password = args.from_number, args.to_number, args.username, args.password

# Open a browser
browser = RB(history=True)

# Log in
browser.open('https://didlogic.com/')
form = browser.get_form(action='/session')
form['email'].value = username
form['password'].value = password
browser.submit_form(form)

# Submit web call
browser.open('https://didlogic.com/webcalls/new')
form = browser.get_form(action='/webcalls')
# form['webcall[from_transport]'].value = '4'
# form['webcall[to_transport]'].value = '4'
form['webcall[from]'].value = from_number
form['webcall[to]'].value = to_number
browser.submit_form(form)
