def plugin_entrypoint(**kwargs):
    def inner(function):
        def wrapper(providedBus):
                function(providedBus)
                kwargs['register_tasks_callback']()
                return 1
        return wrapper
    return inner