import firebase_admin
from firebase_admin import credentials, db

class PyFirebase:
    def __init__(self, path, url):
        cred = credentials.Certificate(path)
        firebase_admin.initialize_app(
            cred,
            {'databaseURL' : url}
        )
        self.pathdata = {}

    def CreatePath(self, path):
        if not path in self.pathdata.keys():
            self.pathdata[path] = db.reference(path) if path != '' else db.reference()

    def Update(self, path, data):
        try:
            self.pathdata[''].update({path: data})
        except:
            self.CreatePath('')
            self.Update(path, data)

    def GetValue(self, path):
        try:
            return self.pathdata[path].get()
        except:
            self.CreatePath(path)
            self.GetValue(path)

    def AddListener(self, path, listener):
        try:
            self.pathdata[path].listen(listener)
        except:
            self.CreatePath(path)
            self.AddListener(path, listener)
