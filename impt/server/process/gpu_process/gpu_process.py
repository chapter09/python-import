from .. import Utils

class GPUProcess(object):
    def __init__(self):
        print(__name__)
    
    def run(self, name):
        print("run " + name)
        Utils.filename("from GPUProcess class")
