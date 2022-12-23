from api_original import ApiOriginal as ApiO
from api_alternative import ApiAlternative as ApiA

class ClsAdapter(ApiA, ApiO):  # the inheritance order is important
    def getMessages_GET(self):
        def convert_alt_to_origin(message):
            return {"id": message["msg_id"]
, "text": f"Title: {message['title']}\n\nText:\n{message['msg']}"}

        messages = self.getMessages_POST()

        for i in range(len(messages)):
            messages[i] = convert_alt_to_origin(messages[i])
        return messages