# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: calculator.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10\x63\x61lculator.proto\"\"\n\nSumRequest\x12\t\n\x01\x61\x18\x01 \x01(\x01\x12\t\n\x01\x62\x18\x02 \x01(\x01\"\x15\n\x08SumReply\x12\t\n\x01s\x18\x01 \x01(\x01\"#\n\x0bMultRequest\x12\t\n\x01\x61\x18\x01 \x01(\x01\x12\t\n\x01\x62\x18\x02 \x01(\x01\"\x16\n\tMultReply\x12\t\n\x01p\x18\x01 \x01(\x01\"2\n\x0fGreatestRequest\x12\t\n\x01\x61\x18\x01 \x01(\x01\x12\t\n\x01\x62\x18\x02 \x01(\x01\x12\t\n\x01\x63\x18\x03 \x01(\x01\"\x1a\n\rGreatestReply\x12\t\n\x01g\x18\x01 \x01(\x01\"\"\n\nDivRequest\x12\t\n\x01\x61\x18\x01 \x01(\x01\x12\t\n\x01\x62\x18\x02 \x01(\x01\" \n\x08\x44ivReply\x12\t\n\x01q\x18\x01 \x01(\x01\x12\t\n\x01r\x18\x02 \x01(\x01\x32\x9a\x01\n\nCalculator\x12\x1d\n\x03Sum\x12\x0b.SumRequest\x1a\t.SumReply\x12 \n\x04Mult\x12\x0c.MultRequest\x1a\n.MultReply\x12,\n\x08Greatest\x12\x10.GreatestRequest\x1a\x0e.GreatestReply\x12\x1d\n\x03\x44iv\x12\x0b.DivRequest\x1a\t.DivReplyb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'calculator_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_SUMREQUEST']._serialized_start=20
  _globals['_SUMREQUEST']._serialized_end=54
  _globals['_SUMREPLY']._serialized_start=56
  _globals['_SUMREPLY']._serialized_end=77
  _globals['_MULTREQUEST']._serialized_start=79
  _globals['_MULTREQUEST']._serialized_end=114
  _globals['_MULTREPLY']._serialized_start=116
  _globals['_MULTREPLY']._serialized_end=138
  _globals['_GREATESTREQUEST']._serialized_start=140
  _globals['_GREATESTREQUEST']._serialized_end=190
  _globals['_GREATESTREPLY']._serialized_start=192
  _globals['_GREATESTREPLY']._serialized_end=218
  _globals['_DIVREQUEST']._serialized_start=220
  _globals['_DIVREQUEST']._serialized_end=254
  _globals['_DIVREPLY']._serialized_start=256
  _globals['_DIVREPLY']._serialized_end=288
  _globals['_CALCULATOR']._serialized_start=291
  _globals['_CALCULATOR']._serialized_end=445
# @@protoc_insertion_point(module_scope)
