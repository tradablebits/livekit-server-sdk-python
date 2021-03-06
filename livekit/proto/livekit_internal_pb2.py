# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: livekit_internal.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import livekit_models_pb2 as livekit__models__pb2
from . import livekit_recording_pb2 as livekit__recording__pb2
from . import livekit_room_pb2 as livekit__room__pb2
from . import livekit_rtc_pb2 as livekit__rtc__pb2

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x16livekit_internal.proto\x12\x07livekit\x1a\x14livekit_models.proto\x1a\x17livekit_recording.proto\x1a\x11livekit_rtc.proto\x1a\x12livekit_room.proto"\xa7\x01\n\x04Node\x12\n\n\x02id\x18\x01 \x01(\t\x12\n\n\x02ip\x18\x02 \x01(\t\x12\x10\n\x08num_cpus\x18\x03 \x01(\r\x12!\n\x05stats\x18\x04 \x01(\x0b\x32\x12.livekit.NodeStats\x12\x1f\n\x04type\x18\x05 \x01(\x0e\x32\x11.livekit.NodeType\x12!\n\x05state\x18\x06 \x01(\x0e\x32\x12.livekit.NodeState\x12\x0e\n\x06region\x18\x07 \x01(\t"\xe6\x03\n\tNodeStats\x12\x12\n\nstarted_at\x18\x01 \x01(\x03\x12\x12\n\nupdated_at\x18\x02 \x01(\x03\x12\x11\n\tnum_rooms\x18\x03 \x01(\x05\x12\x13\n\x0bnum_clients\x18\x04 \x01(\x05\x12\x15\n\rnum_tracks_in\x18\x05 \x01(\x05\x12\x16\n\x0enum_tracks_out\x18\x06 \x01(\x05\x12\x10\n\x08\x62ytes_in\x18\x07 \x01(\x04\x12\x11\n\tbytes_out\x18\x08 \x01(\x04\x12\x12\n\npackets_in\x18\t \x01(\x04\x12\x13\n\x0bpackets_out\x18\n \x01(\x04\x12\x12\n\nnack_total\x18\x0b \x01(\x04\x12\x18\n\x10\x62ytes_in_per_sec\x18\x0c \x01(\x02\x12\x19\n\x11\x62ytes_out_per_sec\x18\r \x01(\x02\x12\x1a\n\x12packets_in_per_sec\x18\x0e \x01(\x02\x12\x1b\n\x13packets_out_per_sec\x18\x0f \x01(\x02\x12\x14\n\x0cnack_per_sec\x18\x10 \x01(\x02\x12\x10\n\x08num_cpus\x18\x11 \x01(\r\x12\x19\n\x11load_avg_last1min\x18\x12 \x01(\x02\x12\x19\n\x11load_avg_last5min\x18\x13 \x01(\x02\x12\x1a\n\x12load_avg_last15min\x18\x14 \x01(\x02\x12\x10\n\x08\x63pu_load\x18\x15 \x01(\x02"\xef\x04\n\x0eRTCNodeMessage\x12\x17\n\x0fparticipant_key\x18\x01 \x01(\t\x12\x13\n\x0bsender_time\x18\x0b \x01(\x03\x12.\n\rstart_session\x18\x02 \x01(\x0b\x32\x15.livekit.StartSessionH\x00\x12)\n\x07request\x18\x03 \x01(\x0b\x32\x16.livekit.SignalRequestH\x00\x12>\n\x12remove_participant\x18\x04 \x01(\x0b\x32 .livekit.RoomParticipantIdentityH\x00\x12\x33\n\nmute_track\x18\x05 \x01(\x0b\x32\x1d.livekit.MuteRoomTrackRequestH\x00\x12?\n\x12update_participant\x18\x06 \x01(\x0b\x32!.livekit.UpdateParticipantRequestH\x00\x12\x31\n\x0b\x64\x65lete_room\x18\x07 \x01(\x0b\x32\x1a.livekit.DeleteRoomRequestH\x00\x12\x43\n\x14update_subscriptions\x18\x08 \x01(\x0b\x32#.livekit.UpdateSubscriptionsRequestH\x00\x12-\n\tsend_data\x18\t \x01(\x0b\x32\x18.livekit.SendDataRequestH\x00\x12\x42\n\x14update_room_metadata\x18\n \x01(\x0b\x32".livekit.UpdateRoomMetadataRequestH\x00\x12(\n\nkeep_alive\x18\x0c \x01(\x0b\x32\x12.livekit.KeepAliveH\x00\x42\t\n\x07message"\x8e\x01\n\x11SignalNodeMessage\x12\x15\n\rconnection_id\x18\x01 \x01(\t\x12+\n\x08response\x18\x02 \x01(\x0b\x32\x17.livekit.SignalResponseH\x00\x12*\n\x0b\x65nd_session\x18\x03 \x01(\x0b\x32\x13.livekit.EndSessionH\x00\x42\t\n\x07message"\xf8\x01\n\x0cStartSession\x12\x11\n\troom_name\x18\x01 \x01(\t\x12\x10\n\x08identity\x18\x02 \x01(\t\x12\x15\n\rconnection_id\x18\x03 \x01(\t\x12\x11\n\treconnect\x18\x04 \x01(\x08\x12\x16\n\x0e\x61uto_subscribe\x18\t \x01(\x08\x12\x0e\n\x06hidden\x18\n \x01(\x08\x12#\n\x06\x63lient\x18\x0b \x01(\x0b\x32\x13.livekit.ClientInfo\x12\x10\n\x08recorder\x18\x0c \x01(\x08\x12\x0c\n\x04name\x18\r \x01(\t\x12\x13\n\x0bgrants_json\x18\x0e \x01(\t\x12\x17\n\x0f\x61\x64\x61ptive_stream\x18\x0f \x01(\x08"\x0c\n\nEndSession"+\n\x11RemoveParticipant\x12\x16\n\x0eparticipant_id\x18\x01 \x01(\t"8\n\x14RecordingReservation\x12\n\n\x02id\x18\x01 \x01(\t\x12\x14\n\x0csubmitted_at\x18\x02 \x01(\x03"\xf7\x01\n\x10RecordingRequest\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x12/\n\x05start\x18\x02 \x01(\x0b\x32\x1e.livekit.StartRecordingRequestH\x00\x12/\n\nadd_output\x18\x03 \x01(\x0b\x32\x19.livekit.AddOutputRequestH\x00\x12\x35\n\rremove_output\x18\x04 \x01(\x0b\x32\x1c.livekit.RemoveOutputRequestH\x00\x12+\n\x03\x65nd\x18\x05 \x01(\x0b\x32\x1c.livekit.EndRecordingRequestH\x00\x42\t\n\x07request"6\n\x11RecordingResponse\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x12\r\n\x05\x65rror\x18\x02 \x01(\t"\x0b\n\tKeepAlive*;\n\x08NodeType\x12\n\n\x06SERVER\x10\x00\x12\x0e\n\nCONTROLLER\x10\x01\x12\t\n\x05MEDIA\x10\x02\x12\x08\n\x04TURN\x10\x04*<\n\tNodeState\x12\x0f\n\x0bSTARTING_UP\x10\x00\x12\x0b\n\x07SERVING\x10\x01\x12\x11\n\rSHUTTING_DOWN\x10\x02\x42\x46Z#github.com/livekit/protocol/livekit\xaa\x02\rLiveKit.Proto\xea\x02\x0eLiveKit::Protob\x06proto3'
)

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "livekit_internal_pb2", globals())
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b"Z#github.com/livekit/protocol/livekit\252\002\rLiveKit.Proto\352\002\016LiveKit::Proto"
    _NODETYPE._serialized_start = 2238
    _NODETYPE._serialized_end = 2297
    _NODESTATE._serialized_start = 2299
    _NODESTATE._serialized_end = 2359
    _NODE._serialized_start = 122
    _NODE._serialized_end = 289
    _NODESTATS._serialized_start = 292
    _NODESTATS._serialized_end = 778
    _RTCNODEMESSAGE._serialized_start = 781
    _RTCNODEMESSAGE._serialized_end = 1404
    _SIGNALNODEMESSAGE._serialized_start = 1407
    _SIGNALNODEMESSAGE._serialized_end = 1549
    _STARTSESSION._serialized_start = 1552
    _STARTSESSION._serialized_end = 1800
    _ENDSESSION._serialized_start = 1802
    _ENDSESSION._serialized_end = 1814
    _REMOVEPARTICIPANT._serialized_start = 1816
    _REMOVEPARTICIPANT._serialized_end = 1859
    _RECORDINGRESERVATION._serialized_start = 1861
    _RECORDINGRESERVATION._serialized_end = 1917
    _RECORDINGREQUEST._serialized_start = 1920
    _RECORDINGREQUEST._serialized_end = 2167
    _RECORDINGRESPONSE._serialized_start = 2169
    _RECORDINGRESPONSE._serialized_end = 2223
    _KEEPALIVE._serialized_start = 2225
    _KEEPALIVE._serialized_end = 2236
# @@protoc_insertion_point(module_scope)
