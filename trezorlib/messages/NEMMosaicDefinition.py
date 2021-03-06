# Automatically generated by pb2py
from .. import protobuf as p


class NEMMosaicDefinition(p.MessageType):
    FIELDS = {
        1: ('name', p.UnicodeType, 0),
        2: ('ticker', p.UnicodeType, 0),
        3: ('namespace', p.UnicodeType, 0),
        4: ('mosaic', p.UnicodeType, 0),
        5: ('divisibility', p.UVarintType, 0),
        6: ('levy', p.UVarintType, 0),
        7: ('fee', p.UVarintType, 0),
        8: ('levy_address', p.UnicodeType, 0),
        9: ('levy_namespace', p.UnicodeType, 0),
        10: ('levy_mosaic', p.UnicodeType, 0),
        11: ('supply', p.UVarintType, 0),
        12: ('mutable_supply', p.BoolType, 0),
        13: ('transferable', p.BoolType, 0),
        14: ('description', p.UnicodeType, 0),
        15: ('networks', p.UVarintType, p.FLAG_REPEATED),
    }
