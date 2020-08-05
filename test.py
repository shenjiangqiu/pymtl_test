from pymtl3 import *
from pymtl3.stdlib.queues import PipeQueueRTL
from pymtl3.stdlib.ifcs import RecvIfcRTL, SendIfcRTL


class TestComponent(Component):
    def construct(s):
        s.recv = RecvIfcRTL(b32)
        s.send = SendIfcRTL(b32)
        s.q = PipeQueueRTL(b32, 64)
        s.recv //= s.q.enq

        @update
        def comb():
            s.send.en@=s.send.rdy & s.q.deq.rdy
            s.q.deq.en@=s.send.rdy & s.q.deq.rdy
