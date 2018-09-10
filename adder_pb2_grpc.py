# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import adder_pb2 as adder__pb2


class AdderStub(object):
  """The adding service definition.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.add = channel.unary_unary(
        '/adder.Adder/add',
        request_serializer=adder__pb2.AddRequest.SerializeToString,
        response_deserializer=adder__pb2.AddResult.FromString,
        )


class AdderServicer(object):
  """The adding service definition.
  """

  def add(self, request, context):
    """Adds Two Numbers
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_AdderServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'add': grpc.unary_unary_rpc_method_handler(
          servicer.add,
          request_deserializer=adder__pb2.AddRequest.FromString,
          response_serializer=adder__pb2.AddResult.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'adder.Adder', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))