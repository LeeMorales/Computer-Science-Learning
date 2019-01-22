import itchat
itchat.login()
def check_login(self, uuid=None):
    def get_contact(self, update=False):
        raise NotImplementedError()
    def get_friends(self, update=False):
        raise NotImplementedError()
    def get_chatrooms(self, update=False, contactOnly=False):
        raise NotImplementedError()
    def get_maps(self, update=False):
        raise NotADirectoryError()
    from  itchat.storage.templates import ContactList
    itchat.auto_login()
    print(itchat.get_contact())
    print(itchat.get_chatrooms())
    print(itchat.get_friends())
    print(itchat.get_mps())
    print(type(itchat.get_contact()))
    print(type(itchat.get_chatrooms()))
    print(type(itchat.get_friends()))
    print(type(itchat.get_mps()))    
    def logout(self):
        raise NotImplementedError()
