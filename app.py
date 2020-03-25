from flask import Flask, render_template, request, redirect, jsonify
from pymongo import MongoClient


client = MongoClient("mongodb+srv://shreesh:gottacatchemall@projectcorontine-ohoqg.mongodb.net/test?retryWrites=true&w=majority")
db = client['hfg']
datacollection = db['feedback']
likesCount = db['Likes']


app = Flask(__name__)


@app.route('/', methods=['GET'])
def homepage():
    if request.method == "GET":
            return render_template('index.html')

@app.route('/events', methods=['GET'])
def eventspage():
    if request.method == "GET":
            return render_template('events.html')


@app.route('/material', methods=['GET'])
def materialpage():
    if request.method == "GET":
            return render_template('mat.html')

@app.route('/contact', methods=['GET', 'POST'])
def contactpage():
    nolikes = likesCount.find_one({'hfg':'likes'})['count']
    nodislikes = likesCount.find_one({'hfg':'dislikes'})['count']
    if request.method == "GET":
        return render_template('contact.html', nolikes=nolikes, nodislikes=nodislikes)
    
    if request.method == "POST":
        feedbackData ={
            'email':request.form['mail'],
            'user-feedback':request.form['feedback']
        }
        id = datacollection.insert_one(feedbackData) 
        return render_template('contact.html', nolikes=nolikes, nodislikes=nodislikes)

@app.route('/contact/like', methods=['POST'])
def likeAdd():
    likesCount.update_one({'hfg':'likes'},{'$inc':{'count':1}})
    # someValue=request.form['hfg2']
    someValue = 'something'
    return someValue

@app.route('/contact/dislike', methods=['POST'])
def likeSubtract():
    likesCount.update_one({'hfg':'dislikes'},{'$inc':{'count':1}})
    Somevalue = 'something'
    return Somevalue

@app.route('/contact/form', methods= ['POST'])
def formWithAJAX():
    feedback_data ={
            'email':request.form['mail'],
            'user_feedback':request.form['feedback']
        }
    id = datacollection.insert_one(feedback_data)
    returnVal = request.form['mail']
    return returnVal



@app.route('/maintainance')
def serverDown():
    initialLikes = {
        'hfg':'likes',
        'count':0
    }
    id = likesCount.insert_one(initialLikes)
    initialLikes2 = {
        'hfg':'dislikes',
        'count':0
    }
    id = likesCount.insert_one(initialLikes2)
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)