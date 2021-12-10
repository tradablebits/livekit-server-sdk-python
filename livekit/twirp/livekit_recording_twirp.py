# -*- coding: utf-8 -*-
# Generated by https://github.com/verloop/twirpy/protoc-gen-twirpy.  DO NOT EDIT!
# source: livekit_recording.proto

from google.protobuf import symbol_database as _symbol_database
from twirp.base import Endpoint
from twirp.client import TwirpClient
from twirp.server import TwirpServer

_sym_db = _symbol_database.Default()


class RecordingServiceServer(TwirpServer):
    def __init__(self, *args, service, server_path_prefix="/twirp"):
        super().__init__(service=service)
        self._prefix = f"{server_path_prefix}/livekit.RecordingService"
        self._endpoints = {
            "StartRecording": Endpoint(
                service_name="RecordingService",
                name="StartRecording",
                function=getattr(service, "StartRecording"),
                input=_sym_db.GetSymbol("livekit.StartRecordingRequest"),
                output=_sym_db.GetSymbol("livekit.StartRecordingResponse"),
            ),
            "AddOutput": Endpoint(
                service_name="RecordingService",
                name="AddOutput",
                function=getattr(service, "AddOutput"),
                input=_sym_db.GetSymbol("livekit.AddOutputRequest"),
                output=_sym_db.GetSymbol("google.protobuf.Empty"),
            ),
            "RemoveOutput": Endpoint(
                service_name="RecordingService",
                name="RemoveOutput",
                function=getattr(service, "RemoveOutput"),
                input=_sym_db.GetSymbol("livekit.RemoveOutputRequest"),
                output=_sym_db.GetSymbol("google.protobuf.Empty"),
            ),
            "EndRecording": Endpoint(
                service_name="RecordingService",
                name="EndRecording",
                function=getattr(service, "EndRecording"),
                input=_sym_db.GetSymbol("livekit.EndRecordingRequest"),
                output=_sym_db.GetSymbol("google.protobuf.Empty"),
            ),
        }


class RecordingServiceClient(TwirpClient):
    def StartRecording(
        self, *args, ctx, request, server_path_prefix="/twirp", **kwargs
    ):
        return self._make_request(
            url=f"{server_path_prefix}/livekit.RecordingService/StartRecording",
            ctx=ctx,
            request=request,
            response_obj=_sym_db.GetSymbol("livekit.StartRecordingResponse"),
            **kwargs,
        )

    def AddOutput(self, *args, ctx, request, server_path_prefix="/twirp", **kwargs):
        return self._make_request(
            url=f"{server_path_prefix}/livekit.RecordingService/AddOutput",
            ctx=ctx,
            request=request,
            response_obj=_sym_db.GetSymbol("google.protobuf.Empty"),
            **kwargs,
        )

    def RemoveOutput(self, *args, ctx, request, server_path_prefix="/twirp", **kwargs):
        return self._make_request(
            url=f"{server_path_prefix}/livekit.RecordingService/RemoveOutput",
            ctx=ctx,
            request=request,
            response_obj=_sym_db.GetSymbol("google.protobuf.Empty"),
            **kwargs,
        )

    def EndRecording(self, *args, ctx, request, server_path_prefix="/twirp", **kwargs):
        return self._make_request(
            url=f"{server_path_prefix}/livekit.RecordingService/EndRecording",
            ctx=ctx,
            request=request,
            response_obj=_sym_db.GetSymbol("google.protobuf.Empty"),
            **kwargs,
        )
