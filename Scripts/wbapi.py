import requests
class Client():
    def __init__(self) -> None:
        super().__init__()
        self.avatarurl = ""
    def Login(self,url):
        self.wburl = url
    def SetUsername(self,username):
        if username:
            self.username = username
        else:
            self.username = ""
    def SetAvatar(self,avatar):
        if avatar:
            self.avatarurl = avatar
        else:
            self.avatarurl = ""
    def Send(self,message):
        WebHookR = {
            "content":message,
            "username":self.username,
            "avatar_url":self.avatarurl
        }
        r = requests.post(self.wburl,json=WebHookR)
        return r.status_code