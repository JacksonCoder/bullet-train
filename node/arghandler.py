import argparse

class Argstate:
    pass

def handleNodeArgs():
    a = Argstate()
    a.version = "0.1"
    a.dbpath = "/"
    return a