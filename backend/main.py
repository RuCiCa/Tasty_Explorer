import datetime

from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, text

today_weekday = datetime.date.today().weekday()

app = Flask(__name__)
CORS(app, resources={r"/*":{'origins':"*"}})
# engine = create_engine("mysql+pymysql://gdsc:NCCUgdsc1234!@34.81.186.58:3306/bricksdata?charset=utf8mb4")
engine = create_engine("mysql+pymysql://root:Yu0!newcode@localhost:3306/tastyexplorerdb?charset=utf8mb4")

app.config.from_object(__name__)


  
def open_check(id, conn):
    open_query = """
            SELECT
                weekday, openning_time, closing_time
            FROM
                business_hour
            WHERE
                restaurant_id = {};
        """.format(id)
    open = query_data(conn, open_query)

    matching_dict = None
    for item in open:
        if item["weekday"] == today_weekday:
            matching_dict = item
            break
    opening_time = matching_dict["openning_time"]
    closing_time = matching_dict["closing_time"]
    if opening_time > datetime.datetime.now().time() > closing_time:
        open_status = {
            "operating_status": True,
            "time": closing_time
        }
    else:
        open_status = {
            "operating_status": False,
            "time": opening_time
        }

    return open_status

def query_data(conn, query):
    data = conn.execute(text(query))
    keys = list(data.keys())
    new_data = [dict(zip(keys, row)) for row in data.fetchall()]

    return new_data

def get_personal_info(conn, id):
    info_query = """
    SELECT user_name, profile_photo
        FROM users
        WHERE id = {};
    """.format(id)

    diary_query = """
    SELECT
        diary.restaurant_id, diary.date_visited, diary.is_public,  
        diary.photo, diary.user_id, users.user_name, restaurants.restaurant_name
    FROM
        diary
        JOIN users ON diary.user_id = users.id
        JOIN restaurants ON diary.restaurant_id = restaurants.id
    WHERE
        diary.user_id = {};
    """.format(id)

    follower_query = """
    SELECT users.user_name, following_relation.following_id, users.profile_photo
    FROM 
        following_relation
        JOIN users ON following_relation.followers_id = users.id
    WHERE followers_id = {};
    """.format(id)

    following_query = """
    SELECT users.user_name, following_relation.followers_id, users.profile_photo
    FROM 
        following_relation
        JOIN users ON following_relation.following_id = users.id
    WHERE following_relation.following_id = {};
    """.format(id)

    comment_query = """
    SELECT feedback_rating.id, restaurants.restaurant_name, AVG(feedback_rating.total_rating) AS avg_rating, feedback_rating.feedback, feedback_rating.photo, feedback_rating.post_date
    FROM feedback_rating
    JOIN restaurants ON feedback_rating.restaurant_id = restaurants.id
    WHERE feedback_rating.user_id = {}
    GROUP BY feedback_rating.id, restaurants.restaurant_name, feedback_rating.feedback, feedback_rating.photo, feedback_rating.post_date;
    """.format(id)

    list_query = """
    SELECT id, list_name
        FROM lists
        WHERE user_id = {};
    """.format(id)

    info = query_data(conn, info_query)
    diary = query_data(conn, diary_query)
    follower = query_data(conn, follower_query)
    following = query_data(conn, following_query)
    comment = query_data(conn, comment_query)
    list = query_data(conn, list_query)

    info_count = len(info)
    diary_count = len(diary)
    follower_count = len(follower)
    following_count = len(following)
    comment_count = len(comment)
    list_count = len(list)

    return info, diary, follower, following, comment, list, info_count, diary_count, follower_count, following_count, comment_count, list_count


# hello world route
@app.route("/", methods=["GET"])
def greetings():
    return("Hello, world!")

@app.route("/follow", methods=["GET"])
def get_follow():
    response_object = {"status": "success"}
    try:
        conn = engine.connect()
        get_data = request.get_json()
        user_id = get_data.get("user_id")
        info, diary, follower, following, comment, list, info_count, diary_count, follower_count, following_count, comment_count, list_count = get_personal_info(conn, user_id)

        response_object["info"] = info
        response_object["following"] = following
        response_object["info_count"] = info_count
        response_object["diary_count"] = diary_count
        response_object["follower_count"] = follower_count
        response_object["following_count"] = following_count
        response_object["comment_count"] = comment_count
        response_object["list_count"] = list_count

    except Exception as e:
        response_object["status"] = "failed"
        response_object["message"] = str(e)

    
    return jsonify(response_object)

