from eventbus.event import Event

class EventBus:
    
    def __init__(self):
        self.__is_running = False
        self.__map_event_to_task = {
            Event.ON_START : [],
            Event.ON_STOP : []
        }
    
    def register_task(self, event, function):
        self.__map_event_to_task[event].append(function)

    def start(self):
        if self.__is_running == False:
            for callable in self.__map_event_to_task[Event.ON_START]:
                callable()

    def stop(self):
        if self.__is_running == True:
            for callable in self.__map_event_to_task[Event.ON_START]:
                callable()
    
    def fire_event(self, event):
        for callable in self.__map_event_to_task[event]:
            callable()