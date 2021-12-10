# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: livekit_analytics.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import enum_type_wrapper

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2

from . import livekit_internal_pb2 as livekit__internal__pb2
from . import livekit_models_pb2 as livekit__models__pb2

DESCRIPTOR = _descriptor.FileDescriptor(
    name="livekit_analytics.proto",
    package="livekit",
    syntax="proto3",
    serialized_options=b"Z#github.com/livekit/protocol/livekit",
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\x17livekit_analytics.proto\x12\x07livekit\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x14livekit_models.proto\x1a\x16livekit_internal.proto"\xdd\x02\n\rAnalyticsStat\x12\x15\n\ranalytics_key\x18\x01 \x01(\t\x12!\n\x04kind\x18\x02 \x01(\x0e\x32\x13.livekit.StreamType\x12.\n\ntime_stamp\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04node\x18\x04 \x01(\t\x12\x0f\n\x07room_id\x18\x05 \x01(\t\x12\x16\n\x0eparticipant_id\x18\x06 \x01(\t\x12\x0e\n\x06jitter\x18\x07 \x01(\x01\x12\x15\n\rtotal_packets\x18\x08 \x01(\x04\x12\x13\n\x0bpacket_lost\x18\t \x01(\x04\x12\r\n\x05\x64\x65lay\x18\n \x01(\x04\x12\x13\n\x0btotal_bytes\x18\x0b \x01(\x04\x12\x12\n\nnack_count\x18\x0c \x01(\x05\x12\x11\n\tpli_count\x18\r \x01(\x05\x12\x11\n\tfir_count\x18\x0e \x01(\x05\x12\x11\n\troom_name\x18\x0f \x01(\t"7\n\x0e\x41nalyticsStats\x12%\n\x05stats\x18\x01 \x03(\x0b\x32\x16.livekit.AnalyticsStat"\xfd\x02\n\x0e\x41nalyticsEvent\x12)\n\x04type\x18\x01 \x01(\x0e\x32\x1b.livekit.AnalyticsEventType\x12-\n\ttimestamp\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x10\n\x08room_sid\x18\x03 \x01(\t\x12\x1b\n\x04room\x18\x04 \x01(\x0b\x32\r.livekit.Room\x12\x16\n\x0eparticipant_id\x18\x05 \x01(\t\x12-\n\x0bparticipant\x18\x06 \x01(\x0b\x32\x18.livekit.ParticipantInfo\x12\x10\n\x08track_id\x18\x07 \x01(\t\x12!\n\x05track\x18\x08 \x01(\x0b\x32\x12.livekit.TrackInfo\x12\x14\n\x0crecording_id\x18\t \x01(\t\x12\x15\n\ranalytics_key\x18\n \x01(\t\x12)\n\x08sdk_type\x18\x0b \x01(\x0e\x32\x17.livekit.ClientInfo.SDK\x12\x0e\n\x06region\x18\x0c \x01(\t":\n\x0f\x41nalyticsEvents\x12\'\n\x06\x65vents\x18\x01 \x03(\x0b\x32\x17.livekit.AnalyticsEvent**\n\nStreamType\x12\x0c\n\x08UPSTREAM\x10\x00\x12\x0e\n\nDOWNSTREAM\x10\x01*\xea\x01\n\x12\x41nalyticsEventType\x12\x10\n\x0cROOM_CREATED\x10\x00\x12\x0e\n\nROOM_ENDED\x10\x01\x12\x16\n\x12PARTICIPANT_JOINED\x10\x02\x12\x14\n\x10PARTICIPANT_LEFT\x10\x03\x12\x13\n\x0fTRACK_PUBLISHED\x10\x04\x12\x15\n\x11TRACK_UNPUBLISHED\x10\x05\x12\x14\n\x10TRACK_SUBSCRIBED\x10\x06\x12\x16\n\x12TRACK_UNSUBSCRIBED\x10\x07\x12\x15\n\x11RECORDING_STARTED\x10\x08\x12\x13\n\x0fRECORDING_ENDED\x10\t2\xa4\x01\n\x18\x41nalyticsRecorderService\x12\x42\n\x0bIngestStats\x12\x17.livekit.AnalyticsStats\x1a\x16.google.protobuf.Empty"\x00(\x01\x12\x44\n\x0cIngestEvents\x12\x18.livekit.AnalyticsEvents\x1a\x16.google.protobuf.Empty"\x00(\x01\x42%Z#github.com/livekit/protocol/livekitb\x06proto3',
    dependencies=[
        google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,
        google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,
        livekit__models__pb2.DESCRIPTOR,
        livekit__internal__pb2.DESCRIPTOR,
    ],
)

_STREAMTYPE = _descriptor.EnumDescriptor(
    name="StreamType",
    full_name="livekit.StreamType",
    filename=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
    values=[
        _descriptor.EnumValueDescriptor(
            name="UPSTREAM",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="DOWNSTREAM",
            index=1,
            number=1,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=997,
    serialized_end=1039,
)
_sym_db.RegisterEnumDescriptor(_STREAMTYPE)

StreamType = enum_type_wrapper.EnumTypeWrapper(_STREAMTYPE)
_ANALYTICSEVENTTYPE = _descriptor.EnumDescriptor(
    name="AnalyticsEventType",
    full_name="livekit.AnalyticsEventType",
    filename=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
    values=[
        _descriptor.EnumValueDescriptor(
            name="ROOM_CREATED",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="ROOM_ENDED",
            index=1,
            number=1,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="PARTICIPANT_JOINED",
            index=2,
            number=2,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="PARTICIPANT_LEFT",
            index=3,
            number=3,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="TRACK_PUBLISHED",
            index=4,
            number=4,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="TRACK_UNPUBLISHED",
            index=5,
            number=5,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="TRACK_SUBSCRIBED",
            index=6,
            number=6,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="TRACK_UNSUBSCRIBED",
            index=7,
            number=7,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="RECORDING_STARTED",
            index=8,
            number=8,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="RECORDING_ENDED",
            index=9,
            number=9,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=1042,
    serialized_end=1276,
)
_sym_db.RegisterEnumDescriptor(_ANALYTICSEVENTTYPE)

AnalyticsEventType = enum_type_wrapper.EnumTypeWrapper(_ANALYTICSEVENTTYPE)
UPSTREAM = 0
DOWNSTREAM = 1
ROOM_CREATED = 0
ROOM_ENDED = 1
PARTICIPANT_JOINED = 2
PARTICIPANT_LEFT = 3
TRACK_PUBLISHED = 4
TRACK_UNPUBLISHED = 5
TRACK_SUBSCRIBED = 6
TRACK_UNSUBSCRIBED = 7
RECORDING_STARTED = 8
RECORDING_ENDED = 9


_ANALYTICSSTAT = _descriptor.Descriptor(
    name="AnalyticsStat",
    full_name="livekit.AnalyticsStat",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="analytics_key",
            full_name="livekit.AnalyticsStat.analytics_key",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="kind",
            full_name="livekit.AnalyticsStat.kind",
            index=1,
            number=2,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="time_stamp",
            full_name="livekit.AnalyticsStat.time_stamp",
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="node",
            full_name="livekit.AnalyticsStat.node",
            index=3,
            number=4,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="room_id",
            full_name="livekit.AnalyticsStat.room_id",
            index=4,
            number=5,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="participant_id",
            full_name="livekit.AnalyticsStat.participant_id",
            index=5,
            number=6,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="jitter",
            full_name="livekit.AnalyticsStat.jitter",
            index=6,
            number=7,
            type=1,
            cpp_type=5,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="total_packets",
            full_name="livekit.AnalyticsStat.total_packets",
            index=7,
            number=8,
            type=4,
            cpp_type=4,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="packet_lost",
            full_name="livekit.AnalyticsStat.packet_lost",
            index=8,
            number=9,
            type=4,
            cpp_type=4,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="delay",
            full_name="livekit.AnalyticsStat.delay",
            index=9,
            number=10,
            type=4,
            cpp_type=4,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="total_bytes",
            full_name="livekit.AnalyticsStat.total_bytes",
            index=10,
            number=11,
            type=4,
            cpp_type=4,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="nack_count",
            full_name="livekit.AnalyticsStat.nack_count",
            index=11,
            number=12,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="pli_count",
            full_name="livekit.AnalyticsStat.pli_count",
            index=12,
            number=13,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="fir_count",
            full_name="livekit.AnalyticsStat.fir_count",
            index=13,
            number=14,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="room_name",
            full_name="livekit.AnalyticsStat.room_name",
            index=14,
            number=15,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=145,
    serialized_end=494,
)


_ANALYTICSSTATS = _descriptor.Descriptor(
    name="AnalyticsStats",
    full_name="livekit.AnalyticsStats",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="stats",
            full_name="livekit.AnalyticsStats.stats",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=496,
    serialized_end=551,
)


_ANALYTICSEVENT = _descriptor.Descriptor(
    name="AnalyticsEvent",
    full_name="livekit.AnalyticsEvent",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="type",
            full_name="livekit.AnalyticsEvent.type",
            index=0,
            number=1,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="timestamp",
            full_name="livekit.AnalyticsEvent.timestamp",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="room_sid",
            full_name="livekit.AnalyticsEvent.room_sid",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="room",
            full_name="livekit.AnalyticsEvent.room",
            index=3,
            number=4,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="participant_id",
            full_name="livekit.AnalyticsEvent.participant_id",
            index=4,
            number=5,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="participant",
            full_name="livekit.AnalyticsEvent.participant",
            index=5,
            number=6,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="track_id",
            full_name="livekit.AnalyticsEvent.track_id",
            index=6,
            number=7,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="track",
            full_name="livekit.AnalyticsEvent.track",
            index=7,
            number=8,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="recording_id",
            full_name="livekit.AnalyticsEvent.recording_id",
            index=8,
            number=9,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="analytics_key",
            full_name="livekit.AnalyticsEvent.analytics_key",
            index=9,
            number=10,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="sdk_type",
            full_name="livekit.AnalyticsEvent.sdk_type",
            index=10,
            number=11,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="region",
            full_name="livekit.AnalyticsEvent.region",
            index=11,
            number=12,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=554,
    serialized_end=935,
)


_ANALYTICSEVENTS = _descriptor.Descriptor(
    name="AnalyticsEvents",
    full_name="livekit.AnalyticsEvents",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="events",
            full_name="livekit.AnalyticsEvents.events",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=937,
    serialized_end=995,
)

_ANALYTICSSTAT.fields_by_name["kind"].enum_type = _STREAMTYPE
_ANALYTICSSTAT.fields_by_name[
    "time_stamp"
].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_ANALYTICSSTATS.fields_by_name["stats"].message_type = _ANALYTICSSTAT
_ANALYTICSEVENT.fields_by_name["type"].enum_type = _ANALYTICSEVENTTYPE
_ANALYTICSEVENT.fields_by_name[
    "timestamp"
].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_ANALYTICSEVENT.fields_by_name["room"].message_type = livekit__models__pb2._ROOM
_ANALYTICSEVENT.fields_by_name[
    "participant"
].message_type = livekit__models__pb2._PARTICIPANTINFO
_ANALYTICSEVENT.fields_by_name["track"].message_type = livekit__models__pb2._TRACKINFO
_ANALYTICSEVENT.fields_by_name[
    "sdk_type"
].enum_type = livekit__internal__pb2._CLIENTINFO_SDK
_ANALYTICSEVENTS.fields_by_name["events"].message_type = _ANALYTICSEVENT
DESCRIPTOR.message_types_by_name["AnalyticsStat"] = _ANALYTICSSTAT
DESCRIPTOR.message_types_by_name["AnalyticsStats"] = _ANALYTICSSTATS
DESCRIPTOR.message_types_by_name["AnalyticsEvent"] = _ANALYTICSEVENT
DESCRIPTOR.message_types_by_name["AnalyticsEvents"] = _ANALYTICSEVENTS
DESCRIPTOR.enum_types_by_name["StreamType"] = _STREAMTYPE
DESCRIPTOR.enum_types_by_name["AnalyticsEventType"] = _ANALYTICSEVENTTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AnalyticsStat = _reflection.GeneratedProtocolMessageType(
    "AnalyticsStat",
    (_message.Message,),
    {
        "DESCRIPTOR": _ANALYTICSSTAT,
        "__module__": "livekit_analytics_pb2"
        # @@protoc_insertion_point(class_scope:livekit.AnalyticsStat)
    },
)
_sym_db.RegisterMessage(AnalyticsStat)

AnalyticsStats = _reflection.GeneratedProtocolMessageType(
    "AnalyticsStats",
    (_message.Message,),
    {
        "DESCRIPTOR": _ANALYTICSSTATS,
        "__module__": "livekit_analytics_pb2"
        # @@protoc_insertion_point(class_scope:livekit.AnalyticsStats)
    },
)
_sym_db.RegisterMessage(AnalyticsStats)

AnalyticsEvent = _reflection.GeneratedProtocolMessageType(
    "AnalyticsEvent",
    (_message.Message,),
    {
        "DESCRIPTOR": _ANALYTICSEVENT,
        "__module__": "livekit_analytics_pb2"
        # @@protoc_insertion_point(class_scope:livekit.AnalyticsEvent)
    },
)
_sym_db.RegisterMessage(AnalyticsEvent)

AnalyticsEvents = _reflection.GeneratedProtocolMessageType(
    "AnalyticsEvents",
    (_message.Message,),
    {
        "DESCRIPTOR": _ANALYTICSEVENTS,
        "__module__": "livekit_analytics_pb2"
        # @@protoc_insertion_point(class_scope:livekit.AnalyticsEvents)
    },
)
_sym_db.RegisterMessage(AnalyticsEvents)


DESCRIPTOR._options = None

_ANALYTICSRECORDERSERVICE = _descriptor.ServiceDescriptor(
    name="AnalyticsRecorderService",
    full_name="livekit.AnalyticsRecorderService",
    file=DESCRIPTOR,
    index=0,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_start=1279,
    serialized_end=1443,
    methods=[
        _descriptor.MethodDescriptor(
            name="IngestStats",
            full_name="livekit.AnalyticsRecorderService.IngestStats",
            index=0,
            containing_service=None,
            input_type=_ANALYTICSSTATS,
            output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="IngestEvents",
            full_name="livekit.AnalyticsRecorderService.IngestEvents",
            index=1,
            containing_service=None,
            input_type=_ANALYTICSEVENTS,
            output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
)
_sym_db.RegisterServiceDescriptor(_ANALYTICSRECORDERSERVICE)

DESCRIPTOR.services_by_name["AnalyticsRecorderService"] = _ANALYTICSRECORDERSERVICE

# @@protoc_insertion_point(module_scope)
