import pymem.process
from pymem import Pymem


class ModuleInfo:
    def __init__(self, handle: pymem.Pymem):
        self.handle = handle

        # client.dll
        self.client = pymem.process.module_from_name(handle.process_handle, "client.dll")
        self.client_base = self.client.lpBaseOfDll
        self.client_module = handle.read_bytes(self.client_base, self.client.SizeOfImage)
        # server.dll
        self.server = pymem.process.module_from_name(handle.process_handle, "server.dll")
        self.server_base = self.server.lpBaseOfDll
        self.server_module = handle.read_bytes(self.server_base, self.server.SizeOfImage)
        # engine.dll
        self.engine = pymem.process.module_from_name(handle.process_handle, "engine.dll")
        self.engine_base = self.engine.lpBaseOfDll
        self.engine_module = handle.read_bytes(self.engine_base, self.engine.SizeOfImage)

