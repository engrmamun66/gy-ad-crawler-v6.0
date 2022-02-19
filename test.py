import os
import validators


url = 'https://www.atu.de/winterreifen/19-zoll'
# url = 'http:/bit.\y/Breitreifen-'

valid=validators.url(url)
if valid == True:
    print("Url is valid")
else:
    print("Invalid url")
