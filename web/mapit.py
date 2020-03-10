""" Opens a map to the address specified in the CLI argument"""

import webbrowser, sys
# webbrowser.open('https://www.google.co.in/')

# sys.argv stores the list of all commandline argumnets including the name of the file being executed.
# print(sys.argv)
if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
# else:
#     # Get address from clipboard.
#     address = pyperclip.paste()
# print(address)
webbrowser.open('https://www.google.com/maps/place/' + address)