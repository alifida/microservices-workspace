import logging
import grpc
from grpc_stub.service2 import services_pb2
from grpc_stub.service2 import services_pb2_grpc
from kafka import KafkaConsumer
import json
from fastapi import FastAPI, BackgroundTasks

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

consumer = KafkaConsumer(
    'my_topic',
    bootstrap_servers='localhost:9092',
    #group_id='my-group',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

def grpc_send_message(message):
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = services_pb2_grpc.CommunicationServiceStub(channel)
        response = stub.sendMessage(services_pb2.Request(message=message))
        logger.info("gRPC response: %s", response.message)

# Move the Kafka consumer to a background task
def consume_kafka_messages():
    for message in consumer:
        logger.info(f"Received message from Kafka: {message.value}")
        grpc_send_message(message.value["message"])

@app.on_event("startup")
async def startup_event():
    from threading import Thread
    kafka_thread = Thread(target=consume_kafka_messages)
    kafka_thread.daemon = True  # Allow thread to exit when the main program exits
    kafka_thread.start()

@app.get("/")
async def read_root():
    return {"message": "API is running!"}
