# Service 1: Kafka Producer
# This service sends messages to Kafka.

import asyncio
import json
from fastapi import FastAPI
from kafka import KafkaProducer
from pydantic import BaseModel

app = FastAPI()

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

class Message(BaseModel):
    message: str

@app.post("/send/")
async def send_message(msg: Message):
    # Send message to Kafka topic
    producer.send('my_topic', {"message": msg.message})
    producer.flush()
    return {"status": "message sent to Kafka"}

