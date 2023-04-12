import enum

class ChatEvent(enum.Enum):
    ON_USER_CONNECT = 2
    ON_USER_DISCONNECT = 3
    ON_MESSAGE_RECEIVED = 4
    ON_USER_REGISTER = 5
    ON_USER_LOGIN = 6
    ON_CLIENT_CONNECT = 7