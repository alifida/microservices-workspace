# FastAPI Microservices with Kafka and gRPC

This repository demonstrates how to create a set of microservices using **FastAPI**, **Kafka**, and **gRPC** to allow services to communicate with each other. The system consists of three services that interact with one another in the following manner:

1. **Service 1 (Kafka Producer)**: Sends messages to a Kafka topic.
2. **Service 2 (Kafka Consumer and gRPC Client)**: Consumes messages from the Kafka topic and forwards them to a gRPC server.
3. **Service 3 (gRPC Server)**: Receives and processes messages via gRPC.

## Architecture Overview

- **Kafka**: Used for asynchronous messaging between the services.
- **gRPC**: Used for synchronous communication between Service 2 (Kafka Consumer) and Service 3 (gRPC Server).

## Requirements

Before you begin, make sure you have the following installed:

### Software Dependencies:
1. **Kafka**: Kafka should be running on your local machine. If you don't have Kafka set up, you can follow the official Kafka [quick start guide](https://kafka.apache.org/quickstart).
2. **Python 3.8+**: This project requires Python 3.8 or higher.
3. **Python Libraries**: The following Python libraries are required for running the services:
   - `fastapi`: For creating the FastAPI application.
   - `uvicorn`: ASGI server to run FastAPI.
   - `grpcio` and `grpcio-tools`: For gRPC communication between services.
   - `kafka-python`: For Kafka integration in the producer and consumer services.

You can install the dependencies using the following command:

 
pip install fastapi uvicorn grpcio grpcio-tools kafka-python


### Kafka Setup
**Kafka** should be running on your machine, and the default Kafka port is localhost:9092.
You should also have Zookeeper running if you're using a separate Zookeeper instance.


### gRPC Setup
A .proto file is used to define the message types and the service interface. The protobuf file services.proto is defined as follows:

 
syntax = "proto3";

package communication;

message Request {
  string message = 1;
}

message Response {
  string message = 1;
}

service CommunicationService {
  rpc sendMessage(Request) returns (Response);
}




You can generate the necessary Python files (services_pb2.py and services_pb2_grpc.py) by running:

 
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. services.proto



###Services Overview
**Service 1: Kafka Producer**
This service acts as the Kafka producer. It listens for incoming HTTP POST requests and sends the message content to a Kafka topic (my_topic). This service uses the KafkaProducer from the kafka-python library to send the message.

**Service 2: Kafka Consumer and gRPC Client**
This service acts as the Kafka consumer. It continuously listens to the Kafka topic (my_topic) for new messages. Once it receives a message, it forwards the message to Service 3 (gRPC Server) using gRPC. The communication between Service 2 and Service 3 is handled by the grpcio library, where Service 2 acts as the gRPC client.

**Service 3: gRPC Server**
This service implements the gRPC server. It listens for incoming gRPC requests from Service 2, processes the message, and responds back to Service 2. The gRPC server is created using the gRPC Python library, and the service interface is defined in the services.proto file.

### Running the Services
**Start Kafka**: Ensure Kafka and Zookeeper are running on your machine. By default, Kafka listens on localhost:9092.

**Run Service 1 (Kafka Producer):**

This service sends messages to the Kafka topic my_topic.
Start the service by running:

`uvicorn service1:app --reload --host 0.0.0.0 --port 8001`


**Run Service 2 (Kafka Consumer and gRPC Client):**

This service listens for messages on the Kafka topic my_topic, then forwards those messages to Service 3 using gRPC.
Start the service by running:


`uvicorn service2:app --reload --host 0.0.0.0 --port 8002`


**Run Service 3 (gRPC Server):**

This service handles incoming gRPC requests from Service 2.
Start the service by running:


`uvicorn service3:app --reload --host 0.0.0.0 --port 8003`

### Interaction Flow

**Service 1**: Sends a message to Kafka through an HTTP POST request. For example:

`curl -X 'POST' \
  'http://localhost:8000/send/' \
  -H 'Content-Type: application/json' \
  -d '{
  "message": "Hello from Service 1"
}'`

**Service 2**: Consumes the message from Kafka and forwards it to **Service 3** using gRPC.

**Service 3**: Processes the message via gRPC and sends a response back.

**Service 2**: The response from Service 3 is received and logged.

### Explanation of gRPC Integration
**Service 3** implements the gRPC server and defines the service method sendMessage. This method is responsible for handling the gRPC requests sent by Service 2.

**Service 2** sends the message to Service 3 by calling the sendMessage RPC method.

**Service 3** responds with a message confirming it received and processed the message.

**Running Kafka and gRPC Simultaneously**
The gRPC server in Service 3 runs on a separate thread alongside FastAPI by using asyncio. This ensures that FastAPI's HTTP server doesn't block the execution of the gRPC server.
**Troubleshooting**
Ensure Kafka is running on localhost:9092 and that there are no issues with the Kafka topic my_topic.
Verify that all services are running on the correct ports and are able to communicate with each other (e.g., Service 2 should be able to reach Service 3 on port 50051 for gRPC).
If you encounter issues with gRPC, ensure that the .proto file is correctly compiled and that the generated files are being used.
