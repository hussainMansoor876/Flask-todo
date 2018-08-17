from flask import Flask ,jsonify
from flask_pymongo import PyMongo

app=Flask(__name__)
app.config['MONGO_DBNAME']='todo-123'
app.config['MONGO_URI']='mongodb://todo123:todo123@ds119702.mlab.com:19702/todo-123'

mongo=PyMongo(app)

# @app.route("/form")
# def index():
#     students=[]
#     # records = mongo.db.users.find({'name':'Hussain' or 'hussain','pass':'password'})
#     records = mongo.db.users.find()
#     for user in records:
#         students.append({'name': user['name'], 'password': user['pass']})

    
#     return jsonify({'SaylaniStudents': students})

@app.route("/")
def add():
    add = mongo.db.users
    add.insert({'name' :'Sufiyan','pass':'Password'})
    return 'Successfully Add'
app.run(debug=True)