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

json_config_file_list = []

commit_channel: int = 0

service_files = ["service1.service", "service2.service"]
service_health_channel = 0
status_file_with_message_id = "./tmp/message_id.txt"

server_admin_status_file = "/pathto/ServerAdminTools_Stats.json"
server_admin_status_file_2 = "/pathto/ServerAdminTools_Stats.json"
