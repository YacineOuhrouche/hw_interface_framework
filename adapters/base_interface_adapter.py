# defines the shared adapter interface for all hardware interfaces


class BaseInterfaceAdapter:
    # stores the adapter name and connection state
    def __init__(self, name):
        self.name = name
        self.connected = False

    # connects to the interface adapter
    def connect(self):
        self.connected = True

    # disconnects from the interface adapter
    def disconnect(self):
        self.connected = False

    # returns true when the adapter is connected
    def is_connected(self):
        return self.connected

    # returns adapter information
    def get_info(self):
        return {
            "name": self.name,
            "connected": self.connected,
        }

    # raises an error when a method is not implemented
    def not_implemented(self, method_name):
        raise NotImplementedError(f"{method_name} is not implemented")