# from .process.gpu_process.gpu_process import GPUProcess
from . import process
from . import load_balance
from ..utils.utils import Utils

class Server(object):
    def __init__(self):
        print(__name__)
        self.utils = Utils()

    def launch_gpu(self):
        # gpu_proc = GPUProcess()
        gpu_proc = process.gpu_process.GPUProcess()
        gpu_proc.run("from Server") 
        Utils.filename("server")
