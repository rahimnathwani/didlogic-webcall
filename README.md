didlogic-webcall
================

Python script to initiate a phone call between two numbers using DIDLogic's webcall service

usage: didlogic.py [-h] from_number to_number username password

e.g. If your number is +8618612345678 and you want to call +442072221234, then:

didlogic.py 8618612345678 442072221234 user@domain.com supersecretpass

Of course, you need some credit in your DIDLogic account.  You will be charged for two outbound calls: one to your phone, and the other to your destination number.

I made this script because:
- VoIP calls aren't always stable on my bus ride home
- DIDLogic's rates for calling some destinations (e.g. UK mobiles) are much cheaper than alternatives
- DIDLogic's web interface is a pain to use on a small screen

I use the script with a macro on vSSH on iPhone.  I save my username, password, and from_number in the macro, and it prompts me to enter the phone number before sending the command to the server.

