class Log:
    
    
    def __init__(self, msg_log:str, hour_format: str = '', id: int = None) -> None:
        self.id = id
        self.msg_log = msg_log
        self.hour_format = hour_format
