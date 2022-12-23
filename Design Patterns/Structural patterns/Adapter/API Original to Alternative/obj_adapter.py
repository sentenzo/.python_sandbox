from api_original import ApiOriginal as ApiO
from api_alternative import ApiAlternative as ApiA

class ObjAdapter(ApiO):
    def __init__(self) -> None:
        super().__init__()
        self.api_alt = ApiA()

    def getMessages_GET(self):
        messages = self.api_alt.getMessages_POST()

        def convert_alt_to_origin(message):
            return {"id": message["msg_id"]
, "text": f"Title: {message['title']}\n\nText:\n{message['msg']}"}

        for i in range(len(messages)):
            messages[i] = convert_alt_to_origin(messages[i])
        return messages