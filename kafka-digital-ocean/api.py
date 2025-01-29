from fastapi import FastAPI
from confluent_kafka import Producer

# Initialize the FastAPI app
app = FastAPI()

# Kafka configuration
KAFKA_BROKER = "db-kafka-dev-do-user-1010676-0.g.db.ondigitalocean.com:25062"
SSL_CERTIFICATE = "/media/ali/workspace/workspace/fellowpro-ubuntu/microservices-workspace/kafka-digital-ocean/files/user-access-certificate.crt"
SSL_KEY = "/media/ali/workspace/workspace/fellowpro-ubuntu/microservices-workspace/kafka-digital-ocean/files/user-access-key.key"
SSL_CA_CERTIFICATE = "/media/ali/workspace/workspace/fellowpro-ubuntu/microservices-workspace/kafka-digital-ocean/files/root-ca.pem"

# Kafka producer configuration
kafka_config = {
    "bootstrap.servers": KAFKA_BROKER,
    "security.protocol": "SSL",
    "ssl.certificate.location": SSL_CERTIFICATE,
    "ssl.key.location": SSL_KEY,
    'ssl.endpoint.identification.algorithm': 'none',
    "ssl.ca.location": SSL_CA_CERTIFICATE,
}

# Create the Kafka producer
producer = Producer(kafka_config)

@app.post("/produce")
async def produce_message(topic: str, message: str):
    try:
        # Send a message to the Kafka topic
        producer.produce(topic, value=message)
        producer.flush()  # Ensure the message is sent
        return {"status": "Message sent successfully"}
    except Exception as e:
        return {"status": "Error", "message": str(e)}
