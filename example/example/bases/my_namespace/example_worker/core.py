from faststream import FastStream
from faststream.rabbit import RabbitBroker

from my_namespace.events import ExampleEvent

broker = RabbitBroker('ampqs://guest:guest@rabbitmq:5672/')
app = FastStream(broker)

@broker.subscriber('example')
async def handle(msg: ExampleEvent):
    print(msg)

@broker.subscriber('another_example')
async def another_handle(msg:ExampleEvent):
    print(msg.message)