# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 12:48:27 2018

@author: hasee
"""

# -*- coding: utf-8 -*-
import urllib.request as ul_re
import json
import jsonpath
bot_id = ''
return_session = ''
while 1:
    user_text = input('ask:')
    url = 'https://aip.baidubce.com/rpc/2.0/unit/bot/chat?access_token=24.62800c1e0d94478b487ec04859411f5b.2592000.1546348586.282335-14856895'
    post_data = {
        "bot_session": return_session,
        "log_id": "7758521",
        "request": {
            "bernard_level": 0,
            "client_session": "{\"client_results\":\"\", \"candidate_options\":[]}",
            "query": user_text,
            "query_info": {
                "asr_candidates": [],
                "source": "KEYBOARD",
                "type": "TEXT"
            },
            "updates": "",
            "user_id": "88888"
        },
        "bot_id": "17037",
        "version": "2.0"
    }
    encoded_data = json.dumps(post_data).encode('utf-8')
    headers = {'Content-Type': 'application/json'}
    request = ul_re.Request(url, data=encoded_data, headers=headers)
    response = ul_re.urlopen(request)
    html = response.read()
    # data=json.loads(html)
    # data["action_list"][0]['say']
    jsonobj = json.loads(html)
    say = jsonpath.jsonpath(jsonobj, '$..say')
    bot_session = jsonpath.jsonpath(jsonobj, '$..bot_session')
    session_str = str(bot_session)
    index = session_str.find('session_id')
    index = index-1
    session_id = session_str[index:-5]
    return_session = str("{"+session_id+"}")
    # session_id=session_str[-46:-6]
    print(say)