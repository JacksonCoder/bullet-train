class Node:
    def __init__(self,argstate):
        self.version = argstate.version
        self.dbpath = argstate.dbpath
    def Run(self):
        print("Running")
    def Exit(self):
        print("Exiting")
        pass