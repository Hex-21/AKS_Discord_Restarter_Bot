from dotenv import load_dotenv
from os import getenv

load_dotenv(".env")
TOKEN: str = getenv("Token")
whitelist = {
    "example discord Name": 0
}

aks1serverimage = ""
aks2serverimage = ""
aks3serverimage = ""
aks4serverimage = ""
aks5serverimage = ""
aks6backupimage = ""

aks1chatfilepath = ""
aks2chatfilepath = ""
aks3chatfilepath = ""
aks4chatfilepath = ""
aks5chatfilepath = ""

sessionsavepath1 = ""
sessionsavepath2 = ""
sessionsavepath3 = ""
sessionsavepath4 = ""
sessionsavepath5 = ""

forwardchattodiscordchannelchatid: int = 0

aksconfigpath = ""
