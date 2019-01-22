import  itchat
import  time
itchat.auto_login()

user=itchat.search_friends(nickName="rong's")[0]
for i in range(10):
    itchat.send_msg(msg="我错了",toUserName=user['UserName'])
    time.sleep(0)
itchat.logout()