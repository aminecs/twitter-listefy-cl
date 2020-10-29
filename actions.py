import numpy as np
import json


def getFollowings(oauth, handle):
    response_followings = oauth.get(f"https://api.twitter.com/1.1/friends/ids.json?screen_name={handle}")
    parsed_data_followings = json.loads(response_followings.text)
    followings_arr = np.array(parsed_data_followings.get('ids'))
    return followings_arr


def createList(oauth, list_name):
    response = oauth.post(f"https://api.twitter.com/1.1/lists/create.json?name={list_name}&mode=private")
    parsed_response = json.loads(response.text)
    list_id = parsed_response["id"]
    return list_id


def createFollowersList(oauth, handle, list_name):
    followings = getFollowings(oauth, handle)
    list_id = createList(oauth, list_name)
    for i in range(0, len(followings), 100):
        followings_str = ','.join(str(following) for following in followings[i:i + 100])
        response = oauth.post("https://api.twitter.com/1.1/lists/members/create_all.json",
                              params={"list_id": list_id, "user_id": followings_str})
        if response.status_code != 200:
            raise Exception(f"There was an error {response}")
    return True
