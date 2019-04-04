# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envelopewrapper.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import common_pb2 as common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='envelopewrapper.proto',
  package='proto',
  syntax='proto3',
  serialized_options=_b('\n\020bft.miguel.proto'),
  serialized_pb=_b('\n\x15\x65nvelopewrapper.proto\x12\x05proto\x1a\x0c\x63ommon.proto\"\xbe\x01\n\x0f\x45nvelopeWrapper\x12\x11\n\tchannelId\x18\x01 \x01(\t\x12\"\n\x08\x65nvelope\x18\x02 \x01(\x0b\x32\x10.common.Envelope\x12\x11\n\ttimestamp\x18\x03 \x01(\x03\x12\x39\n\x0c\x65nvelopeType\x18\x04 \x01(\x0e\x32#.proto.EnvelopeWrapper.EnvelopeType\"&\n\x0c\x45nvelopeType\x12\n\n\x06NORMAL\x10\x00\x12\n\n\x06\x43ONFIG\x10\x01\x42\x12\n\x10\x62\x66t.miguel.protob\x06proto3')
  ,
  dependencies=[common__pb2.DESCRIPTOR,])



_ENVELOPEWRAPPER_ENVELOPETYPE = _descriptor.EnumDescriptor(
  name='EnvelopeType',
  full_name='proto.EnvelopeWrapper.EnvelopeType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NORMAL', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONFIG', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=199,
  serialized_end=237,
)
_sym_db.RegisterEnumDescriptor(_ENVELOPEWRAPPER_ENVELOPETYPE)


_ENVELOPEWRAPPER = _descriptor.Descriptor(
  name='EnvelopeWrapper',
  full_name='proto.EnvelopeWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='channelId', full_name='proto.EnvelopeWrapper.channelId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='envelope', full_name='proto.EnvelopeWrapper.envelope', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='proto.EnvelopeWrapper.timestamp', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='envelopeType', full_name='proto.EnvelopeWrapper.envelopeType', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ENVELOPEWRAPPER_ENVELOPETYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=47,
  serialized_end=237,
)

_ENVELOPEWRAPPER.fields_by_name['envelope'].message_type = common__pb2._ENVELOPE
_ENVELOPEWRAPPER.fields_by_name['envelopeType'].enum_type = _ENVELOPEWRAPPER_ENVELOPETYPE
_ENVELOPEWRAPPER_ENVELOPETYPE.containing_type = _ENVELOPEWRAPPER
DESCRIPTOR.message_types_by_name['EnvelopeWrapper'] = _ENVELOPEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EnvelopeWrapper = _reflection.GeneratedProtocolMessageType('EnvelopeWrapper', (_message.Message,), dict(
  DESCRIPTOR = _ENVELOPEWRAPPER,
  __module__ = 'envelopewrapper_pb2'
  # @@protoc_insertion_point(class_scope:proto.EnvelopeWrapper)
  ))
_sym_db.RegisterMessage(EnvelopeWrapper)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
