from flask import *
from config import *
from urllib.request import urlopen
from json import load, dumps

app = Flask(__name__)

markers = {"markers": 
    [
        {
            "active": "True",
            "id": "1",
            "icon": "/static/img/active.png",
            "cords": [55.825057381076974, 37.660095989744796]
        }, 
        {
            "active": "True", 
            "id": "2",
            "icon": "/static/img/active.png",
            "cords": [55.81173153663427, 37.7403867323819]
        }, 
        {
            "active": "False", 
            "id": "3",
            "icon": "/static/img/not_active.png",
            "cords": [55.84595627427325, 37.54763066029805]
        }, 
        {
            "active": "False", 
            "id": "4",
            "icon": "/static/img/not_active.png",
            "cords": [55.78402973748055, 37.65614698803291]
        }, 
        {
            "active": "True",
            "id": "1",
            "icon": "/static/img/active.png",
            "cords": [55.825057381036974, 37.660025989744796]
        }, 
        {
            "active": "True", 
            "id": "2",
            "icon": "/static/img/active.png",
            "cords": [55.81173153463427, 37.740385323819]
        }, 
        {
            "active": "False", 
            "id": "3",
            "icon": "/static/img/not_active.png",
            "cords": [55.84595677427325, 37.5476666029805]
        }, 
        {
            "active": "False", 
            "id": "4",
            "icon": "/static/img/not_active.png",
            "cords": [55.78402978748055, 37.65619698803291]
        }, 
        {
            "active": "True",
            "id": "1",
            "icon": "/static/img/active.png",
            "cords": [55.82597381076974, 37.66000989744796]
        }, 
        {
            "active": "True", 
            "id": "2",
            "icon": "/static/img/active.png",
            "cords": [55.81123453663427, 37.7454867323819]
        }, 
        {
            "active": "False", 
            "id": "3",
            "icon": "/static/img/not_active.png",
            "cords": [55.84595656427325, 37.54762366029805]
        }, 
        {
            "active": "False", 
            "id": "4",
            "icon": "/static/img/not_active.png",
            "cords": [55.78402973748345, 37.65614654803291]
        }, 
    ]

}

@app.route("/map")
def bluemap():
    return render_template('main.html', apikey=google_api_key, host=host)

@app.route("/static/img/<name>")
def images(name):
    return send_file('./static/imgs/'+name)

@app.route("/jsonapilist/markers")
def jsonapilist_markers():
    return markers

@app.route("/jsonapilist/markers/info/<marker_id>")
def markerinfo(marker_id):
    return {"name": str(marker_id), "info": str(marker_id)}
    

app.run(port=80, debug=True, host=host)