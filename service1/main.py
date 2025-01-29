# Service 1: Kafka Producer
# This service sends messages to Kafka.

import asyncio
import json
from fastapi import FastAPI
from kafka import KafkaProducer
from pydantic import BaseModel

from grpc_stub.service1.services_pb2 import Request

app = FastAPI()

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    #value_serializer=lambda v: json.dumps(v).encode('utf-8')
    #value_serializer=lambda v: v.SerializeToString()  # Serialize Protobuf message to bytes
)

class Message(BaseModel):
    message: str

@app.post("/send/")
async def send_message(msg: Message):  # msg is a Pydantic model
    # Extract the string from the Pydantic model
    kafka_message = Request(message=msg.message)  # <-- Fix: Use msg.message

    # Send serialized message to Kafka
    producer.send('my_topic', kafka_message.SerializeToString())
    producer.flush()
    print(f"Message Sent to Kafka: {msg.message}")
    return {"status": "message sent to Kafka"}
