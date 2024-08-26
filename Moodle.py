import requests


def getMaterias(token, userid,link):
    url = link + '/webservice/rest/server.php'
    data = {
        'moodlewsrestformat': 'json',
        'wstoken': token,
        'wsfunction': 'core_enrol_get_users_courses',
        'userid': userid
    }
    res = requests.post(url, data=data).json()

    return res



def getAssignments(token, courseid , link):
    url = link + '/webservice/rest/server.php'
    data = {
        'moodlewsrestformat': 'json',
        'wstoken': token,
        'wsfunction': 'mod_assign_get_assignments',
        'courseids[0]': courseid
    }
    res = requests.post(url, data=data).json()

    return res




def getQuizes(token, courseid, link):
    url = link +'/webservice/rest/server.php'
    data = {
        'moodlewsrestformat': 'json',
        'wstoken': token,
        'wsfunction': 'mod_quiz_get_quizzes_by_courses',
        'courseids[0]': courseid
    }
    res = requests.post(url, data=data).json()

    return res



def getForums(token, courseid, link):
    url = link + '/webservice/rest/server.php'
    data = {
        'moodlewsrestformat': 'json',
        'wstoken': token,
        'wsfunction': 'mod_forum_get_forums_by_courses',
        'courseids[0]': courseid
    }
    res = requests.post(url, data=data).json()

    return res



def login(username, password ,link):
    url = link + '/login/token.php?service=moodle_mobile_app'
    data = {
        'moodlewsrestformat': 'json',
        'username': username,
        'password': password
    }

    res = requests.post(url, data=data).json()
    
    return res['token']
    #return jsonify({'token': res['token']})



def getUserId(token, username,link):
    url = link + '/webservice/rest/server.php'
    data = {
        'moodlewsrestformat': 'json',
        'wstoken': token,
        'wsfunction': 'core_user_get_users_by_field',
        'field': 'username',
        'values[0]': username
    }
    res = requests.post(url, data=data).json()
    
    return res[0]['id']


def IniciarSesion(username, password, link):

    try:
        token = login(username, password, link)

        userId = getUserId(token, username, link)
    except:
        
        token = None
        userId = None


    return token, userId