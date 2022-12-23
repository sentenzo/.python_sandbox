import json
from typing import Dict, List, Tuple
from mock_web import Web

class ApiOriginal:
    base_url = "www.api_original.com/api_root"

    def __init__(self) -> None:
        self.token = ApiOriginal.authorize(ApiOriginal.get_api_key())

    @staticmethod
    def get_api_key(): return "178635a23f82774"

    @staticmethod
    def authorize(api_key: str) -> str:
        rez = Web.request(
            "POST", f"{ApiOriginal.base_url}/authorize", {"api_key": api_key})
        rez = json.loads(rez["body"])
        return rez["token"]

    def getMessages_GET(self) -> List[any]:
        url_str = f"{ApiOriginal.base_url}/getMessages?token={self.token}"
        rez = Web.request("GET", url_str)
        rez = json.loads(rez["body"])
        messages = rez["messages"]
        return messages