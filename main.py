from flask import Flask, jsonify , request

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'take books to school',
        'description': u'english, french', 
        'done': False
    },
]
@app.route("/")
def name():
    return "This is the homepage use /add-data to move to the TO DO LIST"

@app.route("/add-data",methods = ["POST"] )   
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the data!"
        },400)

    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description',""), 
        'done': False
     }        
    tasks.append(task)
    return jsonify({
          "status":"success",
            "message": "task added succesfully!"
     })

@app.route("/get-data")
def get_task():
    return jsonify({
        "data":tasks
    })
    
if(__name__ == "__main__"):
     app.run(debug=True)


    