@app.route("/follow", methods=["POST"])
def follow():
    response_object = {"status": "success"}
    try:
        conn = engine.connect()
        post_data = request.get_json()
        following_id = post_data.get("following_id")
        user_id = post_data.get("user_id")
        follow_or_disfollow = post_data.get("follow_or_disfollow")
        if follow_or_disfollow == True:
            follow_query = """
                INSERT INTO following_relation (follower, following)
                VALUES 
                ({}, {});
            """.format(following_id, user_id)
        else:
            follow_query = """
                DELETE FROM following_relation
                WHERE follower = {} AND following = {};
            """.format(following_id, user_id)

        conn.execute(text(follow_query))
        conn.execute(text("COMMIT;"))

        info, diary, follower, following, comment, list, info_count, diary_count, follower_count, following_count, comment_count, list_count = get_personal_info(conn, user_id)

        response_object["info"] = info
        response_object["following"] = following
        response_object["info_count"] = info_count
        response_object["diary_count"] = diary_count
        response_object["follower_count"] = follower_count
        response_object["following_count"] = following_count
        response_object["comment_count"] = comment_count
        response_object["list_count"] = list_count

        conn.close()
        
    except Exception as e:
        response_object["status"] = "failed"
        response_object["message"] = str(e)

    return jsonify(response_object)

@app.route("/follower", methods=["GET"])
def get_follower():
    response_object = {"status": "success"}
    try:
        conn = engine.connect()
        get_data = request.get_json()
        user_id = get_data.get("user_id")
        info, diary, follower, following, comment, list, info_count, diary_count, follower_count, following_count, comment_count, list_count = get_personal_info(conn, user_id)

        response_object["info"] = info
        response_object["follower"] = follower
        response_object["info_count"] = info_count
        response_object["diary_count"] = diary_count
        response_object["follower_count"] = follower_count
        response_object["following_count"] = following_count
        response_object["comment_count"] = comment_count
        response_object["list_count"] = list_count

    except Exception as e:
        response_object["status"] = "failed"
        response_object["message"] = str(e)
    
    return jsonify(response_object)

@app.route("/follower", methods=["POST"])
def follower():
    response_object = {"status": "success"}
    try:
        conn = engine.connect()
        post_data = request.get_json()
        follower_id = post_data.get("follower_id")
        user_id = post_data.get("user_id")
        follow_or_disfollow = post_data.get("follow_or_disfollow")
        if follow_or_disfollow == True:
            follow_query = """
                INSERT INTO following_relation (follower, following)
                VALUES 
                ({}, {});
            """.format(user_id, follower_id)
        else:
            follow_query = """
                DELETE FROM following_relation
                WHERE follower = {} AND following = {};
            """.format(user_id, follower_id)

        conn.execute(text(follow_query))
        conn.execute(text("COMMIT;"))

        info, diary, follower, following, comment, list, info_count, diary_count, follower_count, following_count, comment_count, list_count = get_personal_info(conn, user_id)

        response_object["info"] = info
        response_object["follower"] = follower
        response_object["info_count"] = info_count
        response_object["diary_count"] = diary_count
        response_object["follower_count"] = follower_count
        response_object["following_count"] = following_count
        response_object["comment_count"] = comment_count
        response_object["list_count"] = list_count

        conn.close()
        
    except Exception as e:
        response_object["status"] = "failed"
        response_object["message"] = str(e)
    
    return jsonify(response_object)

@app.route("/diary", methods=["GET"])
def get_all_diary():
    response_object = {"status": "success"}
    try:
        conn = engine.connect()
        get_data = request.get_json()
        user_id = get_data.get("user_id")
        info, diary, follower, following, comment, list, info_count, diary_count, follower_count, following_count, comment_count, list_count = get_personal_info(conn, user_id)
        conn.close()

        response_object["info"] = info
        response_object["diary"] = diary
        response_object["info_count"] = info_count
        response_object["diary_count"] = diary_count
        response_object["follower_count"] = follower_count
        response_object["following_count"] = following_count
        response_object["comment_count"] = comment_count
        response_object["list_count"] = list_count
        
    except Exception as e:
        response_object["status"] = "failed"
        response_object["message"] = str(e)
    
    return jsonify(response_object)

