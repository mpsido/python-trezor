# Automatically generated by pb2py
from .. import protobuf as p


class DebugLinkDecision(p.MessageType):
    FIELDS = {
        1: ('yes_no', p.BoolType, 0),
        2: ('up_down', p.BoolType, 0),
        3: ('input', p.UnicodeType, 0),
    }
    MESSAGE_WIRE_TYPE = 100
