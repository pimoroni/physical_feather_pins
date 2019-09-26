class PinNotAddressableError(Exception):
    def __init__(self, *args, **kwargs):
        default_message = "Pin is not addressable"

        if not (args or kwargs):
            args = (default_message, )
        
        super().__init__(*args, **kwargs)

class PinDoesNotExistError(Exception):
    def __init__(self, *args, **kwargs):
        default_message = "Pin does not exist"

        if not (args or kwargs):
            args = (default_message, )
        
        super().__init__(*args, **kwargs)