@app.route("/diary_info", methods=["GET"])
def get_diary():
    response_object = {"status": "success"}
    try:
        conn = engine.connect()
        get_data = request.get_json()
        user_id = get_data.get("user_id")
        id = get_data.get("dairy_id")
        info, diary, follower, following, comment, list, info_count, diary_count, follower_count, following_count, comment_count, list_count = get_personal_info(conn, user_id)
        
        diary_query = """
            SELECT
                diary.restaurant_id, diary.date_visited, diary.is_public, 
                diary.photo, diary.user_id, users.user_name, restaurants.restaurant_name
            FROM
                diary
                JOIN users ON diary.user_id = users.user_id
                JOIN restaurants ON diary.restaurant_id = restaurants.id
            WHERE
                diary.diary_id = {};
        """.format(id)
        diary = query_data(conn, diary_query)
        response_object["diary"] = diary
        conn.close()

        response_object["info"] = info
        response_object["info_count"] = info_count
        response_object["diary_count"] = diary_count
        response_object["follower_count"] = follower_count
        response_object["following_count"] = following_count
        response_object["comment_count"] = comment_count
        response_object["list_count"] = list_count
        
    except Exception as e:
        response_object["status"] = "failed"
        response_object["message"] = str(e)

    return jsonify(response_object)

@app.route("/diary_post", methods=["POST"])
def post_diary():
    response_object = {"status": "success"}
    try:
        conn = engine.connect()
        post_data = request.get_json()
        res_id = post_data.get("restaurant_id")
        user_id = post_data.get("user_id")
        content = post_data.get("content")
        photo = post_data.get("photo")

        diary_query = """
            INSERT INTO diary (restaurant_id, user_id, content, photo)
            VALUES 
            ({}, {}, "{}", "{}");
        """.format(res_id, user_id, content, photo)

        conn.execute(text(diary_query))
        conn.execute(text("COMMIT;"))

        conn.close()

        response_object["message"] = "新增成功"
        
    except Exception as e:
        response_object["status"] = "failed"
        response_object["message"] = str(e)

    return jsonify(response_object)

@app.route("/diary_edit", methods=["GET"])
def get_edit_diary():
    response_object = {"status": "success"}
    try:
        conn = engine.connect()
        get_data = request.get_json()
        id = get_data.get("dairy_id")
        
        diary_query = """
            SELECT
                diary.restaurant_id, diary.date_visited, 
                diary.photo, diary.user_id, users.user_name, restaurants.restaurant_name
            FROM
                diary
                JOIN users ON diary.user_id = users.user_id
                JOIN restaurants ON diary.restaurant_id = restaurants.id
            WHERE
                diary.diary_id = {};
        """.format(id)
        diary = query_data(conn, diary_query)
        response_object["diary"] = diary
        conn.close()
        
    except Exception as e:
        response_object["status"] = "failed"
        response_object["message"] = str(e)

    return jsonify(response_object)

@app.route("/diary_edit", methods=["POST"])
def edit_diary():
    response_object = {"status": "success"}
    try:
        conn = engine.connect()
        post_data = request.get_json()
        user_id = post_data.get("user_id")
        content = post_data.get("content")
        photo = post_data.get("photo")
        restaurant_id = post_data.get("restaurant_id")

        edit_diary_query = """
            UPDATE diary
            SET content = "{}", photo = "{}", restaurant_id = "{}"
            WHERE
            user_id = {};
        """.format(content, photo, restaurant_id, user_id)

        conn.execute(text(edit_diary_query))
        conn.execute(text("COMMIT;"))

        conn.close()

        response_object["message"] = "新增成功"
        
    except Exception as e:
        response_object["status"] = "failed"
        response_object["message"] = str(e)

    return jsonify(response_object)

