# Copyright 2016 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: windmill_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import windmill_pb2 as windmill__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='windmill_service.proto',
  package='google.dataflow.windmillservice.v1alpha1',
  syntax='proto2',
  serialized_pb=_b('\n\x16windmill_service.proto\x12(google.dataflow.windmillservice.v1alpha1\x1a\x0ewindmill.proto2\xf9\x02\n\x1c\x43loudWindmillServiceV1Alpha1\x12>\n\x07GetWork\x12\x18.windmill.GetWorkRequest\x1a\x19.windmill.GetWorkResponse\x12>\n\x07GetData\x12\x18.windmill.GetDataRequest\x1a\x19.windmill.GetDataResponse\x12G\n\nCommitWork\x12\x1b.windmill.CommitWorkRequest\x1a\x1c.windmill.CommitWorkResponse\x12\x44\n\tGetConfig\x12\x1a.windmill.GetConfigRequest\x1a\x1b.windmill.GetConfigResponse\x12J\n\x0bReportStats\x12\x1c.windmill.ReportStatsRequest\x1a\x1d.windmill.ReportStatsResponseB7\n5com.google.cloud.dataflow.sdk.runners.worker.windmill')
  ,
  dependencies=[windmill__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)





DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n5com.google.cloud.dataflow.sdk.runners.worker.windmill'))
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities


class BetaCloudWindmillServiceV1Alpha1Servicer(object):
  """The Cloud Windmill Service API used by GCE to acquire and process streaming
  Dataflow work.
  """
  def GetWork(self, request, context):
    """Gets streaming Dataflow work.
    """
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
  def GetData(self, request, context):
    """Gets data from Windmill.
    """
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
  def CommitWork(self, request, context):
    """Commits previously acquired work.
    """
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
  def GetConfig(self, request, context):
    """Gets dependant configuration from windmill.
    """
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
  def ReportStats(self, request, context):
    """Reports stats to Windmill.
    """
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


