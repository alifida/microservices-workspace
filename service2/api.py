# Service 2: Kafka Consumer
# This service listens to Kafka topics and processes incoming messages.
# service2.py (updated to include gRPC communication)
import grpc
from grpc_stub.service2 import services_pb2
from grpc_stub.service2 import services_pb2_grpc
from kafka import KafkaConsumer
import json
from fastapi import FastAPI

app = FastAPI()

consumer = KafkaConsumer(
    'my_topic',
    bootstrap_servers='localhost:9092',
    group_id='my-group',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

def grpc_send_message(message):
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = services_pb2_grpc.CommunicationServiceStub(channel)
        response = stub.sendMessage(services_pb2.Request(message=message))
        print("gRPC response:", response.message)

@app.on_event("startup")
async def startup_event():
    # Start consuming messages
    for message in consumer:
        print(f"Received message from Kafka: {message.value}")
        grpc_send_message(message.value["message"])