@app.route("/list", methods=["GET"])
def get_all_list():
    response_object = {"status": "success"}
    try:
        conn = engine.connect()
        get_data = request.get_json()
        user_id = get_data.get("user_id")
        info, diary, follower, following, comment, list, info_count, diary_count, follower_count, following_count, comment_count, list_count = get_personal_info(conn, user_id)

        response_object["info"] = info
        response_object["list"] = list
        response_object["info_count"] = info_count
        response_object["diary_count"] = diary_count
        response_object["follower_count"] = follower_count
        response_object["following_count"] = following_count
        response_object["comment_count"] = comment_count
        response_object["list_count"] = list_count

    except Exception as e:
        response_object["status"] = "failed"
        response_object["message"] = str(e)
    
    return jsonify(response_object)

@app.route("/list_info", methods=["GET"])
def get_list_info():
    response_object = {"status": "success"}
    try:
        conn = engine.connect()
        get_data = request.get_json()
        id = get_data.get("list_id")
        diary_query = """
            SELECT
                id, list_name
            FROM
                lists
            WHERE
                id = {};
        """.format(id)
        diary = query_data(conn, diary_query)
        response_object["diary"] = diary
        conn.close()
        
    except Exception as e:
        response_object["status"] = "failed"
        response_object["message"] = str(e)
    
    return jsonify(response_object)

@app.route("/restaurant", methods=["POST"])
def get_restaurant():
    response_object = {"status": "success"}
    try:
        conn = engine.connect()
        post_data = request.get_json()
        id = post_data.get("restaurant_id")
        res_query = """
            SELECT
                restaurant_id, name,address, latitude, longitude, is_open, 
                food_type, phone, email, website, menu_id
            FROM
                restaurant
            WHERE
                restaurant_id = {};
        """.format(id)
        restaurant = query_data(conn, res_query)
        response_object["restaurant"] = restaurant

        open_status = open_check(id, conn)
        response_object["open_status"] = open_status
        conn.close()
        
    except Exception as e:
        response_object["status"] = "failed"
        response_object["message"] = str(e)

    return jsonify(response_object)

@app.route("/restaurant_info", methods=["POST"])
def get_restaurant_info():
    response_object = {"status": "success"}
    try:
        conn = engine.connect()
        post_data = request.get_json()
        id = post_data.get("restaurant_id")
        res_query = """
            SELECT
                restaurant_id, name,address, is_open, 
                phone, email, website, menu_id
            FROM
                restaurant
            WHERE
                restaurant_id = {};
        """.format(id)
        res_data = conn.execute(res_query)
        keys = list(res_data.keys())
        restaurant = [dict(zip(keys, row)) for row in res_data.fetchall()]
        response_object["restaurant"] = restaurant

        open_status = open_check(id, conn)
        response_object["open_status"] = open_status
        conn.close()
        
    except Exception as e:
        response_object["status"] = "failed"
        response_object["message"] = str(e)

    return jsonify(response_object)

@app.route("/restaurant_menu", methods=["POST"])
def get_menu_info():
    response_object = {"status": "success"}
    try:
        conn = engine.connect()
        post_data = request.get_json()
        id = post_data.get("menu_id")
        menu_query = """
            SELECT
                menu_id
            FROM
                menu
            WHERE
                menu_id = {};
        """.format(id)
        menu = query_data(conn, menu_query)
        response_object["restaurant"] = menu

        conn.close()
        
    except Exception as e:
        response_object["status"] = "failed"
        response_object["message"] = str(e)

    return jsonify(response_object)

@app.route("/restaurant_comment", methods=["POST"])
def get_comment():
    response_object = {"status": "success"}
    try:
        conn = engine.connect()
        post_data = request.get_json()
        id = post_data.get("restaurant_id")
        rating_query = """
            SELECT AVG(deliciousness_rating) AS avg_deliciousness,
                AVG(environment_rating) AS avg_environment,
                AVG(cp_rating) AS avg_cp
                AVG(total_rating) AS avg_total
            FROM feedback_rating
            WHERE restaurant_id = {};
        """.format(id)
        rating = query_data(conn, rating_query)
        response_object["rating"] = rating

        comment_query = """
            SELECT user_id, total_rating, feedback, photo, date_visited
                FROM feedback_rating
                WHERE restaurant_id = {};
        """.format(id)
        comment = query_data(conn, comment_query)
        response_object["comment"] = comment

        diary_query = """
            SELECT users.user_name, users.profile_photo
                FROM diary
                JOIN users ON diary.user_id = users.user_id
                WHERE restaurant_id = {};
        """.format(id)
        diary = query_data(conn, diary_query)
        response_object["comment"] = diary

        conn.close()
        
    except Exception as e:
        response_object["status"] = "failed"
        response_object["message"] = str(e)

    return jsonify(response_object)

