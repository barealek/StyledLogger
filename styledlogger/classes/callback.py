class Callback:
    """
    A callback that can be added to a logger. The callback will be called with the logger name as the first argument and message as the second argument.

    :param name:
    The name of the callback. This is used to identify the callback.

    :param activation_level:
    The level at which the callback will be called. 0 = debug, 1 = info, 2 = warn, 3 = error, 4 = fatal. All prints lower than the level will be ignored.

    :param callback:
    The callback function. This will be called with the logger name as the first argument, the level as the second and message as the third argument.
    """

    def __init__(self, name: str, activation_levels: tuple, callback: callable):
        self.name = name
        self.activation_levels = activation_levels
        self.callback = callback

    def run_callback(self, level, message):
        self.callback(self.name, level, message)

    def __repr__(self):
        return f"<Callback name={self.name} activation_levels={self.activation_levels} callback={self.callback}>"

    def __str__(self):
        return self.__repr__()
