import json
from typing import Dict

class Web:
    @staticmethod
    def request(method, url, vals=None) -> Dict[str, any]:
        if url.endswith("/authorize"):
            ret = {"code": 200,
                   "body": '{"token": "12345", "api_key": "' + vals["api_key"] + '"}'}
        elif url.endswith("/auth_post"):
            ret = {"code": 200, "body": '{"token": "12345", "credentials": "' +
                   vals["credentials"] + '"}'}
        else:
            ans = {"method": method, "url": url}
            if vals:
                ans["parameters"] = vals
            if url.find("/get_last_messages?") >= 0:
                ans["messages"] = [
                    {"msg_id": id(i), "title": f"msg title from alt {i}", "msg": f"msg body from alt {i}"
                     }
                    for i in range(1, 6)]
            elif url.find("/getMessages?") >= 0:
                ans["messages"] = [
                    {"id": i, "text": f"some text from original {i}"} for i in range(1, 6)]
            ret = {"code": 200, "body": json.dumps(ans, indent=4)}

        print(ret)
        print("------")
        return ret