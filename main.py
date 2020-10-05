from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def home():
    # POST
    if request.method == 'POST':

        json = request.get_json()

        if 'acc' in json and 'dsc' in json:
            if json['acc'].lower() == "aggie coding club" and json['dsc'].lower() == "developer student club":
                return "That's Correct! For the next question, make a POST request to https://acc-dsc-api.herokuapp.com/numofficers with a JSON object payload of key “num_officers” and the value as an integer number as your answer to how many officers acc has. Go to aggiecodingclub.com to find out!"
            else:
                return "Hmmm... Didn't get the names quite right. Try again!"
        else:
            return 'Not quite! Make sure you have no extra spaces. The values for each acronymn be the full form. POST a JSON object {"acc": "your_answer_here","dsc": "your_answer_here"} on the same url'
    else:
        return 'WELCOME! Create a POST request on the same URL with the full forms of the acronyms "acc" and "dsc" via the following JSON object {"acc": "your_answer_here","dsc": "your_answer_here"}'


@app.route('/numofficers', methods=['POST'])
def numOfficers():
    if request.method == 'POST':

        json = request.get_json()

        if 'num_officers' in json:
            numOfficers = json['num_officers']
            if type(numOfficers) is int:
                numOfficers = str(numOfficers)
            if numOfficers.isnumeric() and int(numOfficers) == 9:
                return "You are on a roll! For the next question, make a GET request to https://acc-dsc-api.herokuapp.com/initials/<dsc-lead-last-name> for your next question. With the first three letters of the last name (all lowercase) of the DSC lead as the value in the url (remove the angle brackets). Visit https://dsc.community.dev/texas-am-university for details"
            else:
                return "Hmmm... Didn't get the number quite right. Try again!"
        else:
            return "Not quite! Make sure your key is num_officers"


@app.route('/initials/<name>', methods=['GET'])
def initials(name):
    if request.method == 'GET':
        if name.lower() == 'sri':
            return "You're an expert! Next, make a POST request to https://acc-dsc-api.herokuapp.com/next-dsc-event with the JSON object payload of key “word” and the value as the 2nd to last word of the event on October 10th.  Visit https://dsc.community.dev/texas-am-university for details"
        else:
            return "Not quite! Make sure you have the first 3 letters of her last name right! Hint: She is also the webmaster for ACC"


@app.route('/next-dsc-event', methods=['POST'])
def nextDscEvent():
    if request.method == 'POST':

        json = request.get_json()

        if 'word' in json:
            if json['word'].lower() == 'qwiklabs':
                return "Sweet! One more question and you're on the board...But beware, this one is a bit tricky; don’t be spooked it’s not halloween, but this is a tool that you have all seen. Take a closer look and inspect the ACC website, for what you will find is an image in no time. Gather the source and make your POST request to the https://acc-dsc-api.herokuapp.com/<src> of the image image (omit the .png). One last step.. Add a JSON object with ‘height’ as the max height of the image!"
            else:
                return "Hmmm... Didn't get the word quite right. Try again!"
        else:
            return "Not quite! Make sure you have no extra spaces. HINT: the word is 8 letters long and kinda quirky."


@app.route('/static/images/acc-website-graphics', methods=['POST'])
def finalStretch():
    if request.method == 'POST':

        json = request.get_json()

        if 'height' in json:
            height = json['height']
            if type(height) is int:
                height = str(height)
            if height.isnumeric() and int(height) == 400:
                return "CONGRATULATIONS! Message in the Zoom saying 'Liitle Mac Trash' to Shrey Shah privately and we will know you won!"
            else:
                return "Hmmm... Didn't get the height quite right. Try again!"
        else:
            return "Not quite! Make sure you send it as 'height' and not 'max_height'."


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
