from ansibledocgen.parser.playbook import PlaybookParser

class RoleParser(object):
    def __init__(self, rolepath):
        self.rolepath = rolepath
        # TESTING FOR NOW
        print(self.rolepath)
