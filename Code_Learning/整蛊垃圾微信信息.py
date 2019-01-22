import  itchat
import  time
itchat.auto_login()

user=itchat.search_friends(nickName="PureBlue_恒")[0]
for i in range(10):
    itchat.send_msg(msg="You were being hacked",toUserName=user['UserName'])
    time.sleep(0)
itchat.logout()