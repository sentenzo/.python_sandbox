import json
from typing import Dict, List
from mock_web import Web


class ApiAlternative:
    base_url = "www.api_alter.com/api_v0_12"

    def __init__(self) -> None:
        self.token = ApiAlternative.authorize(ApiAlternative.get_api_key())

    @staticmethod
    def get_api_key(): return "CNDJYAX-BRRQBVD-JDA4XO4"

    @staticmethod
    def authorize(api_key: str) -> str:
        rez = Web.request(
            "POST", f"{ApiAlternative.base_url}/auth_post", {"credentials": api_key})
        rez = json.loads(rez["body"])
        return rez["token"]

    def getMessages_POST(self) -> List[any]:
        url_str = f"{ApiAlternative.base_url}/get_last_messages?amount=0"
        rez = Web.request(
            "POST", url_str, {"token": self.token})
        rez = json.loads(rez["body"])
        messages = rez["messages"]
        return messages