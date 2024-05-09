from calculator_pb2_grpc import CalculatorServicer

from calculator_pb2 import SumRequest
from calculator_pb2 import SumReply
from calculator_pb2 import MultRequest
from calculator_pb2 import MultReply
from calculator_pb2 import GreatestRequest
from calculator_pb2 import GreatestReply
from calculator_pb2 import DivRequest
from calculator_pb2 import DivReply

from grpc import ServicerContext


class Calculator(CalculatorServicer):

    def Sum(self, request: SumRequest, context: ServicerContext) -> SumReply:
        return SumReply(s=request.a + request.b)
    
    def Mult(self, request: MultRequest, context: ServicerContext) -> MultReply:
        return MultReply(p=request.a * request.b)
    
    def Greatest(self, request: GreatestRequest, context: ServicerContext) -> GreatestReply:
        return GreatestReply(g=max(request.a, request.b, request.c))
    
    def Div(self, request: DivRequest, conntext: ServicerContext) -> DivReply:
        return DivReply(q=int(request.a / request.b), r=request.a % request.b)

