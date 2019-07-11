import  itchat
import  time
itchat.auto_login()
user=itchat.search_friends(nickName="蝶恋花")[0]
for i in range(1000):
    itchat.send_msg(msg="You were being hacked",toUserName=user['UserName'])
    time.sleep(1)
itchat.logout()