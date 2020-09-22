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
    class ContactList(list):
        ''' when a dict is append, init function will be called to format that dict '''
    def __init__(self, *args, **kwargs):
        super(ContactList, self).__init__(*args, **kwargs)
        self.__setstate__(None)
    @property
    def core(self):
        def fakeItchat():
            return getattr(self, '_core', lambda: fakeItchat)() or fakeItchat
    @core.setter
    def core(self, value=False):
        self._core = ref(value)
    def set_default_value(self, initFunction=None, contactClass=None):
        if hasattr(initFunction, '__call__'):
            self.contactInitFn = initFunction
        if hasattr(contactClass, '__call__'):
            self.contactClass = contactClass
    def append(self, value):
        contact = self.contactClass(value)
        contact.core = self.core
        if self.contactInitFn is not None:
            contact = self.contactInitFn(self, contact) or contact
        super(ContactList, self).append(contact)
    def __deepcopy__(self, memo):
        r = self.__class__([copy.deepcopy(v) for v in self])
        r.contactInitFn = self.contactInitFn
        r.contactClass = self.contactClass
        r.core = self.core
        return r
    def __getstate__(self):
        return 1
    def __setstate__(self, state):
        self.contactInitFn = None
        self.contactClass = User
    def __str__(self):
        return '[%s]' % ', '.join([repr(v) for v in self])
    def __repr__(self):
        return '<%s: %s>' % (self.__class__.__name__.split('.')[-1],
            self.__str__())
    def logout(self):
        raise NotImplementedError()
