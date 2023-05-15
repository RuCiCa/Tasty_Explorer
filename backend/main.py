from flask import Flask, jsonify, request
from flask_cors import CORS

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, text



app = Flask(__name__)
CORS(app, resources={r"/*":{"origins":"*"}})
app.config.from_object(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://gdsc:NCCUgdsc1234!@34.81.186.58:3306/bricksdata"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
engine = create_engine("mysql+pymysql://gdsc:NCCUgdsc1234!@34.81.186.58:3306/bricksdata")
conn = engine.connect()
app.config.from_object(__name__)



DATA = [
    {
    "account":"RuCiCa",
    "password": "RuCiCa0307"
    },
    {
    "account":"LuCiCa",
    "password": "LuCiCa0307"
    }
    ]

P_DATA = [
    {
    "project_id":"1",
    "project_type": "未分類",
    "project_image": "test1.jpg",
    "project_name": "一般",
    "project_trashcan": False,
    "project_ended": False,
    "project_isEdit": False,
    "project_isVisible": False,
    "project_isComment": False,
    "user_id": "1"
    },
    {
    "project_id":"2",
    "project_type": "學校",
    "project_image": "test2.jpg",
    "project_name": "未結束",
    "project_trashcan": True,
    "project_ended": False,
    "project_isEdit": False,
    "project_isVisible": False,
    "project_isComment": False,
    "user_id": "1"
    },
    {
    "project_id":"3",
    "project_type": "學校",
    "project_image": "test3.jpg",
    "project_name": "已結束",
    "project_trashcan": True,
    "project_ended": True,
    "project_isEdit": False,
    "project_isVisible": False,
    "project_isComment": False,
    "user_id": "1"
    },
    {
    "project_id":"4",
    "project_type": "未分類",
    "project_image": "test2.jpg",
    "project_name": "已結束",
    "project_trashcan": False,
    "project_ended": True,
    "project_isEdit": False,
    "project_isVisible": False,
    "project_isComment": False,
    "user_id": "1"
    },
    {
    "project_id":"5",
    "project_type": "學校",
    "project_image": "test3.jpg",
    "project_name": "2的垃圾桶",
    "project_trashcan": True,
    "project_ended": True,
    "project_isEdit": False,
    "project_isVisible": False,
    "project_isComment": False,
    "user_id": "2"
    },
    {
    "project_id":"6",
    "project_type": "學校",
    "project_image": "test2.jpg",
    "project_name": "未結束",
    "project_trashcan": False,
    "project_ended": False,
    "project_isEdit": False,
    "project_isVisible": False,
    "project_isComment": False,
    "user_id": "1"
    },
    {
    "project_id":"7",
    "project_type": "學校",
    "project_image": "test2.jpg",
    "project_name": "未結束",
    "project_trashcan": False,
    "project_ended": False,
    "project_isEdit": False,
    "project_isVisible": False,
    "project_isComment": False,
    "user_id": "1"
    },
    {
    "project_id":"8",
    "project_type": "未分類",
    "project_image": "test2.jpg",
    "project_name": "未結束",
    "project_trashcan": False,
    "project_ended": False,
    "project_isEdit": False,
    "project_isVisible": False,
    "project_isComment": False,
    "user_id": "1"
    }
    ]

U_DATA = [
    {
    "user_id":"1",
    "user_name": "rucica",
    "user_account": "RuCiCa",
    "user_password": "RuCiCa0307",
    "user_purpose": "Student",
    "user_email": "rucica0307@gmail.com",
    "user_identity": "Profession",
    "user_otherool": "",
    },
    {
    "user_id":"2",
    "user_name": "lucica",
    "user_account": "LuCiCa",
    "user_purpose": "Student",
    "user_email": "lucica0307@gmail.com",
    "user_identity": "B.jpg",
    "user_otherool": "",
    }
]

N_DATA = [
    {
    "notification_id":"1",
    "notification_content": "測試",
    "notification_sender_id": "1",
    }
]



# hello world route
@app.route("/", methods=["GET"])
def greetings():
    return("Hello, world!")


@app.route("/bricks", methods=["GET"])
def bricks():
    return("Bricks專案管理實用工具讚讚!")

@app.route("/login", methods=["GET", "POST"])
def login():
    response_object = {"status": "success"}
    if request.method == "POST":
        post_data = request.get_json()
        for account_info in U_DATA:
            if account_info["user_account"] == post_data.get("account") and account_info["user_password"] == post_data.get("password"):
                response_object["message"] = "登入成功"
                break
            else:
                response_object["status"] = "failed"
                response_object["message"] = "登入失敗"

    else:
        response_object["items"] = P_DATA

    return jsonify(response_object)

@app.route("/project_index", methods=["POST"])
def get_project():
    list = []
    response_object = {"status": "success"}
    post_data = request.get_json()
    found = False
    for project_info in P_DATA:
        if project_info["user_id"] == post_data.get("user_id"):
            if post_data.get("project_status") == "normal":
                    if project_info["project_trashcan"] == False:
                        if project_info["project_ended"] == False:
                            list.append(project_info)
                            found = True
            if post_data.get("project_status") == "ended":
                if project_info["project_trashcan"] == False:
                        if project_info["project_ended"] == True:
                            list.append(project_info)
                            found = True
            if post_data.get("project_status") == "trashcan":
                if project_info["project_trashcan"] == True:
                        list.append(project_info)
                        found = True
    if found == False:
        response_object["status"] = "failed"
        response_object["message"] = "沒找到"

    list = sorted(list, key=lambda x: (x['project_type'] == '未分類', x['project_type']))
    response_object["items"] = list
    return jsonify(response_object)


@app.route("/set_project_end", methods=["POST"])
def set_end():
    response_object = {"status": "success"}
    put_data = request.get_json()
    for project_info in P_DATA:
            if project_info["project_id"] == put_data.get("project_id"):
                if project_info["project_ended"] == False:
                    project_info["project_ended"] = True
                    response_object["message"] = "修改成功"
                break
            else:
                response_object["status"] = "failed"
                response_object["message"] = "修改失敗"
    

    return jsonify(response_object)

@app.route("/add_project", methods=["POST"])
def add_project():
    response_object = {"status": "success"}
    post_data = request.get_json()

    P_DATA.append({
            "project_id":  post_data.get("project_id"),
            "project_type": post_data.get("project_type"),
            "project_image": post_data.get("project_image"),
            "project_name":  post_data.get("project_name"),
            "project_trashcan": post_data.get("project_trashcan"),
            "project_ended": post_data.get("project_ended"),
            "project_isEdit": post_data.get("project_isEdit"),
            "project_isVisible": post_data.get("project_isVisible"),
            "project_isComment": post_data.get("project_isComment"),
            "user_id": post_data.get("user_id"),
        })

    response_object["items"] = P_DATA

    return jsonify(response_object)

@app.route("/edit_type", methods=["POST"])
def add_type():
    response_object = {"status": "success"}
    post_data = request.get_json()
    for project_info in P_DATA:
            if project_info["project_id"] == post_data.get("project_id"):
                project_info["project_type"] = (post_data.get("project_type"))
                response_object["message"] = "類別修改成功"
                break
            else:
                response_object["status"] = "failed"
                response_object["message"] = "該專案不存在，類別修改失敗"

    response_object["items"] = P_DATA

    return jsonify(response_object)

@app.route("/personal_setting", methods=["POST"])
def personal_setting():
    found = False
    response_object = {"status": "success"}
    post_data = request.get_json()
    for user_info in U_DATA:
         if user_info["user_id"] == post_data.get("user_id"):
              response_object["items"] = user_info
              found = True
              break
    
    if found == False:
        response_object["message"] = "not found"
        response_object["status"] = "failed"
    
    
    return jsonify(response_object)




if __name__ == "__main__":
    app.run(debug=True)