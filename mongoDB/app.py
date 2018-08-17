from flask import Flask,render_template,url_for,request,jsonify
from flask_pymongo import PyMongo
from flask_bootstrap import Bootstrap
from app1 import TodoForm
import json
from bson.json_util import dumps, ObjectId

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['MONGO_DBNAME']='todo-123'
app.config['MONGO_URI']='mongodb://todo123:todo123@ds119702.mlab.com:19702/todo-123'
app.config['SECRET_KEY'] = 'todo Assignment'
mongo = PyMongo(app)

@app.route('/', methods=['GET'])
def index():
    add = mongo.db.todo
    title = None
    description = None
    task = False
    form = TodoForm()
    if form.validate_on_submit():
        title = form.title.data
        description = form.description.data
        add.insert({'title':title,'description':description,'task':task})
        form.title.data = ''
        form.description.data = ''
    return render_template('index.html', form=form)


@app.route('/todo/api/v1.0/',methods=["POST"])
def todoApi():
    data = []
    api = mongo.db.todo.find()
    for obj in api:
        data.append({'title':obj['title'],'description':obj['description'],'task':obj['task'],'id':str(obj['_id'])})
    return jsonify({'data':data})

@app.route('/todo/api/v1.0/<id>',methods=["GET"])
def todoApitask(id):
    data = []
    api = mongo.db.todo.find_one({'_id': ObjectId(id)})
    if api:
        data.append({"_id":id,
                       "title":api["title"],
                       "description":api["description"],"complete":api["task"]})
    else:
        data= "Nothing Found"
    return jsonify({"results ":data})

@app.route('/todo/api/v1.0/<id>',methods=['PUT'])
def modifytodo(id):
    api = mongo.db.todo

    todo = api.find_one({"_id": ObjectId(id)})
    result = None
    if todo:
     todo["task"]=True
     api.save(todo)
     result = 'Modify Successfully'
    else:
        result ="Unable to complete request"


    return jsonify({"Result ": result})

@app.route('/todo/api/v1.0/<id>',methods=["DELETE"])
def deletetodo(id):
    api = mongo.db.todo
    api.delete_one({"_id": ObjectId(id)})
    return jsonify("Deleted")

@app.route('/todo/api/v2.0/')
def todoApi1():
    data = []
    api = mongo.db.todo.find()
    for obj in api:
        data.append({'obj':str(obj)})
    return jsonify({'data':data})

if __name__ == '__main__':
    app.run(debug=True)