@app.route("/restaurant_comment_post", methods=["POST"])
def post_comment():
    response_object = {"status": "success"}
    try:
        conn = engine.connect()
        post_data = request.get_json()
        res_id = post_data.get("restaurant_id")
        user_id = post_data.get("user_id")
        del_rating = post_data.get("deliciousness_rating")
        env_rating = post_data.get("environment_rating")
        cp_rating = post_data.get("cp_rating")
        comment = post_data.get("comment")
        photo = post_data.get("photo")
        total_rating = (del_rating + cp_rating + env_rating) / 3


        comment_query = """
            INSERT INTO feedback_rating (restaurant_id, user_id, deliciousness_rating,
            environment_rating, cp_rating, total_rating, comment, photo)
            VALUES 
            ({}, {}, {}, {}, {}, {}, "{}", "{}");
        """.format(res_id, user_id, del_rating, env_rating, cp_rating, total_rating, comment, photo)

        conn.execute(text(comment_query))
        conn.execute(text("COMMIT;"))

        conn.close()

        response_object["message"] = "新增成功"
        
    except Exception as e:
        response_object["status"] = "failed"
        response_object["message"] = str(e)

    return jsonify(response_object)

@app.route("/restaurant_add_list", methods=["POST"])
def add_list():
    response_object = {"status": "success"}
    try:
        conn = engine.connect()
        post_data = request.get_json()
        res_id = post_data.get("restaurant_id")
        user_id = post_data.get("user_id")
        list_id = post_data.get("list_id")
        is_visited = post_data.get("is_visited")
        is_favorite = post_data.get("is_favorite")
        is_wanted = post_data.get("is_wanted")


        insert_query = """
            INSERT INTO list (restaurant_id, user_id, list_id, is_visited, is_favorite, is_wanted)
            VALUES 
            ({}, {}, {}, {}, {}, {}, "{}", {}, "{}");
        """.format(res_id, user_id, list_id, is_visited, is_favorite, is_wanted)

        conn.execute(text(insert_query))
        conn.execute(text("COMMIT;"))

        conn.close()

        response_object["message"] = "新增成功"
        
    except Exception as e:
        response_object["status"] = "failed"
        response_object["message"] = str(e)

    return jsonify(response_object)


@app.route('/search', methods=['POST'])
def search():

    response_object = {'status': 'success'}
    try:
        conn = engine.connect()
    except:
        response_object['status'] = "connect failure"

    global search_content
    search_content = request.get_json().get("search_content")
    place_list = request.get_json().get("place_list")
    type_list = request.get_json().get("type_list")
    S_DATA = []

    try:
        searchResult = f"""
            SELECT r.restaurant_name, r.address, r.phone, AVG(f.total_rating) AS total_rating, COUNT(f.user_id) AS rating_num 
            FROM restaurant r
            JOIN (
                SELECT total_rating, user_id, restaurant_id
                FROM feedback_rating
            ) f
            ON r.id = f.restaurant_id
            

        ;"""

        result = conn.execute(text(searchResult))
        cols = list(result.keys())
        data = [dict(zip(cols, row)) for row in result.fetchall()]

        for restaurant_info in data:
            if lcs(restaurant_info) > 0:
                S_DATA.append(restaurant_info)

        S_DATA.sort(key=lcs, reverse=True)

        response_object['items'] = S_DATA
    except:
        response_object['status'] = "algorithm failure"

    result.close()
    conn.close()

    return jsonify(response_object)


def lcs(data):
    str1 = search_content
    str2 = data['restaurant_name']
    str1_len = len(str1)
    str2_len = len(str2)

    dp = [[0 for x in range(str1_len + 1)] for y in range(str2_len + 1)]

    for i in range(1, str2_len + 1):
        for j in range(1, str1_len + 1):
            if (str1[j - 1] == str2[i - 1]):
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[str2_len][str1_len]

if __name__ == "__main__":
    app.run(debug=True)