class BetaCloudWindmillServiceV1Alpha1Stub(object):
  """The Cloud Windmill Service API used by GCE to acquire and process streaming
  Dataflow work.
  """
  def GetWork(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    """Gets streaming Dataflow work.
    """
    raise NotImplementedError()
  GetWork.future = None
  def GetData(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    """Gets data from Windmill.
    """
    raise NotImplementedError()
  GetData.future = None
  def CommitWork(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    """Commits previously acquired work.
    """
    raise NotImplementedError()
  CommitWork.future = None
  def GetConfig(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    """Gets dependant configuration from windmill.
    """
    raise NotImplementedError()
  GetConfig.future = None
  def ReportStats(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    """Reports stats to Windmill.
    """
    raise NotImplementedError()
  ReportStats.future = None


def beta_create_CloudWindmillServiceV1Alpha1_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
  request_deserializers = {
    ('google.dataflow.windmillservice.v1alpha1.CloudWindmillServiceV1Alpha1', 'CommitWork'): windmill__pb2.CommitWorkRequest.FromString,
    ('google.dataflow.windmillservice.v1alpha1.CloudWindmillServiceV1Alpha1', 'GetConfig'): windmill__pb2.GetConfigRequest.FromString,
    ('google.dataflow.windmillservice.v1alpha1.CloudWindmillServiceV1Alpha1', 'GetData'): windmill__pb2.GetDataRequest.FromString,
    ('google.dataflow.windmillservice.v1alpha1.CloudWindmillServiceV1Alpha1', 'GetWork'): windmill__pb2.GetWorkRequest.FromString,
    ('google.dataflow.windmillservice.v1alpha1.CloudWindmillServiceV1Alpha1', 'ReportStats'): windmill__pb2.ReportStatsRequest.FromString,
  }
  response_serializers = {
    ('google.dataflow.windmillservice.v1alpha1.CloudWindmillServiceV1Alpha1', 'CommitWork'): windmill__pb2.CommitWorkResponse.SerializeToString,
    ('google.dataflow.windmillservice.v1alpha1.CloudWindmillServiceV1Alpha1', 'GetConfig'): windmill__pb2.GetConfigResponse.SerializeToString,
    ('google.dataflow.windmillservice.v1alpha1.CloudWindmillServiceV1Alpha1', 'GetData'): windmill__pb2.GetDataResponse.SerializeToString,
    ('google.dataflow.windmillservice.v1alpha1.CloudWindmillServiceV1Alpha1', 'GetWork'): windmill__pb2.GetWorkResponse.SerializeToString,
    ('google.dataflow.windmillservice.v1alpha1.CloudWindmillServiceV1Alpha1', 'ReportStats'): windmill__pb2.ReportStatsResponse.SerializeToString,
  }
  method_implementations = {
    ('google.dataflow.windmillservice.v1alpha1.CloudWindmillServiceV1Alpha1', 'CommitWork'): face_utilities.unary_unary_inline(servicer.CommitWork),
    ('google.dataflow.windmillservice.v1alpha1.CloudWindmillServiceV1Alpha1', 'GetConfig'): face_utilities.unary_unary_inline(servicer.GetConfig),
    ('google.dataflow.windmillservice.v1alpha1.CloudWindmillServiceV1Alpha1', 'GetData'): face_utilities.unary_unary_inline(servicer.GetData),
    ('google.dataflow.windmillservice.v1alpha1.CloudWindmillServiceV1Alpha1', 'GetWork'): face_utilities.unary_unary_inline(servicer.GetWork),
    ('google.dataflow.windmillservice.v1alpha1.CloudWindmillServiceV1Alpha1', 'ReportStats'): face_utilities.unary_unary_inline(servicer.ReportStats),
  }
  server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
  return beta_implementations.server(method_implementations, options=server_options)


def beta_create_CloudWindmillServiceV1Alpha1_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
  request_serializers = {
    ('google.dataflow.windmillservice.v1alpha1.CloudWindmillServiceV1Alpha1', 'CommitWork'): windmill__pb2.CommitWorkRequest.SerializeToString,
    ('google.dataflow.windmillservice.v1alpha1.CloudWindmillServiceV1Alpha1', 'GetConfig'): windmill__pb2.GetConfigRequest.SerializeToString,
    ('google.dataflow.windmillservice.v1alpha1.CloudWindmillServiceV1Alpha1', 'GetData'): windmill__pb2.GetDataRequest.SerializeToString,
    ('google.dataflow.windmillservice.v1alpha1.CloudWindmillServiceV1Alpha1', 'GetWork'): windmill__pb2.GetWorkRequest.SerializeToString,
    ('google.dataflow.windmillservice.v1alpha1.CloudWindmillServiceV1Alpha1', 'ReportStats'): windmill__pb2.ReportStatsRequest.SerializeToString,
  }
  response_deserializers = {
    ('google.dataflow.windmillservice.v1alpha1.CloudWindmillServiceV1Alpha1', 'CommitWork'): windmill__pb2.CommitWorkResponse.FromString,
    ('google.dataflow.windmillservice.v1alpha1.CloudWindmillServiceV1Alpha1', 'GetConfig'): windmill__pb2.GetConfigResponse.FromString,
    ('google.dataflow.windmillservice.v1alpha1.CloudWindmillServiceV1Alpha1', 'GetData'): windmill__pb2.GetDataResponse.FromString,
    ('google.dataflow.windmillservice.v1alpha1.CloudWindmillServiceV1Alpha1', 'GetWork'): windmill__pb2.GetWorkResponse.FromString,
    ('google.dataflow.windmillservice.v1alpha1.CloudWindmillServiceV1Alpha1', 'ReportStats'): windmill__pb2.ReportStatsResponse.FromString,
  }
  cardinalities = {
    'CommitWork': cardinality.Cardinality.UNARY_UNARY,
    'GetConfig': cardinality.Cardinality.UNARY_UNARY,
    'GetData': cardinality.Cardinality.UNARY_UNARY,
    'GetWork': cardinality.Cardinality.UNARY_UNARY,
    'ReportStats': cardinality.Cardinality.UNARY_UNARY,
  }
  stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
  return beta_implementations.dynamic_stub(channel, 'google.dataflow.windmillservice.v1alpha1.CloudWindmillServiceV1Alpha1', cardinalities, options=stub_options)
# @@protoc_insertion_point(module_scope)
